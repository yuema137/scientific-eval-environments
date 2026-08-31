import struct
from pathlib import Path

from scripts.build_explorer_site import build_site
from scripts.export_explorer_data import build_dataset, write_dataset, write_documents


ROOT = Path(__file__).resolve().parents[1]


def test_build_dataset_contains_expected_axes_and_card():
    data = build_dataset(ROOT)
    assert data["ground_truth"]["markdown"] is True
    assert data["stats"]["works"] > 300
    assert any(item["slug"] == "scientific_agents" for item in data["topics"])
    assert any(item["slug"] == "physics" for item in data["domains"])
    assert any(item["slug"] == "scientific_problem_solving_reasoning" for item in data["activities"])
    assert len(data["monthly_reports"]) > 0

    work = next(item for item in data["works"] if item["slug"] == "agentrewardbench")
    assert work["first_appeared"].startswith("2025-04-")
    assert "arXiv" in work["first_appeared_source"]["label"]
    assert any(topic["slug"] == "trajectory_evaluation" for topic in work["topics"])
    physics = next(item for item in data["domains"] if item["slug"] == "physics")
    assert physics["zh_url"] == "./documents/zh/domains/physics.json"
    assert physics["zh_name"]
    assert data["documents"]["README.md"]["url"] == "./documents/en/README.json"


def test_write_dataset_creates_json(tmp_path):
    output = tmp_path / "data" / "index.json"
    write_dataset(build_dataset(ROOT), output)
    assert output.exists()
    text = output.read_text(encoding="utf-8")
    assert '"works"' in text


def test_dataset_generation_is_deterministic():
    assert build_dataset(ROOT) == build_dataset(ROOT)


def test_write_documents_creates_localized_json(tmp_path):
    write_documents(tmp_path, ROOT)
    english = tmp_path / "documents" / "en" / "topics" / "scientific_agents.json"
    chinese = tmp_path / "documents" / "zh" / "topics" / "scientific_agents.json"
    assert english.exists()
    assert chinese.exists()
    assert '"source_path": "topics/scientific_agents.md"' in english.read_text(encoding="utf-8")


def test_production_bundle_is_self_contained(tmp_path):
    output = tmp_path / "scieval"
    build_site(output, "test-sha")
    assert (output / "index.html").exists()
    assert (output / "data" / "index.json").exists()
    assert (output / "documents" / "en" / "README.json").exists()
    assert (output / "documents" / "zh" / "monthly" / "README.json").exists()
    assert (output / "assets" / "social-preview.png").exists()
    assert not list(output.rglob("*.md"))
    assert '"source_sha": "test-sha"' in (output / "manifest.json").read_text(encoding="utf-8")


def test_markdown_navigation_uses_the_in_page_reader():
    index = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    app = (ROOT / "site" / "app.js").read_text(encoding="utf-8")

    assert 'id="monthly-link" data-reader-link="true"' in index
    assert 'id="github-link"' in index
    assert "https://github.com/yuema137/scientific-eval-environments" in index
    assert 'id="tab-reader"' not in index
    assert 'id="reader-subtitle"' not in index
    assert 'id="reader-source-link"' not in index
    assert '>Guide</a>' in index
    assert "<title>Scientific Evaluation Environments</title>" in index
    assert '<h1 id="hero-title">Scientific Evaluation Environments</h1>' in index
    assert 'class="repo-map-figure"' in index
    assert "renderMarkdown(document.markdown, document.source_path)" in app
    assert "resolveDocumentLink(href, sourcePath)" in app
    assert "localizedDocumentUrl(state.reader.url)" in app
    assert 'localStorage.setItem("scieval-explorer-language", state.lang)' in app
    assert "languageSwitcher.test(line.trim())" in app
    assert 'link.dataset.readerLink !== "true" && !isLocalDocumentLink(href)' in app
    assert 'class="table-scroll${wideClass}"' in app
    assert "response.json()" in app
    assert "../README.md" not in index
    assert "Content-Security-Policy" in index
    assert '<link rel="canonical" href="https://yuema137.github.io/scieval/">' in index
    assert '<meta property="og:image" content="https://yuema137.github.io/scieval/assets/social-preview.png">' in index
    assert '<meta name="twitter:card" content="summary_large_image">' in index

    styles = (ROOT / "site" / "styles.css").read_text(encoding="utf-8")
    assert ".table-scroll.is-wide" in styles
    assert "position: sticky" in styles
    assert ".header-actions .button" in styles
    assert "flex-wrap: nowrap" in styles
    assert "--maxw: 1400px" in styles
    assert ".figure-stack .repo-map-figure" in styles
    assert "font-size: clamp(1.3rem, 1.6vw, 1.55rem)" in styles
    assert ".hero-grid" in styles
    assert "grid-template-columns: minmax(0, 1fr)" in styles


def test_every_rendered_markdown_page_has_a_chinese_mirror():
    for folder in ("topics", "domains", "activities", "monthly", "works"):
        english = {path.name for path in (ROOT / folder).glob("*.md")}
        chinese = {path.name for path in (ROOT / "zh" / folder).glob("*.md")}
        assert english == chinese, folder


def test_diagram_connectors_render_behind_nodes():
    loop = (ROOT / "site" / "assets" / "readme-eval-loop.svg").read_text(encoding="utf-8")
    repo_map = (ROOT / "site" / "assets" / "readme-repo-map.svg").read_text(encoding="utf-8")

    assert loop.index('stroke="#7C4DFF"') < loop.index('<rect x="60" y="132"')
    assert repo_map.index('stroke="#7C4DFF"') < repo_map.index('<circle cx="600" cy="380"')
    assert '<g text-anchor="middle" fill="#4E5F7A"' in loop
    assert repo_map.count('text-anchor="middle"') >= 5
    assert "Factual cards for individual papers," not in repo_map


def test_social_preview_has_standard_large_card_dimensions():
    preview = ROOT / "site" / "assets" / "social-preview.png"
    with preview.open("rb") as image:
        assert image.read(8) == b"\x89PNG\r\n\x1a\n"
        assert image.read(4) == b"\x00\x00\x00\r"
        assert image.read(4) == b"IHDR"
        width, height = struct.unpack(">II", image.read(8))
    assert (width, height) == (1200, 630)

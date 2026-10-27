import json
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


def test_works_are_ordered_by_first_appearance_newest_first():
    works = build_dataset(ROOT)["works"]
    assert [work["first_appeared"] for work in works] == sorted(
        (work["first_appeared"] for work in works), reverse=True
    )
    for left, right in zip(works, works[1:]):
        if left["first_appeared"] == right["first_appeared"]:
            assert left["title"].casefold() <= right["title"].casefold()


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
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["source_sha"] == "test-sha"
    assert manifest["source_committed_at"] == "unknown"
    assert manifest["latest_first_appeared"]
    assert manifest["latest_monthly_report"]


def test_manifest_records_explicit_snapshot_date(tmp_path):
    output = tmp_path / "scieval"
    build_site(output, "test-sha", "2026-10-01T00:00:00+00:00")
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["source_committed_at"] == "2026-10-01T00:00:00+00:00"


def test_axis_lists_contain_only_their_own_pages():
    data = build_dataset(ROOT)
    for kind in ("topics", "domains", "activities"):
        assert len(data[kind]) <= data["stats"][kind], kind
        for item in data[kind]:
            assert item["url"] == f"./documents/en/{kind}/{item['slug']}.json", item
            assert item["zh_url"] == f"./documents/zh/{kind}/{item['slug']}.json", item
            assert (ROOT / "zh" / kind / f"{item['slug']}.md").exists(), item
    for work in data["works"]:
        for kind in ("topics", "activities"):
            for item in work[kind]:
                assert item["url"].startswith(f"./documents/en/{kind}/"), (work["slug"], item)
    # A Topics block that only cross-references a domain is not a topic membership.
    pac_bench = next(work for work in data["works"] if work["slug"] == "pac-bench")
    assert pac_bench["topics"] == []
    assert any(domain["slug"] == "robotics" for domain in pac_bench["domains"])


def test_explorer_escapes_data_and_checks_link_schemes():
    app = (ROOT / "site" / "app.js").read_text(encoding="utf-8")
    index = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    for fragment in (
        "${escapeHtml(work.title)}</a>",
        "<p>${escapeHtml(blurb)}</p>",
        "<p>${escapeHtml(summary)}</p>",
        "escapeHtml(safeHref(link.url))",
        "${escapeHtml(link.label)}</a>",
        "${escapeHtml(name)}</a>",
        "${escapeHtml(title)}</a>",
        "if (!isSafeHref(unescapeHtml(resolvedHref))) return safeLabel;",
        "if (!response.ok) throw new Error",
        "main().catch(showLoadError);",
    ):
        assert fragment in app, fragment
    assert "localStorage.setItem" in app and app.count("localStorage.setItem") == 1
    assert 'role="tablist"' in index
    assert index.count('role="tab" aria-selected=') == 6
    assert index.count('role="tabpanel"') == 6
    for control in ("search", "topic-filter", "domain-filter", "activity-filter", "month-filter"):
        assert f'id="{control}"' in index
        tag = index.split(f'id="{control}"', 1)[1].split(">", 1)[0]
        assert "aria-label=" in tag, control


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
    assert "<title>Evaluating AI Scientists</title>" in index
    assert '<h1 id="hero-title">Evaluating AI Scientists</h1>' in index
    assert "repo-map-figure" in index
    assert "readme-eval-loop-dark.svg" in index
    assert "readme-repo-map-dark.svg" in index
    assert "renderMarkdown(document.markdown, document.source_path)" in app
    assert "resolveDocumentLink(href, sourcePath)" in app
    assert "localizedDocumentUrl(state.reader.url)" in app
    assert "right.first_appeared.localeCompare(left.first_appeared)" in app
    assert 'savePreference("scieval-explorer-language", state.lang)' in app
    assert "languageSwitcher.test(line.trim())" in app
    assert 'link.dataset.readerLink !== "true" && !isLocalDocumentLink(href)' in app
    assert 'class="table-scroll${wideClass}"' in app
    assert "response.json()" in app
    assert "../README.md" not in index
    assert "Content-Security-Policy" in index
    assert '<link rel="canonical" href="https://yuema137.github.io/scieval/">' in index
    assert '<meta property="og:image" content="https://yuema137.github.io/scieval/assets/social-preview.png">' in index
    assert '<meta name="twitter:card" content="summary_large_image">' in index
    assert 'class="theme-switch"' in index
    assert 'id="theme-light"' in index
    assert 'id="theme-dark"' in index
    assert 'readPreference("scieval-explorer-theme") || "dark"' in app
    assert 'savePreference("scieval-explorer-theme", theme)' in app
    assert 'document.documentElement.dataset.theme = state.theme' in app

    styles = (ROOT / "site" / "styles.css").read_text(encoding="utf-8")
    assert ".table-scroll.is-wide" in styles
    assert "position: sticky" in styles
    assert ".header-actions" in styles
    assert "--maxw: 1400px" in styles
    assert ".figure-stack .repo-map-figure" in styles
    assert ':root[data-theme="light"]' in styles
    assert "color-scheme: dark" in styles
    assert "color-scheme: light" in styles
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

    assert loop.index('stroke="#3D91F2"') < loop.index('<rect x="60" y="132"')
    assert repo_map.index('stroke="#3D91F2"') < repo_map.index('<circle cx="600" cy="380"')
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

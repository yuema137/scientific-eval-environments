# Explorer Site

This directory is the repository's visual render layer.

It exists because the Markdown knowledge base is good for maintenance, citation, and review, but not ideal for interactive browsing.

## Ground-truth rule

The repository's Markdown files are the only source of truth:

- `works/` and `zh/works/`
- `topics/`
- `domains/`
- `activities/`
- `monthly/` and `zh/monthly/`
- root `README.md` and `zh/README.md`

The explorer must not introduce hand-maintained content that can drift away from those files.

## How it is built

- `scripts/build_explorer_site.py` builds a self-contained static bundle from the Markdown corpus.
- `scripts/export_explorer_data.py` exports the structured index and wraps rendered Markdown documents in JSON.
- `site/index.html`, `site/app.js`, and `site/styles.css` render that exported JSON.
- `site/assets/social-preview.png` and the Open Graph metadata in `site/index.html` provide the public link preview used by social platforms.
- `.github/workflows/explorer-pages.yml` validates the bundle and pushes only `scieval/` to the personal-site repository's `auto/scieval-sync` branch, using `PERSONAL_SITE_DEPLOY_KEY`.
- The receiving repository's [validate-scieval-sync.yml](https://github.com/yuema137/yuema137.github.io/blob/main/.github/workflows/validate-scieval-sync.yml) handles that push: it checks the publication boundary and static files, creates or refreshes the snapshot PR, merges the validated generated snapshot, and requests the Pages deployment.
- The knowledge-base updater's PR is separate and always requires human review. The receiving site's automatic merge applies only to generated website files from already-merged source content.

If the website stops updating, inspect both repositories: first the source's **Publish Explorer Snapshot** run and `auto/scieval-sync` push, then the destination's **Validate and Publish SciEval Snapshot** and Pages runs. A successful source run confirms the handoff, not completion of the destination deployment. The destination must retain its push-triggered workflow and the deploy key must retain access.

`site/data/` and `site/documents/` are generated output and are ignored in git. They may exist locally for preview, but they are never source content.

## Local preview

From the repository root:

```bash
python3 scripts/export_explorer_data.py --output site/data/index.json --documents-output site
python3 -m http.server 8000
```

Then open `http://localhost:8000/site/`.

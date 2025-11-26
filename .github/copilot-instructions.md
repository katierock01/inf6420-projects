<!-- Copilot/AI agent instructions: concise and actionable guidance for INF6420 -->

# INF6420 repo — Copilot instructions (short)

Purpose: Assist a GitHub Copilot/AI agent to quickly understand, update, and maintain this static INF6420 portfolio site.

- Big picture: Static HTML/CSS/PHP site; main content in `inf6420-projects/`; single-page course hub at `rock-INF6420-index.html` in root. No build system — files are served as-is via SFTP.

- Key files & locations:
	- `rock-INF6420-index.html` (root hub)
	- `inf6420-projects/` (Project pages and assets), `inf6420-projects/project3/`, `project4/`
    - `inf6420-projects/rock-project2.1.docx` (Project 2.1 paper)
	- `styles/brand.css` (global theme variables)
	- `.github/audit_layout.py`, `.github/cleanup_inf6420.py` (audit/cleanup helpers)
	- `scripts/upload_22.py` (SFTP deployment; uses Paramiko or OpenSSH fallback)
	- `devcontainer/devcontainer.json` (recommended dev environment)

- Typical agent workflows (concrete):
	1. Run structure audit: `python3 .github/audit_layout.py` from the repo root (inspect output for missing/obsolete items).
	2. If audit reports legacy folders, run cleanup: `python3 .github/cleanup_inf6420.py` (the script copies/moves into `inf6420-projects/` and renames legacy folders `*-old`).
	3. Open the devcontainer (recommended) or run `pip install -r requirements.txt` and serve files locally with Live Server (port 5500) to test navigation.
	4. Deploy for verification: `python3 scripts/upload_22.py` (set SFTP_* env vars to override defaults). The script will verify HTTP endpoints after upload.

- Project conventions to follow:
	- Use lowercase, hyphenated filenames (e.g., `rock-project2-2.html`). Keep `home.html` as the entry for projects.
	- Maintain relative paths for assets; image files reside in `images/` or `inf6420-projects/*/images/`.
	- Theme via `styles/brand.css` variables — avoid hard-coded colors.
	- Server-side form handlers live as PHP (`showform.php`) — do not replace with external libs.

- Integration notes & CI:
	- No external build; treat as deploy-as-is. Devcontainer installs Python & Node for convenience.
	- `scripts/upload_22.py` accepts `SFTP_HOST`, `SFTP_USER`, `SFTP_PORT`, and optionally `SFTP_REMOTE_BASE` environment variables.
	- If you see unrelated GitHub Actions (e.g., `python-publish.yml`), ignore or remove it; it’s not used for the site.

- Safety & PR conventions:
	- Never commit credentials or `.env` files. Use environment variables for SFTP upload.
	- When committing large cleanups, use a single clear message: `Standardize INF6420 project layout and apply EmpathTech theme`.
	- Open a PR for non-trivial changes and include `audit` output and a short test checklist (local live preview + post-deploy HTTP checks).

Examples and gotchas:
	- To confirm the root hub is accessible, the `rock-INF6420-index.html` file must be at repo root.
	- `cleanup_inf6420.py` renames legacy directories with `-old`. Remove them only after manual review.
	- Use `python3` instead of `python` when in doubt on Linux/Ubuntu devcontainers.

If a section here is unclear, tell me which part (deploy, cleanup, devcontainer, or theme) and I’ll expand the checklist for the agent.


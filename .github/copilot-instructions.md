# AI Coding Agent Instructions – `inf6420-projects`

These instructions are for AI coding agents working in this repository for INF 6420 (Web Development and Scripting).

## 1. Big Picture

- This repo is the **hub for all course web projects**; it mirrors the WSU web space but the **WSU server is the grading source of truth**.
- The codebase is almost entirely **static HTML/CSS**, plus a few helper **PowerShell** and **Python** scripts for deployment and packaging.
- Accessibility (WCAG), semantic HTML, and W3C validation are **non‑negotiable requirements**. Do not introduce layout hacks that break semantics or validation.

Key entry points:
- `index.html` – main hub listing projects and links.
- `submission.html` – grader‑focused page with W3C validator links.
- `docs/index.html` – assignment documentation hub.
- Project roots: `rock-Project1/`, `rock-Project2.1/`, `rock-Project2.2/`, `project3/`, `project4/`.

## 2. Structure & Conventions

- **Project directories** are named per assignment (e.g., `rock-Project2.2/`) and may have their own internal structure.
  - Project 2.2 main page: `rock-Project2.2/rock-project2-2.html` (internal CSS on purpose).
  - Project 3 multi‑page site: `project3/` (`home.html`, `fox.html`, `gray.html`, `red.html`, `flying.html`, `squirrels.css`).
- **Shared assets**:
  - CSS: `styles/brand.css` for hub‑level theming.
  - Images: `images/` at the repo root plus per‑project `images/` folders.
- **Docs & status**:
  - High‑level overview and live URLs: `README.md`.
  - Completion tracking: `PROJECT-STATUS.md` (treat as source of truth for what is "done").
  - Project management details: `PROJECT_MANAGEMENT.md`.
- **Do not rename** top‑level project directories or key HTML filenames without updating links in `index.html`, `submission.html`, and any cross‑page navigation.

## 3. Workflows & Commands

All commands assume **Windows PowerShell 5.1**.

**Package site for submission** (creates `dist/<repo-name>.zip`):
- Run from `scripts/` or project root:
  - `scripts/package_site.ps1`

**Deploy to WSU via PowerShell (WinSCP/OpenSSH)**:
- Script: `scripts/deploy.ps1`
- Behavior:
  - Resolves project root and uploads:
    - `index.html`, `submission.html`
    - `styles/brand.css`
    - core images: `images/background.svg`, `images/logo-icon.svg`, `images/logo-lockup.svg`
    - `rock-Project2.2/rock-project2-2.html`
  - Creates remote `images/`, `styles/`, `rock-Project2.2/` and attempts `chmod`.
- Usage pattern:
  - In PowerShell: `.\scripts\deploy.ps1` or `.\scripts\deploy.ps1 -Server 141.217.120.86 -User fn9575` (keep default values unless user updates them).

**Deploy to WSU via Python (Paramiko/OpenSSH)**:
- Script: `scripts/upload_22.py`.
- Behavior:
  - Computes project root (`scripts/..`).
  - Uploads hub pages, shared `images/` and `styles/`, key project files (1.1, 2.1 DOCX, 2.2, 2.3 index, `docs/index.html`), and optional avatar.
  - Tries Paramiko first (password prompt), otherwise falls back to `sftp` batch.
- Usage pattern:
  - `python scripts/upload_22.py`
  - Respect env vars if present: `SFTP_HOST`, `SFTP_USER`, `SFTP_PORT`, `SFTP_REMOTE_BASE`.

When modifying these scripts, keep:
- Paths consistent with existing directory layout.
- Interactive prompts minimal and clear.
- Windows‑friendly behavior (no Bash‑only syntax).

## 4. HTML/CSS Patterns

- Prefer **semantic HTML5**: `header`, `nav`, `main`, `section`, `article`, `footer`, etc.
- Maintain **consistent navigation** within a project (e.g., the squirrel pages in `project3/`). Reuse existing patterns instead of inventing new ones per page.
- Preserve and extend **accessibility features** already used in the repo:
  - Skip links, ARIA where appropriate, clear focus styles.
  - Don't remove `alt` text or replace text with images only.
- Follow **validator‑friendly** patterns:
  - Avoid inline event handlers and obsolete tags/attributes.
  - Close all elements properly; keep one `<h1>` per page.

When introducing new pages:
- Place them in the appropriate project folder.
- Wire them into existing navigation and the hub (`index.html`), if they should be discoverable.

## 5. Project‑Specific Gotchas

- Some files (e.g., DOCX for Project 2.1) are **intentionally excluded** by `.gitignore`; do not attempt to commit them.
- Linux paths on the WSU server are **case‑sensitive**. Keep path and filename casing exactly as in the repo when generating URLs or scripts.

## 6. How to Help Productively

When editing or adding code in this repo, AI agents should:
- Favor **small, focused changes** that don't break existing validator‑friendly HTML/CSS.
- Update **both** hub pages (`index.html`, `submission.html`) and project pages together when adding or renaming assignments.
- Keep deployment and packaging scripts in sync with any new top‑level project directories or key HTML entry points.
- Use existing files as patterns (e.g., `rock-Project2.2/rock-project2-2.html`, `project3/home.html`) instead of inventing entirely new structures.

If any of these instructions seem inconsistent with the current code, prefer the **actual code + README.md** and adjust this file rather than forcing the code to match outdated guidance.

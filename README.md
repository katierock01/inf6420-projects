# INF 6420 – Projects Hub

Course site and sources for INF 6420 by Katie Rock. This repo mirrors your student web space (WSU) but does not replace it. WSU URLs remain the source of truth for grading.

## Live WSU URLs

- Hub: http://141.217.120.86/fn9575/html/inf6420-projects/index.html
- Project 2.2: http://141.217.120.86/fn9575/html/inf6420-projects/project2.2/rock-project2-2.html
- Project 1.1 (links to 2.1 DOCX): http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project1.1/rock-Project1.1.index.html
- Direct Project 2.1 DOCX (optional): http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.1/rock-project2.1.docx

Validators (for 2.2):
- HTML: https://validator.w3.org/nu/?doc=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Fproject2.2%2Frock-project2-2.html
- CSS:  https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Fproject2.2%2Frock-project2-2.html

The Project 2.2 page also includes dynamic validator links that adapt to whatever URL you open.

## Repo layout

- `index.html` – Projects hub
- `submission.html` – Grader-friendly links and validators
- `docs/` – Assignment docs hub and helper text
- `images/`, `styles/` – Shared assets
- `rock-Project1.1/` – Project 1.1 page (links to 2.1 DOCX and 2.2)
- `rock-Project2.1/` – Landing + embedded doc scaffold; keep the DOCX outside of Git
- `project2.2/` – Final 2.2 HTML with internal CSS and validators
- `project3/` – Multi-page squirrels site with shared CSS and PHP form handler
- `scripts/` – Deployment and packaging helpers

Large binaries are excluded by default; `.gitignore` includes `*.docx`.

## Deploy to WSU (SFTP)

Prereqs: WSU VPN (if required), port 22 open. Your server is HTTP-only.

Option A — PowerShell (WinSCP or OpenSSH):
1. Open Windows PowerShell.
2. Run the deploy script:
   - If WinSCP is installed, it will be used automatically; otherwise OpenSSH `sftp` is used.
3. Accept the host key and enter your password when prompted.

Option B — Python (Paramiko/OpenSSH fallback):
1. Ensure Python 3 is installed. Optionally install `paramiko` for password-based SFTP.
2. Run `scripts/upload_22.py` and follow prompts (will fallback to system `sftp` if Paramiko isn’t available).

Notes:
- If port 22 is blocked on your network, connect to WSU VPN or use a different network (e.g., mobile hotspot).
- Linux paths on the server are case-sensitive.

## Package the site (ZIP for submission)

Use the PowerShell script to create a distributable ZIP under `dist/`:
- `scripts/package_site.ps1`

This bundles the hub, projects, docs, assets, and scripts.

## Optional: GitHub Pages

This repo includes a `.nojekyll` file so static assets serve correctly. To enable Pages:
1. In GitHub, go to Settings → Pages.
2. Source: choose `main` branch and `/ (root)`.
3. Save. Your site will publish at `https://<your-username>.github.io/inf6420-projects/`.

Important: Your official grading URLs remain the WSU-hosted HTTP links above.

## Accessibility & validation

- Strong keyboard focus styles, skip link, and semantic landmarks are included.
- `rock-Project2.2/rock-project2-2.html` uses internal CSS by design and includes dynamic validator links.
- `@media (prefers-reduced-motion: reduce)` and print styles are present.

## Troubleshooting

- DOCX downloads over HTTP may be flagged by the browser ("insecure"). Choose “Keep/Keep anyway.”
- If an image or doc 404s, verify the exact filename and capitalization on the server.
- If SFTP fails, check VPN/port 22 or use WinSCP GUI.

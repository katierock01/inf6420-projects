# INF 6420 – Projects Hub

Welcome to the **INF 6420 Projects Hub**. This repository holds the source files for all your INF 6420 assignments. It mirrors the directory structure you will maintain on the WSU server, but it does **not** replace that server—your WSU URLs remain the official grading links. Use this repo to develop, audit, and package your work before uploading.

## 🌐 Live WSU URLs

After you upload via SFTP/OwlFiles to `/home/fn9575/html/`, your projects will live here:

- **Course home (Project 1):**  
  [`http://141.217.120.86/fn9575/html/rock-INF6420-index.html`](http://141.217.120.86/fn9575/html/rock-INF6420-index.html)
- **Project 2.1 (DOCX):**  
  [`http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx`](http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx)
- **Project 2.2 (HTML):**  
  [`http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html`](http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html)
- **Project 3 (Squirrels site):**  
  [`http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html`](http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html)
- **Project 4 (Responsive redesign):**  
  [`http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html`](http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html)

Use these URLs in your documents. Do **not** link to old folder names such as `project1.1/` or `rock-Project2.3/`, which are deprecated.

## 🗂 Canonical Repository Layout

Your local repo (and your WSU server directory) should follow this layout exactly:

```
rock-INF6420-index.html        # Course homepage (Project 1)
img/                           # Your photo and shared images
inf6420-projects/
├ rock-project2.1.docx         # Project 2.1 paper
├ rock-project2-2.html         # Project 2.2 HTML/CSS version
├ project3/                    # Project 3: Squirrels site
│  ├ home.html, fox.html, red.html, gray.html, flying.html
│  ├ squirrels.css
│  ├ showform.php (if used)
│  └ images/
│      ├ home.jpg, fox.jpg, red.jpg, gray.jpg, flying.jpg
└ project4/                    # Project 4: Responsive redesign
   ├ home.html, fox.html, red.html, gray.html, flying.html
   ├ squirrels-responsive.css  # CSS with media queries
   └ images/
       ├ home.jpg, fox.jpg, red.jpg, gray.jpg, flying.jpg
scripts/                       # Deployment and packaging helpers
docs/                          # Assignment PDFs and rubric notes
styles/, images/               # Shared assets (e.g. brand.css)
README.md, submission.html     # This README and grader-friendly links/validators
```

Legacy directories (e.g. `project1.1/`, `project2.1/`, `project2.2/`, `project3/` duplicates, or `rock-Project2.3/`) should be removed or renamed with `-old` after you merge their contents into the canonical structure.

## 🛠 Development & Deployment Workflow

1. **Develop locally** – Edit your HTML, CSS and PHP files in `inf6420-projects/` and the course homepage (`rock-INF6420-index.html`). Keep your DOCX file out of version control if you prefer; the `.gitignore` excludes `*.docx` except for `rock-project2.1.docx`.
2. **Audit & organise** – Use a Python audit script (e.g. `python audit_layout.py`) to check for missing or misplaced files. Run a cleanup script (e.g. `python cleanup_inf6420.py`) to move everything into the canonical layout and rename legacy folders.
3. **Commit & push** – When your repo passes the audit, stage and commit your changes:
   ```bash
   git add -A
   git commit -m "Restructure to canonical layout and archive old folders"
   git push origin main
   ```
4. **Deploy via SFTP** – Connect to WSU VPN (GlobalProtect) and use WinSCP or OwlFiles to upload `rock-INF6420-index.html`, the `img/` folder, and `inf6420-projects/` to `/home/fn9575/html/`. Rename old server directories like `project3` or `project4` to `project3-old`/`project4-old` before uploading.
5. **Validate** – After deployment, test each page at the URLs above. Run the W3C HTML and CSS validators and replace placeholder validator links with the real results.

## 🔒 Security & Backups

Do not store your WSU credentials in the repository. Use environment variables or enter credentials manually when uploading via SFTP. Back up your `inf6420-projects/` folder to OneDrive and Google Drive after each milestone to protect against data loss.

## 📦 Packaging

To create a ZIP for submission, run the packaging script under `scripts/` (e.g. `scripts/package_site.ps1`) which bundles your course homepage, projects, docs, assets and scripts into a single archive. Save the ZIP in `dist/`.

## 🧶 Optional: GitHub Pages

This repo includes a `.nojekyll` file so static assets serve correctly. To publish a copy via GitHub Pages:

1. Go to *Settings → Pages* in your repository.
2. Choose `main` branch and `/ (root)` as the source.
3. Save. Your site will publish at `https://<your-username>.github.io/inf6420-projects/`.

Important: your official grading URLs remain the WSU-hosted HTTP links above.

By following this structure and workflow, you will have a clean, rubric‑compliant repository for INF 6420. Use the included scripts to audit and reorganize your files, commit and push regularly, and deploy to the WSU server for grading.


## Troubleshooting

- DOCX downloads over HTTP may be flagged by the browser ("insecure"). Choose “Keep/Keep anyway.”
- If an image or doc 404s, verify the exact filename and capitalization on the server.
- If SFTP fails, check VPN/port 22 or use WinSCP GUI.

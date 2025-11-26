INF 6420 – Projects Hub

This repository holds all your local source files for INF 6420. It mirrors the structure you must maintain on the WSU server, but it does not replace that server; your WSU URLs remain the official grading links. Use this repo to edit, audit and package your work before uploading to WSU.

🌐 Live WSU URLs

Once uploaded, your pages should be accessible at:

Course home (Project 1): http://141.217.120.86/fn9575/html/rock-INF6420-index.html

Project 2.1 (DOCX): http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx

Project 2.2 (HTML): http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html

Project 3 (Squirrels): http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html

Project 4 (Responsive): http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html

Replace any old links in your pages with these WSU paths. Do not link to folders like project1.1/ or rock-Project2.3/ once you’ve merged their contents.

📂 Canonical Structure

Your repository (and server) should follow this layout:

rock-INF6420-index.html        # Project 1 homepage
img/                           # Contains your photo (myphoto.jpg)
inf6420-projects/
├ rock-project2.1.docx         # Project 2.1 research paper
├ rock-project2-2.html         # Project 2.2 HTML/CSS version
├ project3/                    # Project 3 – Squirrels of Michigan
│  ├ home.html, fox.html, red.html, gray.html, flying.html
│  ├ squirrels.css
│  ├ showform.php              # Form handler (if applicable)
│  └ images/home.jpg … gray.jpg
└ project4/                    # Project 4 – Responsive redesign
   ├ home.html, fox.html, red.html, gray.html, flying.html
   ├ squirrels-responsive.css  # CSS with media queries
   └ images/home.jpg … gray.jpg
scripts/                       # Deployment and packaging scripts
docs/                          # Assignment PDFs and rubric notes
styles/, images/               # Shared assets (e.g. brand.css)
README.md
submission.html


Legacy folders (e.g. project1.1/, project2.1/, project2.2/, project3/ duplicates, rock-Project2.3/) should be removed or renamed with a -old suffix once you merge their contents.

🚧 Workflow

Edit locally: Work on your HTML/CSS/PHP files under inf6420-projects. Keep the DOCX for Project 2.1 outside of Git if .gitignore excludes *.docx.

Audit & organise: Run a Python audit script (e.g. python audit_layout.py) to check for missing or misplaced files. Use a cleanup script (e.g. python cleanup_inf6420.py) to move files into the canonical layout and archive obsolete folders.

Commit & push: When your repo passes the audit, commit and push:

git add -A
git commit -m "Restructure to canonical layout and archive old folders"
git push origin main


Deploy via SFTP: Using GlobalProtect VPN and WinSCP/OwlFiles, upload rock-INF6420-index.html, the img/ folder, and inf6420-projects/ to /home/fn9575/html/ on the WSU server. Rename old server folders like project3 to project3-old before uploading.

Validate: After deployment, check each page at the WSU URL above. Run W3C HTML and CSS validators and replace placeholder links with the real validation URLs.

🔒 Security

Do not store your WSU credentials in this repo. Enter them manually when using SFTP or store them in environment variables. Back up your inf6420-projects/ folder to OneDrive/Google Drive for redundancy.

By following this structure and workflow, you’ll have a clean, unified project tree that meets the course requirements and is easy to deploy.

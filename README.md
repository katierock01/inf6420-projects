# INF 6420 – Projects Hub

**Default repository for all assignments in INF6420 course - Web Development and Scripting**

Course site and sources for INF 6420 by Katie Rock. This repository serves as the central hub for all course projects, assignments, and web development work. This repo mirrors your student web space (WSU) but does not replace it. WSU URLs remain the source of truth for grading.

📖 **Quick Links**: [Quick Start Guide](QUICKSTART.md) | [Detailed Setup Instructions](GITHUB_PROJECT_SETUP.md)

## Course Overview

INF 6420 focuses on modern web development, scripting, and best practices for creating accessible, standards-compliant websites. This repository contains:

- **Project implementations** (HTML, CSS, JavaScript)
- **Documentation and assignment guides**
- **Deployment scripts** for WSU server
- **Shared assets and resources**
- **Automated workflows** for validation and publishing

All projects emphasize web accessibility (WCAG standards), semantic HTML, responsive design, and modern CSS techniques.

## Live WSU URLs

- Hub: http://141.217.120.86/fn9575/html/inf6420-projects/index.html
- Project 2.2: http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.2/rock-project2-2.html
- Project 1.1 (links to 2.1 DOCX): http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project1.1/rock-Project1.1.index.html
- Direct Project 2.1 DOCX (optional): http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.1/rock-project2.1.docx

Validators (for 2.2):
- HTML: https://validator.w3.org/nu/?doc=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Frock-Project2.2%2Frock-project2-2.html
- CSS:  https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Frock-Project2.2%2Frock-project2-2.html

The Project 2.2 page also includes dynamic validator links that adapt to whatever URL you open.

## Repo layout

- `index.html` – Projects hub and main landing page
- `submission.html` – Grader-friendly links and validators
- `docs/` – Assignment documentation hub and helper text
- `images/`, `styles/` – Shared assets (images, CSS, fonts)
- `scripts/` – Deployment, packaging, and automation helpers

### Project Directories

- **`rock-Project1.1/`** – Project 1.1: Introduction page with links to subsequent projects
- **`rock-Project2.1/`** – Project 2.1: Document landing page with embedded doc scaffold
- **`rock-Project2.2/`** – Project 2.2: Complete HTML page with internal CSS, accessibility features
- **`project3/`** – Project 3: Advanced web features (forms, interactivity, multiple pages)
- Additional projects follow similar naming conventions

### Project Features

Each project demonstrates specific web development skills:

1. **Semantic HTML5** markup with proper document structure
2. **CSS styling** (internal, external, or inline as specified)
3. **Accessibility features**: ARIA labels, keyboard navigation, skip links
4. **Responsive design**: Mobile-first approach, flexible layouts
5. **Standards compliance**: W3C HTML and CSS validation
6. **Cross-browser compatibility**: Testing across modern browsers

Large binaries are excluded by default; `.gitignore` includes `*.docx` and other generated files.

## GitHub Project Management

This repository uses GitHub Projects for tracking assignments and milestones.

### Setting Up GitHub Project1

To create and configure the GitHub Project for this course:

```bash
# Run the automated setup script
python scripts/setup_github_project.py
```

This script will:
1. Update the repository description
2. Create a project named "Project1" 
3. Configure it for tracking course assignments

**Manual Setup (if script fails):**
1. Go to https://github.com/katierock01/inf6420-projects/projects
2. Click "New project"
3. Name: `Project1`
4. Description: `INF6420 Course Assignments and Projects Tracking`
5. Add columns: To Do, In Progress, Review, Completed
6. Link issues to track individual assignments

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

## Development Workflow

1. **Create/Edit** files locally in your project directories
2. **Test** locally by opening HTML files in browser
3. **Validate** using W3C validators (links in submission.html)
4. **Commit** changes to Git with descriptive messages
5. **Deploy** to WSU server using deployment scripts
6. **Verify** on WSU URLs for final grading

## Learning Objectives

Through this repository and its projects, students will:

- Master HTML5 semantic markup and document structure
- Apply CSS for layout, typography, and visual design
- Implement web accessibility standards (WCAG 2.1 Level AA)
- Use version control (Git/GitHub) for project management
- Deploy websites to remote servers via SFTP
- Validate code against W3C standards
- Create responsive, mobile-friendly designs
- Follow web development best practices and conventions

## Resources

- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [WAVE Accessibility Tool](https://wave.webaim.org/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [WSU Web Space Documentation](http://141.217.120.86/)

## License

This repository contains coursework for INF 6420. All code and content are for educational purposes.

## Contact

- **Student**: Katie Rock
- **Course**: INF 6420 - Web Development and Scripting
- **Institution**: Wayne State University

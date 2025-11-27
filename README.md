# INF 6420 – Projects Hub

Course portfolio for INF 6420 (Web Development and Scripting) by Katie Rock. This repository mirrors your WSU web space for development and version control. **WSU URLs remain the grading source of truth.**

## 🌐 Live WSU URLs

- **Hub:** [http://141.217.120.86/fn9575/html/inf6420-projects/index.html](http://141.217.120.86/fn9575/html/inf6420-projects/index.html)
- **Project 1:** [http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project1/rock-Project1.index.html](http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project1/rock-Project1.index.html)
- **Project 2.2:** [http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.2/rock-project2-2.html](http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.2/rock-project2-2.html)
- **Project 3:** [http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html](http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html)
- **Project 4:** [http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html](http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html)

### Validator Links (Project 2.2)
- **HTML:** [W3C Validator](https://validator.w3.org/nu/?doc=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Frock-Project2.2%2Frock-project2-2.html)
- **CSS:** [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Frock-Project2.2%2Frock-project2-2.html)

## 📁 Repository Structure

```
index.html                     # Projects hub landing page
submission.html                # Grader-focused links and validators
docs/                          # Assignment documentation
images/                        # Shared graphics
styles/brand.css               # EmpathTech branding
rock-Project1/                 # Project 1: Course index
rock-Project2.1/               # Project 2.1: Doc scaffold
rock-Project2.2/               # Project 2.2: HTML/CSS
project3/                      # Project 3: Squirrels site
project4/                      # Project 4: Responsive redesign
scripts/                       # Deployment tools
```

## 🚀 Quick Start

1. **View locally:** Open `index.html` in your browser
2. **Edit directly:** No build tools required

## 📤 Deployment to WSU Server

**Prerequisites:** WSU VPN (GlobalProtect), SFTP access to `fn9575@141.217.120.86`

**Option A – PowerShell:**
```powershell
.\scripts\deploy.ps1
```

**Option B – Python:**
```bash
python scripts/upload_22.py
```

**Option C – AI-Powered:**
```bash
python deploy-ai.py
```
*(Automated deployment to WSU server)*

**Note:** WSU paths are case-sensitive (Linux)

## 📦 Packaging

Create submission ZIP:
```powershell
.\scripts\package_site.ps1
```
Output: `dist/inf6420-projects.zip`

## 🎨 Design & Accessibility

- **Branding:** EmpathTech green (`#115740`, `#1a6e52`, `#0d4230`)
- **Accessibility:** Semantic HTML5, skip links, WCAG focus styles, reduced-motion support
- **Validation:** All pages pass W3C HTML/CSS validators

## 🛠 Guidelines

1. Use semantic HTML5 (`<article>`, `<section>`, `<nav>`)
2. Validate before deploying (W3C tools)
3. Don't rename folders without updating `index.html` and `submission.html`
4. Track progress in `PROJECT-STATUS.md`

## 🔒 Security

- Never commit credentials
- Use environment variables or manual password entry
- Back up to OneDrive/Google Drive after milestones

## 🐛 Troubleshooting

- **Port 22 blocked?** Connect to WSU VPN or mobile hotspot
- **Case issues?** Match filenames exactly (Linux server)
- **Broken links?** Update all references in hub pages
- **Deploy fails?** Check VPN and credentials

## 📚 Resources

- Project Status: `PROJECT-STATUS.md`
- WSU URLs: `docs/SERVER-URLS.txt`

## 📬 Contact

For questions, contact your instructor.

---

© 2025 Katie Rock – INF 6420 Web Development and Scripting

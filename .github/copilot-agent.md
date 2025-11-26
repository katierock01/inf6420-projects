GitHub Agent Instructions for INF 6420 Repository
Overview

This repository should house all course work for INF 6420 under a single project tree. The aim of this agent is to audit the existing directory structure, eliminate any stray or obsolete folders, and reorganize files into the canonical layout required by the course rubric. Once the structure is corrected, the agent should commit the changes and push them to GitHub.

These instructions assume the following:

Your last name is Rock, so your course home page must be named rock-INF6420-index.html and live at the root of the project.

Your WSU access ID is fn9575, and all server URLs will use this in /home/fn9575/html/.

You wish to consolidate multiple Codespaces and repositories into one clean layout and remove any duplicate or obsolete directories.

1 Audit the current repository

Run the provided audit script to understand the existing state of the repository. This script prints a tree of files, flags missing required components, and lists any legacy folders that should be archived or removed.

# ensure you're at the repository root
python audit_layout.py


Expected key files and directories (the audit script checks for these):

rock-INF6420-index.html at the repository root.

img/ directory containing your photo.

inf6420-projects/ directory containing:

rock-project2.1.docx (Project 2.1 paper)

rock-project2-2.html (Project 2.2 HTML)

project3/ with five pages (home.html, fox.html, red.html, gray.html, flying.html), a shared CSS file (squirrels.css), an optional showform.php, and an images/ subfolder with matching JPGs.

project4/ with the same five pages, a responsive stylesheet (squirrels-responsive.css), and an images/ subfolder.

Obsolete folders such as project1.1/, project2.1/, project2.2/, project3/ (duplicate), rock-Project2.1/, rock-Project2.2/, or rock-Project2.3/ should not exist once cleanup is complete.

2 Clean up and reorganize

If the audit reports missing items or legacy folders, run the cleanup script to reorganize files. The script moves or copies files into the canonical tree and archives unused directories by appending -old to their names.

# run from the repository root
python cleanup_inf6420.py

# run audit again to confirm
python audit_layout.py


After cleanup, manually inspect any *-old folders. If they contain no needed content, you may delete them. Ensure that only the canonical structure remains.

3 Set up a dev container (recommended)

To guarantee a reproducible environment in Codespaces or VS Code Dev Containers, create a .devcontainer folder with a devcontainer.json. This file should specify:

A Python base image (mcr.microsoft.com/devcontainers/python:3.10).

NodeJS feature (optional) for scripts or tooling.

postCreateCommand to install dependencies from requirements.txt.

Extensions like ms-python.python, ms-toolsai.jupyter, and github.copilot.

Forwarded ports (e.g. 8888 for Jupyter) and runtime arguments.

Example:

{
  "name": "INF6420 Development",
  "image": "mcr.microsoft.com/devcontainers/python:3.10",
  "features": {
    "ghcr.io/devcontainers/features/node:1": { "version": "18" }
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter",
        "github.copilot"
      ]
    }
  },
  "forwardPorts": [8888],
  "runArgs": ["--init"]
}


Include a requirements.txt listing Python dependencies for your audit scripts (e.g. beautifulsoup4, lxml if you use them). Also create a .gitignore to exclude compiled files (__pycache__/, *.pyc), secrets (.env), and large binaries (*.docx).

4 Replace the README and ancillary files

Replace the current README.md with the comprehensive version provided. It must:

Describe the canonical folder structure for Projects 2.1, 2.2, 3, 4 and the final group project.

Specify that the course index file must be named rock-INF6420-index.html and stored at the root.

Outline how to run the audit and cleanup scripts.

Explain how to connect via GlobalProtect and deploy to /home/fn9575/html/ using WinSCP or OwlFiles.

Provide instructions for backup to OneDrive and Google Drive.

Warn against including credentials or linking to GitHub in the live site.

If the repository contains unrelated GitHub Actions workflows (e.g. python-publish.yml for PyPI releases), delete them. They are not relevant to this project. Consider creating a simple GitHub Action that runs your audit script on each push to ensure the structure remains correct.

5 Commit and push

After reorganizing and auditing:

Stage all changes and commit with a clear message:

git add -A
git commit -m "Standardize INF6420 project layout and add devcontainer"
git push origin <branch-name>


Optionally merge this branch into main via a pull request when ready.

Delete any extra Codespaces or branches once the work is merged.

6 Deploy to the WSU server

Connect to the WSU network via GlobalProtect (protect.wayne.edu).

Use SFTP (WinSCP or OwlFiles) to upload rock-INF6420-index.html, the img/ directory, and the inf6420-projects/ directory to /home/fn9575/html/.

Verify that the following URLs work:

http://141.217.120.86/fn9575/html/rock-INF6420-index.html

http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx

http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html

http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html

http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html

Update any placeholder validation links in your HTML files once W3C validation passes.

7 Maintain a single source of truth

The repository described here becomes the only authoritative source for your INF 6420 coursework. Do not split projects across multiple repositories or codespaces. Instead, use branches if you need to experiment and merge them back into the main repository once validated. Remove or archive any duplicate or outdated copies of the repository to avoid confusion.

8 Security and privacy

Never store your WSU password or credentials in the repository. Use environment variables or enter credentials manually when uploading via SFTP.

Keep AI prompts and generated code files in a prompts/ folder if your instructor requests them. These should not contain personal information.

Conclusion

Following these steps will ensure that your repository meets the course rubric, is easy to maintain, and can be deployed without errors. Use the provided scripts to automate audits and cleanup, commit your changes regularly, and maintain backups. Once everything is merged and validated, you will have a well-organized codebase ready for grading and further development.

🛠 Additional setup and scripts

Create a .devcontainer directory and add a devcontainer.json (see the agent guide).

Add a requirements.txt listing Python packages you need (e.g. beautifulsoup4, lxml).

Add a .gitignore to exclude compiled files, secrets, and OS-specific files (the agent guide mentions suggested patterns).

Place audit_layout.py and cleanup_inf6420.py in your repo. Use them to audit and reorganise the project structure.

Run python audit_layout.py to print your folder tree and report missing/obsolete files.

Run python cleanup_inf6420.py once to move everything into the correct places and rename legacy folders. Then rerun the audit script to confirm.

🔒 Security reminder

Never commit your WSU credentials (username/password) to the repo. Use environment variables or enter credentials manually when uploading via SFTP. The agent guide includes more detailed guidance on how to keep credentials safe.

Next steps

Download both files from the links above.

Replace your existing README.md and add github-agent.md.

Create your devcontainer and scripts as described.

Run the cleanup script once and the audit script until no issues remain.

Commit and push all changes in your main Codespace.

Deploy via GlobalProtect/SFTP to http://141.217.120.86/fn9575/html/.

By following this plan, you’ll have a clear, unified repository, an explicit deployment guide for your site, and automated checks to ensure everything stays tidy and rubric‑compliant.

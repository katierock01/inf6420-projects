# INF6420 Projects - AI Coding Agent Instructions

## Overview
This repository contains a portfolio of web development projects for the INF6420 course. It's a static site with HTML, CSS, and minimal PHP for form handling. The site is deployed to a WSU server via SFTP.

## Architecture
- **Hub Structure**: `index.html` serves as the main navigation hub with project cards.
- **Project Organization**: Projects in subfolders (e.g., `project3/`, `rock-Project2.1/`).
- **Shared Assets**: `styles/brand.css` for EmpathTech branding, `images/` for common graphics.
- **No Backend**: Static files; PHP only for simple form echo (server-side processing).

Key files: `index.html` (hub), `styles/brand.css` (shared styles), `scripts/deploy.ps1` (deployment).

## Key Patterns
- **Branding**: Use EmpathTech palette (`--primary-accent: #083B55`, `--link-hover: #FF6B63`). Override in `:root` as in `index.html`.
- **Accessibility**: Include `focus-visible` outlines, `@media (prefers-reduced-motion: reduce)`, semantic landmarks.
- **CSS Structure**: Variables in `:root`, internal CSS for self-contained projects (e.g., `project2.2/rock-project2-2.html`), external for multi-page (e.g., `project3/squirrels.css`).
- **Forms**: Submit to `showform.php` for simple data display; no storage.
- **Navigation**: Consistent topbar with logo and nav links.

## Workflows
- **Deployment**: Run `scripts/deploy.ps1` (PowerShell) or `scripts/upload_22.py` (Python) to SFTP upload to WSU server. Requires VPN if port 22 blocked.
- **Packaging**: `scripts/package_site.ps1` creates `dist/` ZIP for submission.
- **Validation**: Include W3C validator links in pages (e.g., `project2.2/rock-project2-2.html` has dynamic links).
- **No Builds**: Edit HTML/CSS directly; no compilers or frameworks.

## Conventions
- **File Naming**: `rock-` prefix for deliverables (e.g., `rock-project2-2.html`).
- **Color Usage**: Navy blues for primary, coral for accents; avoid pure black text.
- **Typography**: Serif for headings (`--font-serif`), sans for body (`--font-sans`).
- **Images**: SVG icons in `images/`, photos in project folders.
- **Links**: External links open in new tab with `rel="noopener"`.

## Integration Points
- **PHP Forms**: Simple POST handling in `showform.php`; outputs form data in table.
- **Server URLs**: Live at `http://141.217.120.86/fn9575/html/inf6420-projects/`.
- **GitHub Pages**: Optional static hosting; includes `.nojekyll` for assets.

Reference: `README.md` for URLs and setup; `styles/brand.css` for design tokens.
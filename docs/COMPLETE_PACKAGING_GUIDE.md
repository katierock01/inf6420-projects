# INF 6420 – Complete Project Packaging & Submission Guide

> **Master Document Version**: 1.0  
> **Purpose**: Comprehensive guide to packaging all project requirements, structure, and submission workflow  
> **Audience**: INF 6420 students preparing projects for submission

---

## ?? Document Overview

This is the **main integration guide** that brings together all project requirements, structure, and deployment information. Use this as your primary reference, with detailed guides available in supporting documents:

| Document | Purpose | Key Content |
|----------|---------|------------|
| **PROJECT_REQUIREMENTS.md** | Detailed rubrics | All project requirements, rubric points, accessibility standards |
| **DIRECTORY_STRUCTURE.md** | File organization | Canonical layout, file naming, migration guide |
| **FILE_INVENTORY.md** | Tracking template | Status tracking, validation checklist, deployment verification |
| **AUTOMATION_GUIDE.md** | Deployment tools | PowerShell scripts, Python utilities, SFTP instructions |
| **README.md** | Repository overview | Setup, URLs, workflows |

---

## Table of Contents

1. [Quick Start (5 Minutes)](#quick-start-5-minutes)
2. [Project Overview](#project-overview)
3. [Complete Workflow](#complete-workflow)
4. [Project Details & Requirements](#project-details--requirements)
5. [Quality Assurance](#quality-assurance)
6. [Deployment & Submission](#deployment--submission)
7. [FAQs & Troubleshooting](#faqs--troubleshooting)

---

## Quick Start (5 Minutes)

### For First-Time Setup

1. **Clone/open the repository**
   ```bash
   cd C:\Users\k8roc\source\repos\inf6420-projects
   ```

2. **Review project requirements**
   - Open: `docs/PROJECT_REQUIREMENTS.md`
   - Skim relevant project sections

3. **Check directory structure**
   - Verify layout matches: `docs/DIRECTORY_STRUCTURE.md`
   - Files should be in canonical locations

4. **Create your first project**
   - Copy template from PROJECT_REQUIREMENTS.md
   - Save in correct folder (see DIRECTORY_STRUCTURE.md)

5. **Validate and deploy**
   - Run: `.\scripts\validate_all.ps1`
   - Deploy: `.\scripts\deploy.ps1` (requires VPN)

### For Ongoing Development

```powershell
# Daily workflow
1. cd C:\Users\k8roc\source\repos\inf6420-projects
2. # Edit files in correct project folder
3. git add -A
4. git commit -m "Update project X"
5. git push origin inf6420-project

# Before submission
1. .\scripts\validate_all.ps1         # Check for errors
2. .\scripts\package_site.ps1        # Create backup ZIP
3. .\scripts\deploy.ps1              # Upload to server (VPN required)
4. # Test live URLs in browser
5. # Mark as submitted in FILE_INVENTORY.md
```

---

## Project Overview

### All INF 6420 Projects at a Glance

```
???????????????????????????????????????????????????????????????????
? INF 6420 – Complete Portfolio (5 Projects)                      ?
???????????????????????????????????????????????????????????????????

?? PROJECT 1: Course Homepage (50 points)
   File: rock-INF6420-index.html (root)
   Type: HTML/CSS
   Link: http://141.217.120.86/fn9575/html/rock-INF6420-index.html
   Required: Student photo, project links, navigation

?? PROJECT 2.1: Research Paper (100 points)
   File: rock-project2.1.docx
   Type: DOCX Document
   Link: http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx
   Required: 5-7 pages, 5+ sources, citations, professional formatting

?? PROJECT 2.2: HTML/CSS Implementation (100 points)
   File: rock-project2-2.html
   Type: HTML/CSS
   Link: http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html
   Required: 500+ words, based on 2.1 topic, responsive design

?? PROJECT 3: Multi-Page Site (150 points)
   Files: project3/{home,fox,red,gray,flying}.html + images + CSS
   Type: HTML/CSS/PHP
   Link: http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html
   Required: 5 pages, navigation, 300+ words per page, images

?? PROJECT 4: Responsive Redesign (150 points)
   Files: project4/{home,fox,red,gray,flying}.html + images + CSS
   Type: HTML/CSS/PHP (Mobile-first responsive)
   Link: http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html
   Required: Mobile/tablet/desktop layouts, hamburger menu, optimized

TOTAL: 550 points available
```

### Grading Breakdown

| Project | Points | Component | Rubric Link |
|---------|--------|-----------|-------------|
| 1 | 50 | Homepage design | See PROJECT_REQUIREMENTS.md § Project 1 |
| 2.1 | 100 | Research quality | See PROJECT_REQUIREMENTS.md § Project 2.1 |
| 2.2 | 100 | HTML/CSS implementation | See PROJECT_REQUIREMENTS.md § Project 2.2 |
| 3 | 150 | Multi-page site | See PROJECT_REQUIREMENTS.md § Project 3 |
| 4 | 150 | Responsive design | See PROJECT_REQUIREMENTS.md § Project 4 |

---

## Complete Workflow

### Phase 1: Setup & Planning (Week 1)

```
?? Read all requirements ??????????????????????
? 1. Open docs/PROJECT_REQUIREMENTS.md        ?
? 2. Review your project assignment          ?
? 3. Check grading rubric for your project   ?
? 4. Note any dependencies (e.g., 2.2 ? 2.1) ?
??????????????????????????????????????????????
           ?
?? Verify directory structure ?????????????????
? 1. Open docs/DIRECTORY_STRUCTURE.md         ?
? 2. Create required folders                  ?
? 3. Verify canonical layout                  ?
? 4. Organize any existing files              ?
??????????????????????????????????????????????
           ?
?? Create tracking sheet ??????????????????????
? 1. Copy docs/FILE_INVENTORY.md template     ?
? 2. Fill in project-specific info           ?
? 3. Update status as you progress           ?
? 4. Track validation results                ?
??????????????????????????????????????????????
```

### Phase 2: Development (Weeks 2-8)

#### For Each Project:

```
?? Develop locally ???????????????????????????
? 1. Create HTML/CSS/PHP files               ?
? 2. Test in browser (Chrome, Firefox, Edge) ?
? 3. Test on mobile device/emulator          ?
? 4. Follow accessibility guidelines         ?
? 5. Use semantic HTML5 elements             ?
? 6. Implement responsive design (if needed) ?
? 7. Optimize images (< 500KB each)          ?
??????????????????????????????????????????????
           ?
?? Commit to Git ?????????????????????????????
? git add -A                                 ?
? git commit -m "Descriptive message"        ?
? git push origin inf6420-project            ?
??????????????????????????????????????????????
           ?
?? Track progress ????????????????????????????
? 1. Update FILE_INVENTORY.md status         ?
? 2. Check off completed features            ?
? 3. Note any issues or blockers             ?
??????????????????????????????????????????????
```

### Phase 3: Quality Assurance (Week 9)

```
?? Validate code ?????????????????????????????
? 1. Run: .\scripts\validate_all.ps1         ?
? 2. Check for HTML/CSS errors               ?
? 3. Fix validation issues                   ?
? 4. Re-run validation until clean           ?
??????????????????????????????????????????????
           ?
?? Accessibility audit ???????????????????????
? 1. Run Lighthouse in Chrome DevTools       ?
? 2. Check keyboard navigation               ?
? 3. Verify color contrast (WCAG AA)         ?
? 4. Test with screen reader (optional)      ?
? 5. Fix any accessibility issues            ?
??????????????????????????????????????????????
           ?
?? Cross-browser testing ?????????????????????
? 1. Test in Chrome                          ?
? 2. Test in Firefox                         ?
? 3. Test in Safari (if available)           ?
? 4. Test in Edge                            ?
? 5. Test on mobile (320px-1200px width)    ?
? 6. Fix any browser-specific issues         ?
??????????????????????????????????????????????
```

### Phase 4: Deployment (Week 10)

```
?? Create backup ?????????????????????????????
? 1. Run: .\scripts\package_site.ps1         ?
? 2. Save ZIP to safe location               ?
? 3. Upload to OneDrive/Google Drive         ?
??????????????????????????????????????????????
           ?
?? Deploy to server ??????????????????????????
? 1. Connect to WSU VPN (GlobalProtect)      ?
? 2. Run: .\scripts\deploy.ps1               ?
? 3. Monitor upload progress                 ?
? 4. Verify upload completion                ?
??????????????????????????????????????????????
           ?
?? Test on live server ???????????????????????
? 1. Open Project 1 URL                      ?
? 2. Test all project links                  ?
? 3. Verify images display                   ?
? 4. Test forms (if applicable)              ?
? 5. Check mobile responsiveness             ?
? 6. Document any issues                     ?
??????????????????????????????????????????????
           ?
?? Submit for grading ????????????????????????
? 1. Verify all URLs accessible              ?
? 2. Provide link to instructor              ?
? 3. Note any known issues                   ?
? 4. Update submission date in FILE_INVENTORY?
? 5. Commit final changes to Git             ?
??????????????????????????????????????????????
```

---

## Project Details & Requirements

### Summary Table

| Project | Type | Points | Duration | Key Requirement |
|---------|------|--------|----------|-----------------|
| 1 | Web | 50 | 1-2 weeks | Responsive homepage |
| 2.1 | Research | 100 | 2-3 weeks | 5-7 pages, 5+ sources |
| 2.2 | Web | 100 | 2-3 weeks | 500+ words, implementation |
| 3 | Web | 150 | 3-4 weeks | 5-page site with navigation |
| 4 | Web | 150 | 4-5 weeks | Mobile-first responsive design |

### Project 1: Course Homepage

**Quick Reference**:
- **File**: `rock-INF6420-index.html` (at root level)
- **Points**: 50
- **Rubric**: Content (10) + HTML (10) + CSS (10) + Navigation (10) + Responsive (10)
- **Key Elements**: Student photo, project links, contact info, professional design

**Delivery Checklist**:
- [ ] Student name and photo visible
- [ ] Links to all 4 projects (2.1, 2.2, 3, 4)
- [ ] Professional CSS styling with brand colors
- [ ] Mobile-responsive layout
- [ ] Valid HTML5
- [ ] Valid CSS3
- [ ] Keyboard accessible navigation
- [ ] HTML validates without errors
- [ ] CSS validates without errors

**References**: See PROJECT_REQUIREMENTS.md § Project 1

---

### Project 2.1: Research Paper

**Quick Reference**:
- **File**: `rock-project2.1.docx`
- **Points**: 100
- **Rubric**: Topic (15) + Research (20) + Organization (15) + Writing (15) + Analysis (15) + Formatting (10) + References (10)
- **Requirements**: 5-7 pages, minimum 5 credible sources, proper citations

**Delivery Checklist**:
- [ ] 5-7 pages of content (single-spaced) or 8-10 (double-spaced)
- [ ] Clear thesis statement
- [ ] Minimum 5 credible sources
- [ ] Proper citations (APA/MLA/Chicago style)
- [ ] Bibliography page
- [ ] Professional formatting (title page, headers, footers)
- [ ] Spell-checked and proofread
- [ ] Topic related to web design/accessibility/performance

**Research Topics**: Responsive design, accessibility (WCAG), CSS Grid vs Flexbox, mobile-first design, web performance, web security, UX research, typography trends

**References**: See PROJECT_REQUIREMENTS.md § Project 2.1

---

### Project 2.2: HTML/CSS Implementation

**Quick Reference**:
- **File**: `rock-project2-2.html`
- **Points**: 100
- **Rubric**: Content (15) + HTML (15) + CSS (20) + Responsive (15) + Layout (15) + Validation (10) + Accessibility (10)
- **Requirements**: 500+ words, based on 2.1 topic, responsive design, all CSS internal or external (NO inline)

**Delivery Checklist**:
- [ ] Minimum 500 words of content (from 2.1 topic)
- [ ] Semantic HTML5 (header, main, section, article, footer)
- [ ] No inline styles (all CSS in <style> block or external file)
- [ ] CSS variables for theming
- [ ] Professional color scheme (3+ colors)
- [ ] At least one image with alt text
- [ ] Mobile-responsive layout
- [ ] Tested on 320px, 768px, 1200px widths
- [ ] HTML validates
- [ ] CSS validates
- [ ] Keyboard accessible
- [ ] Proper heading hierarchy

**CSS Requirements**:
```css
/* Use CSS variables */
:root {
    --primary-color: #083B55;
    --accent-color: #FF6B63;
}

/* Media queries for responsive */
@media (max-width: 768px) {
    /* Mobile styles */
}

@media (min-width: 769px) {
    /* Tablet/desktop styles */
}
```

**References**: See PROJECT_REQUIREMENTS.md § Project 2.2

---

### Project 3: Multi-Page Site

**Quick Reference**:
- **Files**: `project3/{home,fox,red,gray,flying}.html` + `squirrels.css` + `images/` (5 JPGs)
- **Points**: 150
- **Rubric**: Content (25) + HTML (20) + CSS (25) + Navigation (15) + Images (15) + Responsive (20) + Validation (15) + Accessibility (10) + Form (10)
- **Requirements**: 5 pages, 300+ words each, consistent navigation, responsive design

**File Structure**:
```
inf6420-projects/project3/
??? home.html
??? fox.html
??? red.html
??? gray.html
??? flying.html
??? squirrels.css (external, shared)
??? showform.php (optional)
??? images/
    ??? home.jpg
    ??? fox.jpg
    ??? red.jpg
    ??? gray.jpg
    ??? flying.jpg
```

**Delivery Checklist**:
- [ ] All 5 HTML pages present and accessible
- [ ] Navigation bar on every page (consistent)
- [ ] Current page highlighted/active in navigation
- [ ] Minimum 300 words per page
- [ ] Minimum one image per page
- [ ] External CSS file (squirrels.css)
- [ ] No inline styles
- [ ] Responsive design (tested on mobile/tablet/desktop)
- [ ] Valid HTML5 on all pages
- [ ] Valid CSS3
- [ ] All links functional
- [ ] All images load correctly
- [ ] Alt text on all images
- [ ] Form working (if included with showform.php)

**References**: See PROJECT_REQUIREMENTS.md § Project 3

---

### Project 4: Responsive Redesign

**Quick Reference**:
- **Files**: `project4/{home,fox,red,gray,flying}.html` + `squirrels-responsive.css` + `images/` (5 optimized JPGs)
- **Points**: 150
- **Rubric**: Mobile (25) + Tablet (20) + Desktop (20) + Responsive (25) + Navigation (15) + CSS (10) + Performance (10) + Accessibility (15) + Validation (10) + Polish (15)
- **Key Improvement**: Mobile-first approach, hamburger menu, optimized images, media queries

**Responsive Breakpoints**:
```css
/* Mobile-first: Start with mobile styles */
body { font-size: 16px; }

/* Tablet: 600px and up */
@media (min-width: 600px) {
    body { font-size: 17px; }
}

/* Desktop: 1200px and up */
@media (min-width: 1200px) {
    body { font-size: 18px; max-width: 1200px; }
}
```

**Hamburger Menu** (Mobile Navigation):
- Three horizontal lines (?) on mobile
- Click to toggle menu open/close
- Hidden on tablet/desktop (show full nav instead)
- Smooth animations
- Clear "X" to close

**Delivery Checklist**:
- [ ] CSS file named `squirrels-responsive.css` (not squirrels.css)
- [ ] Mobile-first approach implemented
- [ ] Mobile layout (< 600px): single column, hamburger menu
- [ ] Tablet layout (600-1024px): multi-column, full nav
- [ ] Desktop layout (> 1024px): optimized spacing
- [ ] Hamburger menu functional on mobile
- [ ] Full navigation on tablet/desktop
- [ ] Touch-friendly buttons (44x44px minimum)
- [ ] Readable text on mobile (16px minimum)
- [ ] Images optimized for different viewports
- [ ] Tested on multiple device sizes
- [ ] Valid HTML5
- [ ] Valid CSS3
- [ ] Lighthouse score 80+
- [ ] Accessibility audit passed

**References**: See PROJECT_REQUIREMENTS.md § Project 4

---

## Quality Assurance

### Pre-Submission Validation

#### 1. HTML Validation

```powershell
# Automated validation
.\scripts\validate_all.ps1

# Manual validation
# https://validator.w3.org/ (paste HTML or upload file)
```

**Common HTML Issues**:
- Unclosed tags ? Add closing tag
- Invalid attributes ? Check attribute names
- Duplicate IDs ? Use unique IDs or classes instead
- Bad charset ? Use `<meta charset="UTF-8">`
- Improper nesting ? Reorder elements

**Fix Strategy**:
1. Run validator
2. Note all errors
3. Edit HTML to fix errors
4. Re-run validator
5. Repeat until no errors

#### 2. CSS Validation

```powershell
# Automated validation
.\scripts\validate_all.ps1

# Manual validation
# https://jigsaw.w3.org/css-validator/
```

**Common CSS Issues**:
- Unknown properties ? Remove or correct
- Invalid values ? Check CSS syntax
- Missing semicolons ? Add `;` after each property
- Syntax errors ? Check brackets, quotes

#### 3. Accessibility Audit

```powershell
# Run Lighthouse
# Chrome DevTools (F12) ? Lighthouse ? Analyze

# Check for:
? Performance score 75+
? Accessibility score 85+
? Best Practices score 80+
? SEO score 80+
```

**Manual Accessibility Checks**:
- [ ] Keyboard navigation (Tab through all elements)
- [ ] Heading hierarchy (h1 ? h2 ? h3, no skips)
- [ ] Color contrast 4.5:1 for text (WebAIM checker)
- [ ] Alt text on all images
- [ ] Form labels associated with inputs
- [ ] Focus visible states on all interactive elements
- [ ] No auto-playing media
- [ ] Respects prefers-reduced-motion

#### 4. Cross-Browser Testing

Test in all major browsers:

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome | ?/? | DevTools: F12 |
| Firefox | ?/? | Similar to Chrome |
| Safari | ?/? | If available |
| Edge | ?/? | Modern Chromium-based |

**Test at Multiple Viewports**:
- Mobile: 320px-480px
- Tablet: 768px-1024px
- Desktop: 1200px+

#### 5. Link & Image Verification

```powershell
# Check all links work
# Manual: Click every link
# Automated: Use browser extension or script

# Check all images load
# DevTools Network tab: Any red X = broken image
```

---

## Deployment & Submission

### Step-by-Step Deployment

#### Step 1: Connect to WSU VPN

1. **Install GlobalProtect VPN**
   - WSU: https://technology.wsu.edu/vpn/
   
2. **Connect to VPN**
   - Open GlobalProtect client
   - Portal: vpn.wsu.edu
   - Enter WSU credentials
   - Wait for "Connected" status

#### Step 2: Create Backup

```powershell
# Create ZIP package before deployment
.\scripts\package_site.ps1

# Output: dist\inf6420-projects-2024-01-15.zip
# Save to OneDrive/Google Drive for safety
```

#### Step 3: Run Validation

```powershell
# Final quality check
.\scripts\validate_all.ps1

# If errors:
#   1. Fix errors in source files
#   2. Commit changes to Git
#   3. Re-run validation
#   4. Proceed only after all clear
```

#### Step 4: Deploy to Server

```powershell
# Navigate to project root
cd C:\Users\k8roc\source\repos\inf6420-projects

# Run deployment script
.\scripts\deploy.ps1

# Monitor output for:
# ? VPN Connected
# ? Files prepared
# ? Connected to sftp.wsu.edu
# ? Uploading files...
# ? Deployment complete
```

#### Step 5: Verify on Live Server

1. **Open Project 1 homepage**
   - URL: http://141.217.120.86/fn9575/html/rock-INF6420-index.html

2. **Test all project links**
   - Click each project link
   - Verify content displays

3. **Check images**
   - All images should be visible
   - No broken image icons (X)

4. **Test responsiveness**
   - Open DevTools (F12)
   - Toggle Device Toolbar (Ctrl+Shift+M)
   - Test at 320px, 768px, 1200px widths

5. **Test forms** (if applicable)
   - Fill out form
   - Submit
   - Verify success message

### Submission Information

**Required Information for Grading**:
- [ ] Project 1 URL: http://141.217.120.86/fn9575/html/rock-INF6420-index.html
- [ ] GitHub repository link: https://github.com/katierock01/inf6420-projects
- [ ] Submission date: ___________
- [ ] Known issues or notes: ___________

**Submit By**:
1. Provide live URLs in assignment submission
2. Push final code to GitHub
3. Update FILE_INVENTORY.md with submission date
4. Email instructor with summary (if requested)

---

## FAQs & Troubleshooting

### General Questions

#### Q: Which project should I start with?
**A**: Follow this order:
1. Project 1 (homepage) – Quick reference for other projects
2. Project 2.1 (research) – Topic choice for 2.2
3. Project 2.2 (HTML/CSS) – Implementation of 2.1
4. Project 3 (multi-page) – Base site
5. Project 4 (responsive) – Enhanced version of 3

#### Q: Can I use CSS frameworks (Bootstrap, Tailwind)?
**A**: No. Use pure CSS only. Frameworks are prohibited to ensure you learn fundamental CSS skills.

#### Q: How do I test mobile responsiveness?
**A**: Three options:
1. **Chrome DevTools** (F12): Toggle Device Toolbar (Ctrl+Shift+M)
2. **Actual device**: Upload to server and open on phone/tablet
3. **Online emulator**: BrowserStack (paid) or similar

#### Q: Do I need to test in all browsers?
**A**: Yes. Minimum: Chrome, Firefox, and Edge. Safari preferred if available.

#### Q: My images are too large. How do I optimize?
**A**: Use online tools:
- TinyJPG (https://tinyjpg.com/) - Compress JPEGs
- ImageOptim - Batch compression
- Resize images to 1200px width maximum

### Deployment Issues

#### Q: "Connection refused" when deploying
**A**: 
- Verify WSU VPN connected (check GlobalProtect status)
- Try manual upload via WinSCP
- Contact WSU IT if port 22 blocked

#### Q: "Authentication failed" during upload
**A**: 
- Verify WSU username/password correct
- Reset password at https://password.wsu.edu/
- Contact WSU IT for account issues

#### Q: Files uploaded but not visible on live server
**A**: 
- Wait 5 minutes (caching)
- Clear browser cache (Ctrl+Shift+Delete)
- Check file location on server with WinSCP
- Verify file permissions (should be readable)

#### Q: Images showing as broken on live server
**A**: 
- Check image file paths (relative, not absolute)
- Verify images uploaded to correct folder
- Check filename spelling and capitalization
- Images should be in `/project3/images/` and `/project4/images/`

### Code Issues

#### Q: HTML validation error: "Unclosed tag"
**A**: Add closing tag. Example:
```html
<!-- Wrong -->
<div>Content

<!-- Correct -->
<div>Content</div>
```

#### Q: CSS not applying to elements
**A**: 
- Check selector specificity
- Verify CSS file linked (for external CSS)
- Check for typos in class/ID names
- Ensure CSS comes before closing `</body>`

#### Q: Mobile menu not working
**A**: 
- Verify JavaScript if used (syntax errors)
- Check CSS media query breakpoint (default: 600px)
- Test in Chrome DevTools Device Mode
- Verify button click handler works

#### Q: Form not submitting
**A**: 
- Verify form method is POST (not GET)
- Check form action points to `showform.php`
- Verify input names are correct
- Test locally before deploying

### Accessibility Issues

#### Q: How do I check color contrast?
**A**: Use WebAIM Contrast Checker:
- https://webaim.org/resources/contrastchecker/
- Minimum 4.5:1 for normal text (WCAG AA)
- Minimum 3:1 for large text

#### Q: How do I test keyboard navigation?
**A**: 
- Press Tab to move between elements
- Press Shift+Tab to move backward
- Press Enter to activate buttons/links
- Should be able to access all interactive elements

#### Q: How do I add alt text to images?
**A**: 
```html
<!-- Descriptive alt text -->
<img src="image.jpg" alt="Red squirrel sitting on branch">

<!-- Don't use: "image of...", "picture", etc. -->
```

---

## Additional Resources

### ?? Documentation Links

**Within This Repository**:
- `PROJECT_REQUIREMENTS.md` – Complete rubrics and requirements
- `DIRECTORY_STRUCTURE.md` – File organization guide
- `FILE_INVENTORY.md` – Status tracking template
- `AUTOMATION_GUIDE.md` – Deployment scripts documentation
- `README.md` – Repository overview

**External Resources**:
- [MDN Web Docs](https://developer.mozilla.org/) – HTML/CSS reference
- [W3C Validators](https://validator.w3.org/) – Code validation
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) – Accessibility standards
- [CSS Tricks](https://css-tricks.com/) – CSS tutorials and techniques

### ??? Tools & Software

**Validators**:
- W3C HTML Validator: https://validator.w3.org/
- W3C CSS Validator: https://jigsaw.w3.org/css-validator/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/

**Design & Image Tools**:
- TinyJPG: https://tinyjpg.com/ (image compression)
- Color Hunt: https://colorhunt.co/ (color palettes)
- Google Fonts: https://fonts.google.com/ (web fonts)

**Deployment Tools**:
- WinSCP: https://winscp.net/ (SFTP GUI)
- GlobalProtect: https://technology.wsu.edu/vpn/ (WSU VPN)
- Chrome DevTools: F12 in Chrome (testing/debugging)

**Development Environment**:
- Visual Studio Code: https://code.visualstudio.com/
- Sublime Text: https://www.sublimetext.com/
- Notepad++: https://notepad-plus-plus.org/

### ?? Support

**For Questions**:
- **Course Instructor**: Canvas message or email
- **WSU IT Support**: https://technology.wsu.edu/
- **GitHub Issues**: Create issue in repository

---

## Conclusion

This complete packaging guide covers all aspects of the INF 6420 project portfolio:

? **Requirements** – Know what's expected (PROJECT_REQUIREMENTS.md)  
? **Structure** – Organize files correctly (DIRECTORY_STRUCTURE.md)  
? **Tracking** – Monitor progress (FILE_INVENTORY.md)  
? **Automation** – Deploy efficiently (AUTOMATION_GUIDE.md)  
? **Workflow** – Follow best practices (this document)

**Next Steps**:

1. **Read the full requirements** – Open PROJECT_REQUIREMENTS.md and review your project
2. **Setup directory structure** – Follow DIRECTORY_STRUCTURE.md to organize files
3. **Begin development** – Start with Project 1, then move through projects sequentially
4. **Track progress** – Use FILE_INVENTORY.md to monitor status
5. **Validate early, deploy often** – Use scripts to ensure quality
6. **Submit and celebrate** – You've completed a full web development portfolio!

---

**Document End**  
**Version 1.0 | Last Updated: 2024**  
**For support or questions, contact your instructor or visit documentation links above.**

# INF 6420 Assignment Checklist

**Last Updated:** November 27, 2025

Use this checklist to verify all requirements are met for each project before submission.

---

## Project 1 - Personal Introduction Page

**File:** `rock-Project1/rock-Project1.index.html`  
**WSU URL:** http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project1/rock-Project1.index.html

### Requirements Checklist:

- [ ] **HTML Structure**
  - [ ] Valid HTML5 DOCTYPE
  - [ ] Proper `<head>` with charset, viewport, title
  - [ ] Semantic elements (header, main, footer, nav)
  - [ ] One `<h1>` per page
  
- [ ] **Content Requirements**
  - [ ] Student name clearly displayed
  - [ ] Photo included (myphoto.jpeg)
  - [ ] "About Me" section
  - [ ] "Purpose of Taking This Class" section
  - [ ] Course projects list
  - [ ] External link (Wayne State SIS website)
  - [ ] **CRITICAL: Link to Project 2.1 Word document (rock-project2.1.docx)**
  - [ ] Link to Project 2.2 HTML page
  
- [ ] **Styling**
  - [ ] Internal or external CSS
  - [ ] Readable fonts and colors
  - [ ] Professional appearance
  
- [ ] **Validation**
  - [ ] Passes W3C HTML validator
  - [ ] Link to validator result in footer
  
- [ ] **Accessibility**
  - [ ] All images have alt text
  - [ ] External links have target="_blank" and rel="noopener"
  - [ ] Semantic markup used appropriately

---

## Project 2.1 - Research Paper (Word Document)

**File:** `rock-Project2.1/rock-project2.1.docx`  
**Landing Page:** `rock-Project2.1/index.html`  
**WSU URL:** http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.1/rock-project2.1.docx

### Requirements Checklist:

- [ ] **Word Document (.docx)**
  - [ ] Properly formatted research paper
  - [ ] All required sections included
  - [ ] References/bibliography formatted correctly
  - [ ] Uploaded to WSU server
  
- [ ] **Landing Page (index.html)**
  - [ ] Provides link to DOCX download
  - [ ] Optional: Embedded HTML version in `docs/docs/rock-project2.1.html`
  - [ ] Navigation back to main projects hub
  
- [ ] **Integration**
  - [ ] **Project 1 MUST link to this DOCX file** ✅ CRITICAL
  - [ ] DOCX accessible via HTTP (not HTTPS)
  - [ ] File size reasonable for download

---

## Project 2.2 - HTML Conversion with Internal CSS

**File:** `rock-Project2.2/rock-project2-2.html`  
**WSU URL:** http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.2/rock-project2-2.html

### Requirements Checklist:

- [ ] **HTML Structure**
  - [ ] Valid HTML5 with proper structure
  - [ ] Semantic elements used throughout
  - [ ] Table(s) with proper structure (thead, tbody, th, td)
  - [ ] Lists (ul, ol) with styled items
  
- [ ] **CSS Styling (INTERNAL ONLY)**
  - [ ] All CSS in `<style>` tag within `<head>`
  - [ ] NO external stylesheets for this project
  - [ ] Styled tables with borders, padding, colors
  - [ ] Styled lists (custom bullets/numbers, spacing)
  - [ ] Typography styling (fonts, sizes, weights)
  - [ ] Color scheme applied consistently
  
- [ ] **Content**
  - [ ] Converted from Project 2.1 Word document
  - [ ] All text content preserved
  - [ ] Headings hierarchy maintained
  - [ ] References/bibliography formatted
  
- [ ] **Validation Links**
  - [ ] Dynamic HTML validator link (with actual WSU URL)
  - [ ] Dynamic CSS validator link (with actual WSU URL)
  - [ ] Links placed in footer or designated section
  
- [ ] **Validation Results**
  - [ ] Passes W3C HTML validator (0 errors)
  - [ ] Passes W3C CSS validator (0 errors)
  
- [ ] **Accessibility**
  - [ ] Table headers use `<th>` with scope attribute
  - [ ] Proper heading hierarchy (h1, h2, h3)
  - [ ] Sufficient color contrast
  - [ ] Alt text for any images
  
- [ ] **Integration**
  - [ ] **Project 1 MUST link to this page** ✅ CRITICAL
  - [ ] Navigation back to projects hub

---

## Project 3 - Multi-Page Interactive Website (Squirrels)

**Directory:** `project3/`  
**Main Page:** `project3/home.html`  
**WSU URL:** http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html

### Requirements Checklist:

- [ ] **Multi-Page Structure**
  - [ ] home.html (main landing page)
  - [ ] fox.html (Fox Squirrel page)
  - [ ] gray.html (Gray Squirrel page)
  - [ ] red.html (Red Squirrel page)
  - [ ] flying.html (Flying Squirrel page)
  - [ ] All pages linked via consistent navigation
  
- [ ] **CSS (External)**
  - [ ] Single external stylesheet: `squirrels.css`
  - [ ] All pages link to same CSS file
  - [ ] Consistent styling across all pages
  
- [ ] **Navigation**
  - [ ] Navigation menu on every page
  - [ ] Links to all other pages
  - [ ] Current page indication (optional but nice)
  - [ ] Consistent placement and styling
  
- [ ] **Images**
  - [ ] images/ subdirectory
  - [ ] One image per page (home.jpg, fox.jpg, gray.jpg, red.jpg, flying.jpg)
  - [ ] All images have descriptive alt text
  - [ ] Images sized/styled appropriately
  
- [ ] **Form (PHP)**
  - [ ] Form included on at least one page
  - [ ] Action points to showform.php
  - [ ] Form fields properly labeled
  - [ ] showform.php uploaded and functional
  
- [ ] **Content**
  - [ ] Each page has unique, relevant content
  - [ ] Information about each squirrel type
  - [ ] Proper heading structure per page
  
- [ ] **Validation**
  - [ ] All 5 HTML pages pass W3C validator
  - [ ] CSS file passes W3C CSS validator
  
- [ ] **Accessibility**
  - [ ] Semantic HTML throughout
  - [ ] Form labels associated with inputs
  - [ ] Images have alt text
  - [ ] Navigation is keyboard accessible

---

## Project 4 - Responsive Redesign

**Directory:** `project4/`  
**Main Page:** `project4/home.html`  
**WSU URL:** http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html

### Requirements Checklist:

- [ ] **Responsive CSS**
  - [ ] External stylesheet: `squirrels-responsive.css`
  - [ ] Media queries for mobile, tablet, desktop
  - [ ] Flexible layouts (flexbox or grid)
  - [ ] Mobile-first or desktop-first approach
  
- [ ] **Multi-Page Structure** (Same as Project 3)
  - [ ] home.html
  - [ ] fox.html, gray.html, red.html, flying.html
  - [ ] Consistent navigation across all pages
  
- [ ] **Responsive Features**
  - [ ] Navigation adapts to screen size (hamburger menu optional)
  - [ ] Images scale appropriately
  - [ ] Text remains readable on all devices
  - [ ] Layout adjusts (columns → stacked on mobile)
  - [ ] Touch-friendly interactive elements
  
- [ ] **Testing**
  - [ ] Tested on mobile device or emulator
  - [ ] Tested on tablet size (768px - 1024px)
  - [ ] Tested on desktop (1024px+)
  - [ ] No horizontal scrolling on mobile
  
- [ ] **Images**
  - [ ] Same images as Project 3 (can reuse)
  - [ ] images/ subdirectory
  - [ ] Optimized for web (not too large)
  
- [ ] **Validation**
  - [ ] All HTML pages pass W3C validator
  - [ ] Responsive CSS passes W3C CSS validator
  
- [ ] **Accessibility**
  - [ ] Touch targets at least 44x44px
  - [ ] Viewport meta tag included
  - [ ] Text scales appropriately
  - [ ] Color contrast maintained at all sizes

---

## General Requirements (All Projects)

### File Naming Conventions
- [ ] Use `rock-` prefix for deliverables (rock-Project1.index.html, rock-project2-2.html, rock-project2.1.docx)
- [ ] Lowercase for most filenames
- [ ] No spaces in filenames (use hyphens or underscores)

### Directory Structure
- [ ] Projects in correct folders (rock-Project1/, rock-Project2.1/, rock-Project2.2/, project3/, project4/)
- [ ] images/ subdirectories where needed
- [ ] docs/ for documentation

### WSU Server Deployment
- [ ] All files uploaded via SFTP
- [ ] Paths are case-sensitive (Linux server)
- [ ] All links work on live server
- [ ] File permissions set correctly (chmod 644 for files, 755 for directories)

### Hub Integration
- [ ] All projects linked from main index.html
- [ ] All projects linked from submission.html
- [ ] Navigation between projects works
- [ ] WSU URLs in README.md are correct

### Validation
- [ ] All HTML files pass W3C HTML validator
- [ ] All CSS files pass W3C CSS validator
- [ ] Validator links included where required
- [ ] Screenshots of validation results (if required by rubric)

### Accessibility (WCAG)
- [ ] Semantic HTML used
- [ ] Alt text on all images
- [ ] Proper heading hierarchy
- [ ] Color contrast ratio ≥ 4.5:1 for body text
- [ ] Keyboard navigation works
- [ ] Form labels properly associated
- [ ] Skip links where appropriate

### Documentation
- [ ] README.md updated with new projects
- [ ] PROJECT-STATUS.md reflects completion status
- [ ] Comments in code where helpful
- [ ] File structure clear and organized

---

## Pre-Submission Final Checks

### 1. Local Testing
- [ ] Open each HTML file in browser
- [ ] Click all navigation links
- [ ] Test all forms (if applicable)
- [ ] Check images load correctly
- [ ] Verify CSS styling applied

### 2. WSU Server Testing
- [ ] Test all WSU URLs in browser
- [ ] Verify files uploaded correctly
- [ ] Check case-sensitive paths work
- [ ] Test downloads (DOCX files)
- [ ] Verify PHP forms work (if applicable)

### 3. Validation
- [ ] Run W3C HTML validator on all pages
- [ ] Run W3C CSS validator on all stylesheets
- [ ] Fix any errors (must have 0 errors)
- [ ] Document warnings (if any)

### 4. Cross-Browser Testing
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Mobile browser

### 5. Final Integration
- [ ] All inter-project links work
- [ ] Hub pages updated (index.html, submission.html)
- [ ] Project 1 links to Project 2.1 DOCX ✅ CRITICAL
- [ ] Project 1 links to Project 2.2 HTML ✅ CRITICAL
- [ ] All WSU URLs accessible

---

## Submission Checklist

- [ ] All files uploaded to WSU server
- [ ] Submission URL tested and works
- [ ] Validator screenshots captured (if required)
- [ ] ZIP file created (if required): `dist/inf6420-projects.zip`
- [ ] Assignment submitted via course platform
- [ ] Confirmation email/receipt saved

---

**Notes:**
- Keep this checklist updated as requirements change
- Mark items complete as you work through each project
- Review rubric before marking project as "complete"
- Test on WSU server before submission deadline

© 2025 Katie Rock – INF 6420 Web Development and Scripting

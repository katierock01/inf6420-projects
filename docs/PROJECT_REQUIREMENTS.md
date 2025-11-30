# INF 6420 – Complete Project Requirements & Rubrics

> **Document Version**: 1.0  
> **Last Updated**: 2024  
> **Purpose**: Comprehensive reference for all INF 6420 project requirements, rubrics, and submission criteria

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project 1: Course Homepage](#project-1-course-homepage)
3. [Project 2.1: Research Paper](#project-21-research-paper)
4. [Project 2.2: HTML/CSS Implementation](#project-22-htmlcss-implementation)
5. [Project 3: Multi-Page Site](#project-3-multi-page-site)
6. [Project 4: Responsive Redesign](#project-4-responsive-redesign)
7. [Cross-Project Requirements](#cross-project-requirements)
8. [Accessibility Standards](#accessibility-standards)
9. [Validation Requirements](#validation-requirements)
10. [Submission Checklist](#submission-checklist)

---

## Project Overview

This course involves five progressive web development projects that build on each other:

| Project | Type | Deliverable | Status |
|---------|------|-------------|--------|
| **Project 1** | Web Design | HTML/CSS Homepage | Portfolio entry point |
| **Project 2.1** | Research | DOCX Paper | Topic analysis |
| **Project 2.2** | Implementation | HTML/CSS | Design implementation |
| **Project 3** | Multi-page | HTML/CSS/PHP | Full site development |
| **Project 4** | Responsive | HTML/CSS/PHP | Mobile-first redesign |

---

## Project 1: Course Homepage

### ?? Requirements

**Filename**: `rock-INF6420-index.html`  
**Location**: Root directory  
**Serve URL**: `http://141.217.120.86/fn9575/html/rock-INF6420-index.html`

#### Content Requirements
- [ ] Student name and photo
- [ ] Course title (INF 6420)
- [ ] Semester/year information
- [ ] Links to all projects (2.1, 2.2, 3, 4)
- [ ] Brief description of each project
- [ ] Contact information (email/phone)
- [ ] Professional appearance

#### Technical Requirements
- [ ] Valid HTML5
- [ ] CSS styling (internal or linked)
- [ ] Responsive design (mobile-friendly)
- [ ] Semantic HTML elements
- [ ] Accessible navigation
- [ ] No deprecated elements

#### Branding & Style
- [ ] Use EmpathTech palette colors
- [ ] Consistent typography (serif headings, sans-serif body)
- [ ] Professional color scheme (navy + coral accents)
- [ ] Logo or branding element
- [ ] Consistent spacing/margins

#### Navigation
- [ ] Clear project links
- [ ] Links open in current window (not new tab)
- [ ] Breadcrumb or home indicator when returning from projects
- [ ] Keyboard accessible
- [ ] Focus-visible states

### ?? Rubric Criteria (50 points total)

| Criteria | Points | Notes |
|----------|--------|-------|
| Content & Organization | 10 | All required elements present |
| HTML Structure | 10 | Valid HTML5, semantic markup |
| CSS Styling | 10 | Consistent, professional appearance |
| Navigation & Usability | 10 | Clear, accessible, functional |
| Responsive Design | 10 | Works on mobile, tablet, desktop |

### ?? Example Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INF 6420 Projects - [Your Name]</title>
    <link rel="stylesheet" href="styles/brand.css">
    <style>
        /* Project-specific styles */
    </style>
</head>
<body>
    <header>
        <h1>INF 6420 Course Projects</h1>
        <p>Student: [Your Name]</p>
    </header>
    <main>
        <section>
            <h2>Projects</h2>
            <article>
                <h3>Project 2.1: Research Paper</h3>
                <p>Description...</p>
                <a href="inf6420-projects/rock-project2.1.docx">View Paper</a>
            </article>
            <!-- More projects -->
        </section>
    </main>
</body>
</html>
```

---

## Project 2.1: Research Paper

### ?? Requirements

**Filename**: `rock-project2.1.docx`  
**Location**: `inf6420-projects/rock-project2.1.docx`  
**Serve URL**: `http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx`

#### Content Requirements
- [ ] Topic selection (web design, accessibility, performance, or technology trends)
- [ ] 5-7 pages of content (single-spaced) or 8-10 pages (double-spaced)
- [ ] Minimum 5 credible sources
- [ ] Properly cited references (APA, MLA, or Chicago style)
- [ ] Introduction with thesis statement
- [ ] Body paragraphs with supporting evidence
- [ ] Conclusion with summary and implications
- [ ] Professional formatting

#### Research Requirements
- [ ] Peer-reviewed sources (journals, conferences)
- [ ] Recent publications (within 5 years preferred)
- [ ] Reputable websites and documentation
- [ ] Proper attribution and citations
- [ ] No plagiarism

#### Documentation
- [ ] Title page with student name
- [ ] Table of contents (if applicable)
- [ ] Page numbers
- [ ] Header/footer with document title
- [ ] Bibliography/References page

### ?? Rubric Criteria (100 points total)

| Criteria | Points | Notes |
|----------|--------|-------|
| Topic & Thesis | 15 | Clear, focused, appropriate for INF 6420 |
| Research Quality | 20 | Credible sources, proper citation |
| Organization | 15 | Logical flow, clear structure |
| Writing Quality | 15 | Grammar, clarity, professional tone |
| Analysis & Depth | 15 | Critical thinking, evidence-based arguments |
| Formatting | 10 | APA/MLA/Chicago style, consistency |
| References | 10 | Minimum 5 sources, properly formatted |

#### Research Topic Ideas
- Responsive web design trends
- Accessibility (WCAG 2.1 standards)
- Web performance optimization
- CSS Grid vs Flexbox
- Mobile-first design philosophy
- Web security best practices
- User experience research methods
- Web typography trends

---

## Project 2.2: HTML/CSS Implementation

### ?? Requirements

**Filename**: `rock-project2-2.html`  
**Location**: `inf6420-projects/rock-project2-2.html`  
**Serve URL**: `http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html`

#### Content Requirements
- [ ] Static HTML page on researched topic (from Project 2.1)
- [ ] Minimum 500 words of content
- [ ] Well-organized sections (intro, body, conclusion)
- [ ] Proper semantic HTML elements
- [ ] No generic `<div>` wrappers for content sections

#### Layout Requirements
- [ ] Single-page layout (no navigation)
- [ ] Professional design reflecting research topic
- [ ] Consistent spacing and alignment
- [ ] Visual hierarchy (headings, body text, emphasis)
- [ ] Minimum 3 colors in color scheme
- [ ] Background color or image
- [ ] At least one image or graphic related to topic

#### CSS Requirements
- [ ] All CSS in `<style>` block (internal) or external file
- [ ] NO inline styles
- [ ] CSS variables for consistent theming
- [ ] Responsive breakpoints for mobile/tablet/desktop
- [ ] No use of frameworks (Bootstrap, Tailwind, etc.)
- [ ] Proper CSS structure (selectors, specificity, DRY)

#### HTML Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project 2.2: [Topic Title]</title>
    <style>
        /* All CSS here */
    </style>
</head>
<body>
    <header>
        <h1>Main Title</h1>
        <p>Subtitle or introduction</p>
    </header>
    <main>
        <section>
            <h2>Section 1</h2>
            <p>Content...</p>
        </section>
        <section>
            <h2>Section 2</h2>
            <p>Content...</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Katie Rock</p>
    </footer>
</body>
</html>
```

### ?? Rubric Criteria (100 points total)

| Criteria | Points | Notes |
|----------|--------|-------|
| Content & Organization | 15 | Well-written, minimum 500 words, clear structure |
| HTML Structure | 15 | Valid HTML5, semantic markup, no inline styles |
| CSS Design | 20 | Professional appearance, color scheme, typography |
| Responsive Design | 15 | Works on mobile, tablet, desktop |
| Layout & Spacing | 15 | Proper alignment, white space, visual hierarchy |
| Validation | 10 | No HTML/CSS validation errors |
| Accessibility | 10 | Alt text for images, heading hierarchy, keyboard navigation |

#### CSS Best Practices
- Use CSS custom properties (variables):
  ```css
  :root {
      --primary-color: #083B55;
      --accent-color: #FF6B63;
      --font-serif: Georgia, serif;
      --font-sans: 'Segoe UI', sans-serif;
  }
  ```
- Media queries for responsiveness:
  ```css
  @media (max-width: 768px) {
      /* Mobile styles */
  }
  ```
- Avoid ID selectors for styling; use classes
- Group related properties
- Use shorthand where appropriate

---

## Project 3: Multi-Page Site

### ?? Requirements

**Location**: `inf6420-projects/project3/`  
**Base URL**: `http://141.217.120.86/fn9575/html/inf6420-projects/project3/`

#### File Requirements
- [ ] `home.html` – Homepage/introduction
- [ ] `fox.html` – Page about foxes
- [ ] `red.html` – Page about red squirrels
- [ ] `gray.html` – Page about gray squirrels
- [ ] `flying.html` – Page about flying squirrels
- [ ] `squirrels.css` – External stylesheet (shared)
- [ ] `showform.php` – Form submission handler (optional)
- [ ] `images/` folder with 5 images (home.jpg, fox.jpg, red.jpg, gray.jpg, flying.jpg)

#### Content Requirements per Page
- [ ] Minimum 300 words per page
- [ ] Relevant images (high quality)
- [ ] Professional formatting
- [ ] Consistent styling across all pages
- [ ] Factual, well-researched information

#### Navigation Requirements
- [ ] Navigation bar on every page
- [ ] Links to all 5 pages (home, fox, red, gray, flying)
- [ ] Current page highlighted/active state
- [ ] Consistent navigation placement (header or sidebar)
- [ ] Clear visual indication of current page

#### Technical Requirements
- [ ] Valid HTML5 on all pages
- [ ] External CSS file (squirrels.css)
- [ ] Responsive design
- [ ] Consistent color scheme and typography
- [ ] Proper image alt text
- [ ] Meta tags (charset, viewport)
- [ ] Semantic HTML elements

#### Form Requirements (if implemented)
- [ ] Contact form or comment form
- [ ] Minimum 3 input fields
- [ ] Submit button
- [ ] POST to `showform.php`
- [ ] Form validation on client-side
- [ ] Optional: Email field, textarea, select dropdown

#### CSS Structure
```css
/* color variables, typography, layout */
:root {
    --primary-color: #083B55;
    --accent-color: #FF6B63;
}

/* Header and navigation */
header, nav { /* styles */ }

/* Main content */
main, section { /* styles */ }

/* Footer */
footer { /* styles */ }

/* Responsive */
@media (max-width: 768px) { /* mobile styles */ }
```

### ?? Rubric Criteria (150 points total)

| Criteria | Points | Notes |
|----------|--------|-------|
| Content Quality | 25 | Well-written, factual, minimum 300 words per page |
| HTML Structure | 20 | Valid HTML5, semantic elements, consistency |
| CSS Design | 25 | Professional appearance, consistent styling |
| Navigation | 15 | Clear, functional, current page indication |
| Images & Media | 15 | High quality, proper alt text, optimization |
| Responsive Design | 20 | Mobile, tablet, desktop functionality |
| Validation | 15 | No HTML/CSS errors |
| Accessibility | 10 | Keyboard navigation, heading hierarchy, alt text |
| Form (if included) | 10 | Functional, validated, proper submission |

#### Project 3 File Checklist
```
project3/
??? home.html ........................... Homepage
??? fox.html ............................ Fox information
??? red.html ............................ Red squirrel information
??? gray.html ........................... Gray squirrel information
??? flying.html ......................... Flying squirrel information
??? squirrels.css ....................... External stylesheet
??? showform.php ........................ Form handler (optional)
??? images/
    ??? home.jpg ........................ Homepage image
    ??? fox.jpg ......................... Fox image
    ??? red.jpg ......................... Red squirrel image
    ??? gray.jpg ........................ Gray squirrel image
    ??? flying.jpg ...................... Flying squirrel image
```

---

## Project 4: Responsive Redesign

### ?? Requirements

**Location**: `inf6420-projects/project4/`  
**Base URL**: `http://141.217.120.86/fn9575/html/inf6420-projects/project4/`

#### Improvements Over Project 3
- [ ] Enhanced responsive design
- [ ] Mobile-first approach
- [ ] Improved navigation (hamburger menu for mobile)
- [ ] Touch-friendly interface elements
- [ ] Optimized images for different screen sizes
- [ ] Enhanced accessibility features

#### File Requirements (same structure as Project 3)
- [ ] `home.html`, `fox.html`, `red.html`, `gray.html`, `flying.html`
- [ ] `squirrels-responsive.css` (replaces squirrels.css with media queries)
- [ ] `showform.php` (form handler)
- [ ] `images/` folder with optimized images

#### Responsive Design Requirements
- [ ] **Mobile** (< 600px):
  - [ ] Single-column layout
  - [ ] Hamburger menu navigation
  - [ ] Touch-friendly buttons (min 44x44px)
  - [ ] Readable text (16px minimum)
- [ ] **Tablet** (600px - 1024px):
  - [ ] Two-column layout or adjusted spacing
  - [ ] Full navigation bar appears
  - [ ] Optimized image sizes
- [ ] **Desktop** (> 1024px):
  - [ ] Multi-column layout
  - [ ] Full navigation with hover effects
  - [ ] Optimized whitespace

#### CSS Requirements for Project 4
- [ ] Mobile-first approach (styles start at mobile, add breakpoints)
- [ ] Minimum 2 breakpoints (@media queries)
- [ ] Flexible layouts (flexbox or CSS Grid preferred)
- [ ] Responsive images
- [ ] Touch-friendly interactions
- [ ] No CSS frameworks

```css
/* Mobile-first approach */
body {
    font-size: 16px;
    max-width: 100%;
}

/* Tablet */
@media (min-width: 768px) {
    body {
        max-width: 95%;
    }
}

/* Desktop */
@media (min-width: 1200px) {
    body {
        max-width: 1200px;
    }
}
```

#### Navigation Enhancement for Mobile
- [ ] Hamburger menu icon (three horizontal lines)
- [ ] Toggleable nav menu
- [ ] Click/tap to open/close
- [ ] Mobile menu overlays content
- [ ] Clear "X" to close
- [ ] Smooth transitions

#### Image Optimization
- [ ] Images sized appropriately for viewports
- [ ] Use `srcset` for responsive images (bonus)
- [ ] Optimize file sizes (compress JPGs/PNGs)
- [ ] Proper aspect ratios maintained
- [ ] Lazy loading (optional, bonus)

### ?? Rubric Criteria (150 points total)

| Criteria | Points | Notes |
|----------|--------|-------|
| Mobile Design | 25 | Single column, readable, touch-friendly |
| Tablet Design | 20 | Appropriate layout adjustments |
| Desktop Design | 20 | Full-featured, optimized spacing |
| Responsive Implementation | 25 | Proper media queries, flexible layouts |
| Navigation Enhancement | 15 | Hamburger menu, functional mobile nav |
| CSS Organization | 10 | Mobile-first, DRY, well-structured |
| Performance | 10 | Optimized images, fast load times |
| Accessibility | 15 | Keyboard navigation, aria labels, heading hierarchy |
| Validation | 10 | No HTML/CSS errors |
| Polish & Usability | 15 | Professional appearance, intuitive interactions |

---

## Cross-Project Requirements

### ?? Security & Best Practices

#### Form Submission (Project 3 & 4)
- [ ] POST requests only (not GET)
- [ ] Validate inputs on client-side with JavaScript
- [ ] Sanitize inputs server-side in PHP
- [ ] No sensitive data in URLs
- [ ] CSRF protection (tokens if applicable)
- [ ] Proper error handling and user feedback

#### File Management
- [ ] No credentials stored in repository
- [ ] `.gitignore` excludes sensitive files
- [ ] Proper file permissions on server
- [ ] Images optimized for web (< 500KB each)
- [ ] No uncompressed PDFs or large files

#### Links & References
- [ ] All external links open with `rel="noopener"` (if new tab)
- [ ] Proper URL structure (no hardcoded IP addresses)
- [ ] Validate all links before submission
- [ ] Use relative paths within project
- [ ] WSU URLs for official grading links

### ?? Branding & Design Standards

#### Color Palette
- [ ] Primary accent: `#083B55` (navy blue)
- [ ] Link hover: `#FF6B63` (coral)
- [ ] Text color: `#333333` (dark gray, not pure black)
- [ ] Background: `#FFFFFF` or light gray
- [ ] Minimum 3-color scheme per project

#### Typography
- [ ] Serif font for headings: Georgia, Garamond, or serif fallback
- [ ] Sans-serif for body: 'Segoe UI', Arial, sans-serif fallback
- [ ] Base font size: 16px (readable on all devices)
- [ ] Line height: 1.5-1.6 for readability
- [ ] Proper contrast (WCAG AA minimum 4.5:1 for text)

#### Consistency
- [ ] Same header/footer across pages
- [ ] Consistent button styles
- [ ] Unified spacing system (multiples of 8px recommended)
- [ ] Same color scheme throughout
- [ ] Aligned margins and padding

### ?? Mobile Considerations

- [ ] Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- [ ] Minimum touch target: 44x44 pixels
- [ ] Test on actual mobile devices or emulator
- [ ] Portrait and landscape orientations
- [ ] Fast load times (consider image optimization)
- [ ] No horizontal scrolling on mobile

---

## Accessibility Standards

### ?? WCAG 2.1 Level AA Compliance

#### HTML Accessibility
- [ ] Proper heading hierarchy (h1 ? h2 ? h3, etc., no skipping)
- [ ] Semantic elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
- [ ] Form labels associated with inputs via `for` attribute
- [ ] Image `alt` text (descriptive, not "image of...")
- [ ] Links have descriptive text (not "click here")
- [ ] No color as only indicator (always include text/icon)

#### Keyboard Navigation
- [ ] All interactive elements accessible via Tab key
- [ ] Logical tab order (left-to-right, top-to-bottom)
- [ ] `focus-visible` outline on keyboard focus
- [ ] Skip links for navigation (optional but recommended)

```html
<style>
    a:focus-visible,
    button:focus-visible,
    input:focus-visible {
        outline: 2px solid #FF6B63;
        outline-offset: 2px;
    }
</style>
```

#### Color & Contrast
- [ ] Text contrast minimum 4.5:1 (normal text)
- [ ] UI components contrast minimum 3:1
- [ ] Test with WebAIM Contrast Checker
- [ ] No information conveyed by color alone

#### Motion & Animations
- [ ] Respect `prefers-reduced-motion` user preference
- [ ] No auto-playing media
- [ ] Animations/transitions don't interfere with content

```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation: none !important;
        transition: none !important;
    }
}
```

#### Screen Reader Compatibility
- [ ] Proper `alt` text for all images
- [ ] ARIA labels where needed (buttons without visible text)
- [ ] Landmark roles: `<nav>`, `<main>`, `<footer>`
- [ ] Form error messages associated with inputs
- [ ] Table headers use `<th>` with `scope` attribute

---

## Validation Requirements

### ? HTML Validation

- [ ] Valid HTML5 according to W3C validator
- [ ] No deprecated elements or attributes
- [ ] Proper nesting of elements
- [ ] All attributes properly quoted
- [ ] Self-closing tags used correctly

**Validate at**: https://validator.w3.org/

```html
<!-- Valid -->
<input type="text" name="email" required>
<img src="image.jpg" alt="Description">

<!-- Invalid -->
<input type='text' name=email required>
<img src="image.jpg">
```

### ?? CSS Validation

- [ ] Valid CSS3 according to W3C validator
- [ ] No unknown properties or values
- [ ] Proper selector syntax
- [ ] Vendor prefixes used appropriately (or omitted for modern browsers)
- [ ] No syntax errors

**Validate at**: https://jigsaw.w3.org/css-validator/

### ?? Link Validation

- [ ] All links are functional (no 404s)
- [ ] Test both locally and after deployment
- [ ] External links open correctly
- [ ] Download links work (DOCX, PDF, etc.)
- [ ] Email links open mail client

### ?? Responsive Validation

- [ ] Test on Chrome DevTools device emulation
- [ ] Mobile viewport (320px - 480px)
- [ ] Tablet viewport (768px - 1024px)
- [ ] Desktop viewport (1200px+)
- [ ] No horizontal scrolling on any viewport

### ? Accessibility Validation

- [ ] Run Lighthouse audit in Chrome DevTools
- [ ] Use axe DevTools or WAVE browser extension
- [ ] Manual keyboard navigation test
- [ ] Screen reader testing (NVDA or JAWS)
- [ ] Color contrast verification

---

## Submission Checklist

### ? Before Submitting Each Project

#### General
- [ ] All files in correct locations per canonical layout
- [ ] File naming follows convention (rock-project*.* format)
- [ ] No extra or duplicate files
- [ ] `.gitignore` updated if necessary
- [ ] Git history is clean (no unrelated commits)

#### Code Quality
- [ ] HTML validates without errors
- [ ] CSS validates without errors
- [ ] No console errors in browser DevTools
- [ ] All links functional
- [ ] All images load correctly

#### Accessibility & Usability
- [ ] Keyboard navigation works
- [ ] Color contrast meets WCAG AA
- [ ] Alt text on all images
- [ ] Heading hierarchy is proper
- [ ] Focus-visible states present
- [ ] Mobile-friendly responsive design

#### Testing Checklist
- [ ] Tested in Chrome
- [ ] Tested in Firefox
- [ ] Tested in Safari
- [ ] Tested on mobile device/emulator
- [ ] Tested on tablet device/emulator
- [ ] Forms work and submit properly

#### Documentation
- [ ] README.md updated (if applicable)
- [ ] Comments in complex code sections
- [ ] Rubric requirements addressed
- [ ] File structure matches requirements

#### Deployment (before final submission)
- [ ] All files uploaded to WSU server via SFTP
- [ ] URLs accessible from WSU server
- [ ] Pages load without errors on live server
- [ ] All images visible on live server
- [ ] Forms work on live server

### ?? Project-Specific Checklists

#### Project 1 (Homepage)
- [ ] Student photo included and visible
- [ ] All 4 projects linked
- [ ] Course title and semester displayed
- [ ] Professional appearance
- [ ] Mobile-responsive
- [ ] Navigation works

#### Project 2.1 (Research)
- [ ] 5-7 pages of content
- [ ] Minimum 5 credible sources
- [ ] Proper citations (APA/MLA/Chicago)
- [ ] Bibliography included
- [ ] Spelling/grammar checked
- [ ] Formatted professionally (Title page, headers, footers)

#### Project 2.2 (HTML/CSS)
- [ ] Minimum 500 words
- [ ] Based on Project 2.1 topic
- [ ] All CSS in style block or external file
- [ ] No inline styles
- [ ] Valid HTML5
- [ ] Valid CSS3
- [ ] At least one image
- [ ] Mobile-responsive

#### Project 3 (Multi-page)
- [ ] All 5 HTML pages present
- [ ] Navigation bar on each page
- [ ] Current page highlighted in nav
- [ ] All images present in images/ folder
- [ ] External CSS file (squirrels.css)
- [ ] All pages validate
- [ ] Minimum 300 words per page
- [ ] Form working (if included)

#### Project 4 (Responsive)
- [ ] Mobile layout (< 600px) functional
- [ ] Tablet layout (600-1024px) functional
- [ ] Desktop layout (> 1024px) functional
- [ ] Hamburger menu on mobile
- [ ] All 5 pages responsive
- [ ] Images optimized
- [ ] CSS uses media queries
- [ ] Mobile-first approach implemented

### ?? Final Submission

1. **Local Testing Complete**
   - [ ] All projects pass validation
   - [ ] All accessibility checks pass
   - [ ] Links and forms working

2. **Deployment Complete**
   - [ ] Files uploaded to WSU server
   - [ ] Project 1 URL accessible
   - [ ] All project links working from live server

3. **Documentation Complete**
   - [ ] Rubric requirements addressed
   - [ ] Comments added to code
   - [ ] README updated

4. **GitHub Ready**
   - [ ] All changes committed
   - [ ] Pushed to origin/main branch
   - [ ] Repository clean and organized

5. **Ready for Grading**
   - [ ] WSU URLs provided in submission
   - [ ] All deliverables accessible
   - [ ] No broken links or 404s
   - [ ] Professional appearance maintained

---

## Troubleshooting Common Issues

### ?? File Not Found / 404 Errors
- **Cause**: Incorrect file path or capitalization
- **Fix**: Verify exact filename on server; check path capitalization
- **Example**: `project3/Home.html` ? `project3/home.html`

### ??? Images Not Loading
- **Cause**: Image path incorrect or server path mismatch
- **Fix**: Use relative paths; test on both local and server
- **Check**: Verify images in `/project3/images/` folder

### ?? Download Files (DOCX, PDF)
- **Cause**: Browser security flags download
- **Fix**: Users should "Keep" file; this is normal behavior for DOCX over HTTP

### ?? Links Not Working
- **Cause**: URL format or relative path issues
- **Fix**: Test all links before deployment; use correct relative paths

### ?? Mobile Not Responsive
- **Cause**: Missing viewport meta tag or media queries
- **Fix**: Add `<meta name="viewport">` tag; ensure CSS has @media queries

### ? Validation Errors
- **Cause**: Invalid HTML/CSS syntax
- **Fix**: Run W3C validator; fix errors systematically; test again

---

## Resources & References

### ?? Official Resources
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

### ? Accessibility Resources
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM Resources](https://webaim.org/)

### ?? Design Resources
- [Color Hunt](https://colorhunt.co/)
- [Google Fonts](https://fonts.google.com/)
- [Unsplash Images](https://unsplash.com/)

### ?? Learning Resources
- [HTML Best Practices](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)
- [CSS Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Responsive Design Patterns](https://www.smashingmagazine.com/2023/04/responsive-web-design-patterns/)

---

**Document End**  
For questions or updates, refer to the project course page or contact your instructor.

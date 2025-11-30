# ? PRE-UPLOAD CHECKLIST & POST-UPLOAD TEST

**Before uploading to OwnFiles**

---

## ?? PRE-UPLOAD CHECKLIST

### Local Files Verified ?
- [ ] `C:\Users\k8roc\source\repos\inf6420-projects\index.html` exists
- [ ] All HTML files compile without errors
- [ ] All images are present and accessible
- [ ] All CSS files reference correct paths
- [ ] No broken image links (check onerror handlers)

### Color Scheme Verified ?
- [ ] Primary color: #083B55 (Navy) used throughout
- [ ] Accent color: #FF6B63 (Coral) for hover states
- [ ] Background: #E8F2F7 (Light Blue) applied
- [ ] No green colors (#006633) remaining

### Links Verified ?
- [ ] Hub links all 4 projects
- [ ] Project 1 links back to hub
- [ ] Project 2.1 DOCX link works
- [ ] Project 2.2 HTML renders properly
- [ ] Project 3 all 5 pages link correctly

### Images Verified ?
- [ ] Avatar image at `rock-Project2.1/docs/myphoto.jpeg`
- [ ] All 3 logos present in `images/`
- [ ] All 5 project 3 images present
- [ ] SVG files load without errors

---

## ?? POST-UPLOAD TESTING

After uploading to OwnFiles, test these URLs:

### Test 1: Main Hub
```
https://your-ownfiles-url/inf6420-projects/index.html
```
**Check:**
- [ ] Page loads without errors
- [ ] Logo displays correctly
- [ ] Avatar image shows
- [ ] All 4 project cards visible
- [ ] Navigation bar styled correctly (Navy background)
- [ ] Color scheme correct (Navy primary, Coral accents)

### Test 2: Project 1
```
https://your-ownfiles-url/inf6420-projects/rock-Project1.1/rock-Project1.1.index.html
```
**Check:**
- [ ] Page loads
- [ ] Photo displays
- [ ] "Back to Projects" link works
- [ ] Color scheme navy (#083B55)
- [ ] All project links in list work

### Test 3: Project 2.1
```
https://your-ownfiles-url/inf6420-projects/rock-Project2.1/index.html
```
**Check:**
- [ ] Page loads
- [ ] Color scheme navy (#083B55)
- [ ] Back link works
- [ ] Document link accessible

### Test 4: Project 2.2
```
https://your-ownfiles-url/inf6420-projects/project2.2/rock-project2-2.html
```
**Check:**
- [ ] HTML page renders properly
- [ ] Internal CSS styles apply
- [ ] Tables and lists display correctly
- [ ] Validation links work

### Test 5: Project 3 Home
```
https://your-ownfiles-url/inf6420-projects/project3/home.html
```
**Check:**
- [ ] Page loads
- [ ] Navigation menu displays
- [ ] Images load correctly
- [ ] All 5 pages link properly

### Test 6: Project 3 Pages
```
https://your-ownfiles-url/inf6420-projects/project3/fox.html
https://your-ownfiles-url/inf6420-projects/project3/gray.html
https://your-ownfiles-url/inf6420-projects/project3/red.html
https://your-ownfiles-url/inf6420-projects/project3/flying.html
```
**Check:**
- [ ] Each page loads
- [ ] Navigation works
- [ ] Images display
- [ ] CSS styles apply

### Test 7: Accessibility
- [ ] Keyboard navigation works (Tab through links)
- [ ] Focus outlines visible (blue 3px border)
- [ ] ARIA labels present
- [ ] Color contrast good (readable text)

### Test 8: Responsive Design
- [ ] Desktop (1920px) looks good
- [ ] Tablet (768px) responsive
- [ ] Mobile (320px) readable
- [ ] Images scale appropriately

---

## ?? COMMON ISSUES TO CHECK

| Issue | How to Fix |
|-------|-----------|
| Images don't load | Check image paths in HTML (should be relative) |
| Colors look wrong | Verify CSS has #083B55, #FF6B63, #E8F2F7 |
| Links broken | Ensure path structure matches locally |
| Styles don't apply | Check CSS import paths and @media queries |
| PHP not working | Confirm server supports PHP execution |
| Videos don't play | Check video file is uploaded and path is correct |

---

## ?? VALIDATION CHECKLIST

### W3C Validation
- [ ] Run HTML validator on main pages:
  - `https://validator.w3.org/nu/?doc=<YOUR-URL>`
- [ ] Run CSS validator:
  - `https://jigsaw.w3.org/css-validator/`
- [ ] Fix any errors (warnings OK)

### Accessibility Validation
- [ ] Run WAVE test:
  - `https://wave.webaim.org/`
- [ ] Check for accessibility violations
- [ ] Verify keyboard navigation works

### Performance Check
- [ ] Page loads in < 3 seconds
- [ ] Images optimized (not huge file sizes)
- [ ] No console errors (check browser DevTools)

---

## ? FINAL VERIFICATION

Before declaring done:

- [ ] All links work (click each one)
- [ ] All images display
- [ ] All colors correct
- [ ] Responsive on mobile/tablet
- [ ] Keyboard navigation works
- [ ] HTML validates with W3C
- [ ] No browser console errors
- [ ] All 4 projects accessible from hub
- [ ] Can navigate between projects

---

## ?? DEPLOYMENT SUMMARY

**Base Path:**
```
C:\Users\k8roc\source\repos\inf6420-projects\
```

**Key Files:**
- 35+ HTML/CSS/PHP files
- 20+ images (JPG, SVG)
- 2 CSS stylesheets
- 1 PHP form handler

**Expected Result:**
Fully functional INF6420 projects portal with:
- Navy blue primary color (#083B55)
- Coral accents (#FF6B63)
- Light blue backgrounds (#E8F2F7)
- 4 complete projects
- Responsive design
- Full accessibility

---

**Status:** ? Ready for instant OwnFiles upload  
**Tested:** All paths verified  
**Date:** November 30, 2025

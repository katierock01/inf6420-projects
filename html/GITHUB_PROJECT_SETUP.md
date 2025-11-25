# GitHub Project Setup Guide for INF6420

This guide provides detailed instructions for setting up GitHub Projects to manage course assignments and track progress throughout INF 6420.

## Overview

GitHub Projects is a project management tool integrated with GitHub that helps organize and track work using boards, tables, and automation. For this course, we'll create **Project1** to manage all assignments.

## Table of Contents

1. [Automated Setup (Recommended)](#automated-setup-recommended)
2. [Manual Setup](#manual-setup)
3. [Project Configuration](#project-configuration)
4. [Using the Project Board](#using-the-project-board)
5. [Best Practices](#best-practices)

---

## Automated Setup (Recommended)

If you have Python 3 and GitHub CLI installed, use the automated script:

### Prerequisites

- Python 3.x installed
- GitHub CLI (`gh`) installed and authenticated
  - Install from: https://cli.github.com/
  - Authenticate: `gh auth login`

### Running the Script

```bash
# Navigate to the repository
cd /path/to/inf6420-projects

# Run the setup script
python scripts/setup_github_project.py
```

The script will:
✅ Update repository description  
✅ Create "Project1" for course tracking  
✅ List all existing projects  
✅ Provide next steps and URLs  

---

## Manual Setup

If the automated script doesn't work, follow these steps:

### Step 1: Update Repository Description

1. Go to https://github.com/katierock01/inf6420-projects
2. Click the **gear icon** (⚙️) next to "About" on the right sidebar
3. In the "Description" field, enter:
   ```
   Default repository for all assignments in INF6420 course - Web Development and Scripting
   ```
4. Optionally, add topics: `web-development`, `inf6420`, `html`, `css`, `accessibility`
5. Click **Save changes**

### Step 2: Create GitHub Project

1. Navigate to the Projects tab:
   - Click **Projects** at the top of the repository page
   - OR go directly to: https://github.com/katierock01/inf6420-projects/projects

2. Click **New project** (green button)

3. Choose a template:
   - Select **Board** view (recommended for visual tracking)
   - OR select **Table** view for detailed information

4. Configure the project:
   - **Project name**: `Project1`
   - **Description**: `INF6420 Course Assignments and Projects Tracking`
   - **Visibility**: Choose based on preference (Private or Public)

5. Click **Create project**

### Step 3: Set Up Project Columns

For a **Board** view, create these columns:

1. **📋 To Do** - Assignments not yet started
2. **🔄 In Progress** - Currently working on
3. **👀 Review** - Completed, awaiting feedback
4. **✅ Completed** - Finished and graded

To add columns:
- Click **+ Add column** on the board
- Name the column and set automation rules if desired

### Step 4: Link Project to Repository

1. In the project settings (⚙️ icon in project view)
2. Under **Linked repositories**, click **Add repository**
3. Select `katierock01/inf6420-projects`
4. This allows you to create issues directly from the project board

---

## Project Configuration

### Creating Issues for Assignments

Each course assignment should be tracked as an issue:

1. Click **New issue** in the repository
2. Title format: `[ProjectX.X] Assignment Name`
   - Example: `[Project1.1] Create Introduction Page`
3. Description should include:
   - Assignment requirements
   - Due date
   - Grading criteria
   - Links to relevant resources
4. Add labels: `assignment`, `project-1`, `html`, etc.
5. Assign to yourself
6. Link to Project1

### Sample Issue Template

```markdown
## Assignment: Project 1.1 - Introduction Page

### Requirements
- [ ] Create HTML page with proper structure
- [ ] Include semantic markup
- [ ] Add links to subsequent projects
- [ ] Ensure W3C validation passes

### Due Date
[Insert date here]

### Resources
- Assignment PDF: [link]
- WSU URL: [link]
- Validator: https://validator.w3.org/

### Notes
Add any additional notes or questions here.
```

### Setting Up Automation

GitHub Projects supports automation to move issues between columns:

1. Click **•••** (three dots) in a column header
2. Select **Manage automation**
3. Configure rules like:
   - **Auto-add**: Automatically add new issues with label `assignment`
   - **Auto-move**: Move to "In Progress" when issue is assigned
   - **Auto-archive**: Move to "Completed" when issue is closed

---

## Using the Project Board

### Daily Workflow

1. **Check Project1 board** to see current status
2. **Move issues** between columns as you work:
   - Drag from "To Do" to "In Progress" when starting
   - Move to "Review" when ready for feedback
   - Move to "Completed" after grading
3. **Update issues** with progress notes
4. **Close issues** when fully complete

### Linking Commits to Issues

Reference issues in commit messages:

```bash
git commit -m "Complete HTML structure for Project 1.1 - fixes #1"
```

This automatically links the commit to issue #1.

### Viewing Progress

- **Board view**: Visual Kanban-style board
- **Table view**: Spreadsheet with all details
- **Roadmap view**: Timeline view for deadlines

Access these views from the view selector in the project.

---

## Best Practices

### Organization

✅ **Create one issue per assignment** - Don't combine multiple projects  
✅ **Use descriptive titles** - Include project number and brief description  
✅ **Add labels consistently** - Makes filtering and searching easier  
✅ **Set due dates** - Use issue milestones or custom fields  
✅ **Link related issues** - Cross-reference when projects build on each other  

### Documentation

✅ **Comment on progress** - Add updates as you work  
✅ **Include validator results** - Screenshot or paste validation output  
✅ **Document problems** - Note any issues for troubleshooting  
✅ **Track feedback** - Record instructor comments for future reference  

### Collaboration

✅ **Use @mentions** - Tag instructor or peers for questions  
✅ **Link to live URLs** - Include both WSU and GitHub Pages URLs  
✅ **Share screenshots** - Visual confirmation of completed work  
✅ **Update README** - Keep project documentation current  

---

## Troubleshooting

### Problem: Can't create project

**Solution**: Ensure you have write permissions to the repository. Owner or collaborators can create projects.

### Problem: Issues don't appear in project

**Solution**: 
1. Check that issue is assigned to Project1
2. Verify automation rules aren't filtering it out
3. Manually add issue using **+ Add item** button

### Problem: Automation not working

**Solution**:
1. Review automation rules in column settings
2. Ensure labels match automation triggers
3. GitHub Projects automation may have delays (wait a few minutes)

### Problem: Lost access to project

**Solution**:
1. Check project visibility settings
2. Ensure you're logged into correct GitHub account
3. Repository owner can restore access

---

## Additional Resources

- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [Managing Project Boards](https://docs.github.com/en/issues/organizing-your-work-with-project-boards)
- [GitHub Issues Guide](https://docs.github.com/en/issues)
- [Best Practices for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects)

---

## Example Project Structure

Here's what a well-organized Project1 might look like:

```
Project1: INF6420 Course Assignments
│
├── 📋 To Do
│   ├── #5 [Project3.1] Advanced Forms and Validation
│   └── #6 [Project3.2] JavaScript Interactivity
│
├── 🔄 In Progress
│   └── #3 [Project2.2] Complete HTML with Internal CSS
│
├── 👀 Review
│   └── #2 [Project2.1] Document Landing Page
│
└── ✅ Completed
    └── #1 [Project1.1] Introduction Page ✓
```

---

## Summary

You've now set up **Project1** for managing INF 6420 assignments! This project board will help you:

- Track all assignments in one place
- Visualize your progress throughout the course
- Stay organized with deadlines and requirements
- Document your work for future reference

**Next Steps:**
1. Create issues for current assignments
2. Link them to Project1
3. Start moving issues through the workflow
4. Commit code with issue references

Happy coding! 🚀

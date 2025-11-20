#!/usr/bin/env python3
"""
Generate the overview.html page with all project requirements and deliverables.
This script creates a comprehensive overview page for the INF 6420 course projects.
"""

from pathlib import Path
from datetime import datetime

# Project data structure
PROJECTS = [
    {
        "id": "1.1",
        "title": "Personal Introduction Page",
        "status": "Complete",
        "submission": "rock-Project1.1/rock-Project1.1.index.html",
        "requirements": [
            "Create a personal introduction page using basic HTML and CSS",
            "Include personal photo, name, and background information",
            "Demonstrate proper HTML structure (header, main, footer)",
            "Apply inline or embedded CSS for styling",
            "Include link to Project 2.1 DOCX file",
            "Include link to Project 2.2 HTML page",
            "Ensure accessibility with semantic HTML elements",
        ],
        "deliverables": {
            "File": "rock-Project1.1/rock-Project1.1.index.html",
            "Format": "HTML with embedded CSS",
            "Links": "Must link to Project 2.1 DOCX and Project 2.2 HTML",
        },
        "local_url": "rock-Project1.1/rock-Project1.1.index.html",
        "server_url": "http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project1.1/rock-Project1.1.index.html",
    },
    {
        "id": "2.1",
        "title": "Research Paper (DOCX)",
        "status": "Complete",
        "submission": "rock-project2.1.docx",
        "requirements": [
            'Research paper on "The Impact of AI on Web Accessibility"',
            "Approximately 8 pages, double-spaced",
            "Include proper headings, tables, and lists",
            "References section with APA formatting",
            "No AI-generated content (per rubric)",
            "Professional formatting in Microsoft Word",
            "Link from Project 1.1 page to this DOCX file",
        ],
        "deliverables": {
            "File": "rock-Project2.1/rock-project2.1.docx",
            "Format": "Microsoft Word document",
            "Server Path": "html/inf6420-projects/rock-project2.1.docx",
            "Linked From": "Project 1.1 page",
        },
        "local_url": "rock-Project2.1/rock-project2.1.docx",
        "server_url": "http://141.217.120.86/fn9575/html/inf6420-projects/rock-Project2.1/rock-project2.1.docx",
    },
    {
        "id": "2.2",
        "title": "HTML Conversion with Internal CSS",
        "status": "Complete",
        "submission": "project2.2/rock-project2-2.html",
        "requirements": [
            "Convert Project 2.1 research paper to HTML format",
            "Use <strong>internal CSS only</strong> (no external stylesheets)",
            "Include styled tables with colored borders",
            "Include styled ordered and unordered lists with different formatting",
            "Apply proper semantic HTML structure",
            "Include working validator links (HTML and CSS)",
            "Ensure WCAG 2.2 accessibility compliance",
            "Add skip link, keyboard focus styles, and ARIA labels",
            "Include print-friendly CSS with @media print",
            "Respect reduced motion preferences with @media (prefers-reduced-motion)",
        ],
        "deliverables": {
            "File": "project2.2/rock-project2-2.html",
            "Format": "HTML with internal CSS (style tag in head)",
            "Tables": "Styled with colored borders (primary color theme)",
            "Lists": "OL and UL with distinct styling",
            "Validators": "W3C HTML and CSS validator links embedded",
            "Accessibility": "WCAG 2.2 compliant",
        },
        "local_url": "project2.2/rock-project2-2.html",
        "server_url": "http://141.217.120.86/fn9575/html/inf6420-projects/project2.2/rock-project2-2.html",
        "validators": {
            "html": "https://validator.w3.org/nu/?doc=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Fproject2.2%2Frock-project2-2.html",
            "css": "https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Fproject2.2%2Frock-project2-2.html",
        },
    },
    {
        "id": "3",
        "title": "Multi-Page Interactive Website",
        "status": "Complete",
        "submission": "project3/home.html",
        "requirements": [
            "Create a multi-page website about Michigan squirrels",
            "Use <strong>external CSS</strong> (squirrels.css)",
            "Implement consistent navigation across all pages",
            "Include multiple HTML pages (home, fox, gray, red, flying)",
            "Apply proper layout using float-based CSS (navigation + main content)",
            "Include PHP form handler (showform.php) to process form data",
            "Demonstrate semantic HTML structure",
            "Include dynamic validator links in footer",
            "Use images appropriately with alt text",
        ],
        "deliverables": {
            "Main File": "project3/home.html",
            "Additional Pages": "fox.html, gray.html, red.html, flying.html, index.html",
            "Stylesheet": "squirrels.css (external, linked from all pages)",
            "PHP Handler": "showform.php (demonstrates server-side processing)",
            "Layout": "Float-based two-column layout (navigation + main content)",
            "Navigation": "Consistent across all pages",
        },
        "local_url": "project3/home.html",
        "server_url": "http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html",
        "validators": {
            "html": "https://validator.w3.org/nu/?doc=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Fproject3%2Fhome.html",
            "css": "https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2F141.217.120.86%2Ffn9575%2Fhtml%2Finf6420-projects%2Fproject3%2Fsquirrels.css",
        },
    },
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>INF 6420 – Projects Overview</title>
  <meta name="description" content="Complete overview of all INF 6420 course projects with requirements and deliverables by Katie Rock." />
  <link rel="icon" href="favicon.svg" type="image/svg+xml" />
  <style>
    :root {{
      --wsu-green: #115740;
      --wsu-green-light: #1a6e52;
      --wsu-green-dark: #0d4230;
      --accent: #FF6B63;
      --bg: #f7faf7;
      --card-bg: #ffffff;
      --text: #222;
      --muted: #5a5a5a;
      --shadow: 0 8px 20px rgba(0,0,0,0.08);
      --radius: 14px;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ height: 100%; }}
    body {{
      margin: 0;
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      color: var(--text);
      background:
        radial-gradient(1000px 400px at -10% -20%, rgba(17, 87, 64, 0.08) 0%, transparent 60%),
        radial-gradient(800px 300px at 110% -10%, rgba(26, 110, 82, 0.08) 0%, transparent 60%),
        var(--bg);
    }}
    .topbar {{
      background: var(--wsu-green);
      color: #fff;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }}
    .brand {{
      font-weight: 800;
      letter-spacing: 0.2px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .topbar .nav a {{
      color: #fff;
      text-decoration: none;
      margin-left: 16px;
      opacity: 0.95;
      font-weight: 600;
    }}
    .topbar .nav a:hover {{
      opacity: 1;
      text-decoration: underline;
    }}
    header {{
      background: linear-gradient(135deg, var(--wsu-green), var(--wsu-green-light));
      color: white;
      padding: 48px 20px 32px;
      text-align: center;
    }}
    header h1 {{
      margin: 0;
      font-size: 2.2rem;
      letter-spacing: 0.2px;
    }}
    header p {{
      margin: 10px auto 0;
      max-width: 700px;
      color: #e9ffef;
      font-size: 1.05rem;
    }}
    .container {{
      max-width: 1200px;
      margin: 28px auto;
      padding: 0 20px 40px;
    }}
    .project-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 24px;
      margin-bottom: 24px;
      border-left: 5px solid var(--wsu-green);
    }}
    .project-section h2 {{
      margin: 0 0 8px;
      font-size: 1.6rem;
      color: var(--wsu-green);
      font-family: Georgia, "Times New Roman", Times, serif;
    }}
    .project-meta {{
      color: var(--muted);
      font-size: 0.9rem;
      margin-bottom: 16px;
      font-style: italic;
    }}
    .project-section h3 {{
      margin: 20px 0 10px;
      font-size: 1.2rem;
      color: var(--wsu-green-dark);
      font-family: Georgia, "Times New Roman", Times, serif;
    }}
    .requirements-list {{
      background: rgba(17, 87, 64, 0.05);
      border-left: 3px solid var(--wsu-green-light);
      padding: 12px 16px;
      margin: 12px 0;
      border-radius: 6px;
    }}
    .requirements-list ul {{
      margin: 8px 0;
      padding-left: 24px;
    }}
    .requirements-list li {{
      margin: 6px 0;
      line-height: 1.6;
    }}
    .deliverables {{
      background: #fffbe7;
      border: 1px solid #ffe69c;
      border-radius: 8px;
      padding: 14px 18px;
      margin: 14px 0;
    }}
    .deliverables h4 {{
      margin: 0 0 10px;
      color: var(--wsu-green-dark);
      font-size: 1.05rem;
    }}
    .btn-group {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 16px;
    }}
    .btn {{
      display: inline-block;
      padding: 10px 18px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 600;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .btn-primary {{
      background: var(--wsu-green);
      color: white;
      box-shadow: 0 2px 8px rgba(17, 87, 64, 0.3);
    }}
    .btn-primary:hover {{
      background: var(--wsu-green-dark);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(17, 87, 64, 0.4);
    }}
    .btn-secondary {{
      background: white;
      color: var(--wsu-green);
      border: 2px solid var(--wsu-green-light);
    }}
    .btn-secondary:hover {{
      background: rgba(17, 87, 64, 0.08);
      transform: translateY(-2px);
    }}
    .status-badge {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .status-complete {{
      background: #d4edda;
      color: #155724;
    }}
    footer {{
      text-align: center;
      color: var(--muted);
      font-size: 0.9rem;
      padding: 26px 16px 40px;
      border-top: 1px solid rgba(17, 87, 64, 0.25);
      margin-top: 40px;
    }}
    .pill {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 999px;
      background: rgba(17, 87, 64, 0.15);
      color: var(--wsu-green);
      font-weight: 700;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .topbar .nav a:focus-visible,
    .btn:focus-visible,
    a:focus-visible {{
      outline: 3px solid #2b90ff;
      outline-offset: 2px;
      border-radius: 8px;
    }}
    @media (prefers-reduced-motion: reduce) {{
      * {{ animation: none !important; transition: none !important; }}
    }}
    @media print {{
      body {{ background: #fff !important; }}
      .topbar {{ display: none !important; }}
      header {{ background: none !important; color: #000 !important; }}
      .project-section {{ box-shadow: none !important; border-color: #000 !important; }}
      h1, h2, h3 {{ color: #000 !important; }}
      a {{ color: #000 !important; text-decoration: underline; }}
      .btn-group {{ display: none !important; }}
    }}
  </style>
</head>
<body>
  <div class="topbar">
    <div class="brand">
      <img src="images/logo-icon.svg" alt="Katie Rock logo" style="height:28px; width:auto" onerror="this.style.display='none'" />
      <span>Katie Rock, LLMSW</span>
    </div>
    <nav class="nav" aria-label="Primary">
      <a href="index.html">Projects Hub</a>
      <a href="submission.html">Submission</a>
      <a href="docs/index.html">Docs</a>
      <a href="https://github.com/katierock01/inf6420-projects" target="_blank" rel="noopener">GitHub</a>
    </nav>
  </div>

  <header>
    <h1>INF 6420 – Projects Overview</h1>
    <p>Complete requirements, deliverables, and submission details for all course projects.</p>
  </header>

  <main class="container">
{project_sections}
  </main>

  <footer>
    <span class="pill">INF 6420</span>
    <div style="margin-top: 10px;">&copy; {year} Katie Rock, LLMSW · Wayne State University</div>
    <div style="margin-top: 8px;">
      <a href="index.html" style="color: var(--wsu-green); text-decoration: none;">Projects Hub</a> · 
      <a href="submission.html" style="color: var(--wsu-green); text-decoration: none;">Submission</a> · 
      <a href="docs/index.html" style="color: var(--wsu-green); text-decoration: none;">Docs</a>
    </div>
  </footer>

  <script>
    document.querySelectorAll('a[target="_blank"]').forEach(a => {{
      const rel = (a.getAttribute('rel') || '').toLowerCase();
      if (!rel.includes('noopener')) a.setAttribute('rel', (rel + ' noopener noreferrer').trim());
    }});
  </script>
</body>
</html>
"""


def generate_project_section(project):
    """Generate HTML for a single project section."""
    
    # Requirements list
    req_items = "\n".join(f"          <li>{req}</li>" for req in project["requirements"])
    requirements = f"""      <h3>Requirements</h3>
      <div class="requirements-list">
        <ul>
{req_items}
        </ul>
      </div>"""
    
    # Deliverables
    deliv_items = "\n".join(
        f"          <li><strong>{key}:</strong> {value}</li>"
        for key, value in project["deliverables"].items()
    )
    deliverables = f"""      <div class="deliverables">
        <h4>Deliverables</h4>
        <ul>
{deliv_items}
        </ul>
      </div>"""
    
    # Buttons
    buttons = [
        f'        <a href="{project["local_url"]}" class="btn btn-primary">View Project</a>',
        f'        <a href="{project["server_url"]}" class="btn btn-secondary" target="_blank" rel="noopener">Live on Server</a>',
    ]
    
    # Add validator buttons if present
    if "validators" in project:
        buttons.append(
            f'        <a href="{project["validators"]["html"]}" class="btn btn-secondary" target="_blank" rel="noopener">Validate HTML</a>'
        )
        buttons.append(
            f'        <a href="{project["validators"]["css"]}" class="btn btn-secondary" target="_blank" rel="noopener">Validate CSS</a>'
        )
    
    btn_group = f"""      <div class="btn-group">
{chr(10).join(buttons)}
      </div>"""
    
    # Full section
    return f"""    <section class="project-section">
      <h2>Project {project["id"]} – {project["title"]}</h2>
      <p class="project-meta">
        <span class="status-badge status-complete">{project["status"]}</span> · 
        Submission: {project["submission"]}
      </p>
      
{requirements}

{deliverables}

{btn_group}
    </section>
"""


def main():
    """Generate the overview.html page."""
    print("Generating overview.html...")
    
    # Generate all project sections
    project_sections = "\n".join(generate_project_section(p) for p in PROJECTS)
    
    # Build final HTML
    html_content = HTML_TEMPLATE.format(
        project_sections=project_sections,
        year=datetime.now().year
    )
    
    # Write to file
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_file = project_root / "overview.html"
    
    output_file.write_text(html_content, encoding="utf-8")
    
    print(f"✓ Generated: {output_file}")
    print(f"✓ Total projects: {len(PROJECTS)}")
    print("\nTo view: Open overview.html in your browser")


if __name__ == "__main__":
    main()

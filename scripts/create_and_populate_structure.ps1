<<<<<<< Updated upstream
# Enhanced PowerShell script to create and consolidate the INF6420 project structure
# Run from the root: C:\Users\k8roc\source\repos\inf6420-projects
# This script consolidates existing files, creates missing directories/files, and populates content

param(
    [switch]$Force  # Overwrite existing files
)

function Write-Log {
    param([string]$Message)
    Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $Message"
}

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
        Write-Log "Created directory: $Path"
    }
}

function Move-FileIfExists {
    param([string]$Source, [string]$Destination)
    if (Test-Path $Source) {
        if (Test-Path $Destination) {
            if ($Force) {
                Move-Item -Path $Source -Destination $Destination -Force
                Write-Log "Overwrote and moved $Source to $Destination"
            } else {
                Write-Log "Skipped moving $Source to $Destination (destination exists, use -Force to overwrite)"
            }
        } else {
            Move-Item -Path $Source -Destination $Destination
            Write-Log "Moved $Source to $Destination"
        }
    }
}

function Create-FileWithContent {
    param([string]$Path, [string]$Content)
    if (-not (Test-Path $Path) -or $Force) {
        $Content | Out-File -FilePath $Path -Encoding UTF8 -Force
        Write-Log "Created/updated file: $Path"
    } else {
        Write-Log "Skipped creating $Path (file exists, use -Force to overwrite)"
    }
}

Write-Log "Starting INF6420 project structure consolidation and population"

# Consolidate existing files
# Move project3/ to inf6420-projects/project3/ if it exists at root
if (Test-Path "project3") {
    Move-FileIfExists -Source "project3" -Destination "inf6420-projects\project3"
}

# Similarly for project4
if (Test-Path "project4") {
    Move-FileIfExists -Source "project4" -Destination "inf6420-projects\project4"
}

# Move scripts/ to inf6420-projects/scripts/ if needed, but check
# Assuming scripts/ at root should stay, but if inf6420-projects/scripts/ exists, merge or something
# For now, ensure scripts/ at root

# Create directories
$directories = @(
    "img",
    "inf6420-projects",
    "inf6420-projects\project3",
    "inf6420-projects\project3\images",
    "inf6420-projects\project4",
    "inf6420-projects\project4\images",
    "scripts",
    "docs",
    "styles",
    "images"
)

foreach ($dir in $directories) {
    Ensure-Directory -Path $dir
}

# Populate files with content (using here-strings)
# rock-INF6420-index.html
$content = @"
=======

# PowerShell script to create the directory structure and populate files with complete content
# Run from the root: C:\Users\k8roc\source\repos\inf6420-projects

# Create directories
New-Item -ItemType Directory -Force -Path "img"
New-Item -ItemType Directory -Force -Path "inf6420-projects"
New-Item -ItemType Directory -Force -Path "inf6420-projects/project3"
New-Item -ItemType Directory -Force -Path "inf6420-projects/project3/images"
New-Item -ItemType Directory -Force -Path "inf6420-projects/project4"
New-Item -ItemType Directory -Force -Path "inf6420-projects/project4/images"
New-Item -ItemType Directory -Force -Path "scripts"
New-Item -ItemType Directory -Force -Path "docs"
New-Item -ItemType Directory -Force -Path "styles"
New-Item -ItemType Directory -Force -Path "images"

# Populate files with content (using here-strings for multi-line)
@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INF6420 Projects - Katie Rock</title>
    <link rel="stylesheet" href="styles/brand.css">
    <style>
        :root {
            --primary-accent: #083B55;
            --link-hover: #FF6B63;
            --font-serif: 'Georgia', serif;
            --font-sans: 'Arial', sans-serif;
        }
        body { font-family: var(--font-sans); margin: 0; padding: 20px; background-color: #f4f4f4; }
        header { background-color: var(--primary-accent); color: white; padding: 10px; text-align: center; }
        .project-card { border: 1px solid #ddd; margin: 10px; padding: 15px; background: white; }
        .project-card h2 { font-family: var(--font-serif); }
        a { color: var(--primary-accent); text-decoration: none; }
        a:hover { color: var(--link-hover); }
        @media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; } }
    </style>
</head>
<body>
    <header>
        <h1>INF6420 Web Development Portfolio - Katie Rock</h1>
        <nav>
            <a href="#project1">Project 1</a> |
            <a href="#project2">Project 2</a> |
            <a href="#project3">Project 3</a> |
            <a href="#project4">Project 4</a>
        </nav>
    </header>
    <main>
        <section id="project1" class="project-card">
            <h2>Project 1: Course Homepage</h2>
            <p>This is the main hub page for the INF6420 portfolio.</p>
            <a href="http://141.217.120.86/fn9575/html/inf6420-projects/rock-INF6420-index.html">View Live</a>
        </section>
        <section id="project2" class="project-card">
            <h2>Project 2: HTML/CSS Basics</h2>
            <p>Paper and HTML version demonstrating basics.</p>
            <a href="inf6420-projects/rock-project2.1.docx">Paper</a> | <a href="http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html">HTML Live</a>
        </section>
        <section id="project3" class="project-card">
            <h2>Project 3: Squirrels Site</h2>
            <p>Multi-page site with CSS.</p>
            <a href="http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html">Home Live</a>
        </section>
        <section id="project4" class="project-card">
            <h2>Project 4: Responsive Redesign</h2>
            <p>Responsive version of Project 3.</p>
            <a href="http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html">Home Live</a>
        </section>
    </main>
    <footer>
        <p>Validation: <a href="https://validator.w3.org/nu/?doc=http://141.217.120.86/fn9575/html/inf6420-projects/rock-INF6420-index.html" target="_blank" rel="noopener">HTML</a> | <a href="https://jigsaw.w3.org/css-validator/validator?uri=http://141.217.120.86/fn9575/html/inf6420-projects/rock-INF6420-index.html&profile=css3" target="_blank" rel="noopener">CSS</a></p>
    </footer>
</body>
</html>
"@ | Out-File -FilePath "rock-INF6420-index.html" -Encoding UTF8

# Note: rock-project2.1.docx is a Word document; create manually or use a template

@"
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "rock-INF6420-index.html" -Content $content

# Note: rock-project2.1.docx is a Word document; create manually or use a template

$content = @"
=======
"@ | Out-File -FilePath "rock-INF6420-index.html" -Encoding UTF8

# Note: rock-project2.1.docx is a Word document; create manually or use a template

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project 2.2: HTML/CSS Version</title>
    <link rel="stylesheet" href="../styles/brand.css">
    <style>
        body { padding: 20px; }
        h1 { color: var(--primary-accent); }
    </style>
</head>
<body>
    <h1>Project 2.2: HTML/CSS Basics</h1>
    <p>This page demonstrates basic HTML and CSS.</p>
    <footer>
        <p>Validation: <a href="https://validator.w3.org/nu/?doc=http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html" target="_blank" rel="noopener">HTML</a> | <a href="https://jigsaw.w3.org/css-validator/validator?uri=http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html&profile=css3" target="_blank" rel="noopener">CSS</a></p>
    </footer>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\rock-project2-2.html" -Content $content

# Project 3 files
$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/rock-project2-2.html" -Encoding UTF8

# Project 3 files
@"
>>>>>>> Stashed changes
@import url("../../styles/brand.css");

body {
    margin: 0;
    padding: 20px;
}

nav {
    background-color: var(--primary-accent);
    color: white;
    padding: 10px;
}

nav a {
    color: white;
    margin-right: 10px;
}

main img {
    max-width: 100%;
    height: auto;
}
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project3\squirrels.css" -Content $content

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project3/squirrels.css" -Encoding UTF8

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Home</title>
    <link rel="stylesheet" href="squirrels.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Welcome to the Squirrels Site</h1>
        <img src="images/home.jpg" alt="Home image of squirrels">
        <p>Learn about different types of squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project3\home.html" -Content $content

# Similar for other project3 HTML files - fox.html, red.html, gray.html, flying.html
# For brevity, only home.html shown; repeat pattern for others

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project3/home.html" -Encoding UTF8

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Fox Squirrel</title>
    <link rel="stylesheet" href="squirrels.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Fox Squirrel</h1>
        <img src="images/fox.jpg" alt="Fox squirrel">
        <p>Information about fox squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project3\fox.html" -Content $content

# Repeat for red.html, gray.html, flying.html with appropriate titles and content

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project3/fox.html" -Encoding UTF8

# Similar for red.html, gray.html, flying.html - repeat pattern with unique content

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Red Squirrel</title>
    <link rel="stylesheet" href="squirrels.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Red Squirrel</h1>
        <img src="images/red.jpg" alt="Red squirrel">
        <p>Information about red squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project3\red.html" -Content $content

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project3/red.html" -Encoding UTF8

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Gray Squirrel</title>
    <link rel="stylesheet" href="squirrels.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Gray Squirrel</h1>
        <img src="images/gray.jpg" alt="Gray squirrel">
        <p>Information about gray squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project3\gray.html" -Content $content

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project3/gray.html" -Encoding UTF8

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Flying Squirrel</title>
    <link rel="stylesheet" href="squirrels.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Flying Squirrel</h1>
        <img src="images/flying.jpg" alt="Flying squirrel">
        <p>Information about flying squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project3\flying.html" -Content $content

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project3/flying.html" -Encoding UTF8

@"
>>>>>>> Stashed changes
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    echo "<h1>Form Submission</h1><table border='1'>";
    foreach ($_POST as $key => $value) {
        echo "<tr><td>$key</td><td>$value</td></tr>";
    }
    echo "</table>";
} else {
    echo "<p>No form data submitted.</p>";
}
?>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project3\showform.php" -Content $content

# Project 4 - similar to project3 but responsive
$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project3/showform.php" -Encoding UTF8

# Project 4 files - similar to project3 but with responsive CSS
@"
>>>>>>> Stashed changes
@import url("../../styles/brand.css");

body {
    margin: 0;
    padding: 20px;
}

nav {
    background-color: var(--primary-accent);
    color: white;
    padding: 10px;
}

nav a {
    color: white;
    margin-right: 10px;
}

main img {
    max-width: 100%;
    height: auto;
}

@media (max-width: 768px) {
    nav a {
        display: block;
        margin: 5px 0;
    }
    main {
        padding: 10px;
    }
}
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project4\squirrels-responsive.css" -Content $content

# Home for project4
$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project4/squirrels-responsive.css" -Encoding UTF8

# Home for project4 - similar structure
@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Home (Responsive)</title>
    <link rel="stylesheet" href="squirrels-responsive.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Welcome to the Squirrels Site (Responsive)</h1>
        <img src="images/home.jpg" alt="Home image of squirrels">
        <p>Learn about different types of squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project4\home.html" -Content $content

# Repeat for fox.html, red.html, gray.html, flying.html in project4 with same content but responsive CSS

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project4/home.html" -Encoding UTF8

# Repeat for fox.html, red.html, gray.html, flying.html in project4 with same content but responsive CSS

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Fox Squirrel (Responsive)</title>
    <link rel="stylesheet" href="squirrels-responsive.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Fox Squirrel</h1>
        <img src="images/fox.jpg" alt="Fox squirrel">
        <p>Information about fox squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project4\fox.html" -Content $content

# Similar for red, gray, flying

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project4/fox.html" -Encoding UTF8

# Similar for red, gray, flying

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Red Squirrel (Responsive)</title>
    <link rel="stylesheet" href="squirrels-responsive.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Red Squirrel</h1>
        <img src="images/red.jpg" alt="Red squirrel">
        <p>Information about red squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project4\red.html" -Content $content

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project4/red.html" -Encoding UTF8

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Gray Squirrel (Responsive)</title>
    <link rel="stylesheet" href="squirrels-responsive.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Gray Squirrel</h1>
        <img src="images/gray.jpg" alt="Gray squirrel">
        <p>Information about gray squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project4\gray.html" -Content $content

$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project4/gray.html" -Encoding UTF8

@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Squirrels - Flying Squirrel (Responsive)</title>
    <link rel="stylesheet" href="squirrels-responsive.css">
</head>
<body>
    <nav>
        <a href="home.html">Home</a>
        <a href="fox.html">Fox Squirrel</a>
        <a href="red.html">Red Squirrel</a>
        <a href="gray.html">Gray Squirrel</a>
        <a href="flying.html">Flying Squirrel</a>
    </nav>
    <main>
        <h1>Flying Squirrel</h1>
        <img src="images/flying.jpg" alt="Flying squirrel">
        <p>Information about flying squirrels.</p>
    </main>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "inf6420-projects\project4\flying.html" -Content $content

# styles/brand.css
$content = @"
=======
"@ | Out-File -FilePath "inf6420-projects/project4/flying.html" -Encoding UTF8

# Styles/brand.css
@"
>>>>>>> Stashed changes
:root {
    --primary-accent: #083B55;
    --secondary-accent: #0A4A6B;
    --link-hover: #FF6B63;
    --text-color: #333;
    --background: #f4f4f4;
    --font-serif: 'Georgia', serif;
    --font-sans: 'Arial', sans-serif;
}

body {
    font-family: var(--font-sans);
    color: var(--text-color);
    background-color: var(--background);
    margin: 0;
    padding: 0;
}

h1, h2, h3 {
    font-family: var(--font-serif);
}

a {
    color: var(--primary-accent);
    text-decoration: none;
}

a:hover {
    color: var(--link-hover);
}

.focus-visible:focus-visible {
    outline: 2px solid var(--link-hover);
}

@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "styles\brand.css" -Content $content

# README.md
$content = @"
=======
"@ | Out-File -FilePath "styles/brand.css" -Encoding UTF8

# README.md
@"
>>>>>>> Stashed changes
# INF6420 Projects

Portfolio of web development projects for INF6420.

## Live Site
http://141.217.120.86/fn9575/html/inf6420-projects/

## Projects
- Project 1: Course Homepage
- Project 2: HTML/CSS Basics
- Project 3: Squirrels Site
- Project 4: Responsive Redesign

## Deployment
<<<<<<< Updated upstream
Use scripts/deploy.ps1 (PowerShell) or scripts/upload_22.py (Python) to upload to WSU server.
"@
Create-FileWithContent -Path "README.md" -Content $content

# submission.html
$content = @"
=======
Use scripts/deploy.ps1 or scripts/upload_22.py to upload to WSU server.
"@ | Out-File -FilePath "README.md" -Encoding UTF8

# Submission.html
@"
>>>>>>> Stashed changes
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Submission Links</title>
</head>
<body>
    <h1>INF6420 Submission</h1>
    <ul>
        <li><a href="http://141.217.120.86/fn9575/html/inf6420-projects/rock-INF6420-index.html">Project 1</a></li>
        <li><a href="http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html">Project 2</a></li>
        <li><a href="http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html">Project 3</a></li>
        <li><a href="http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html">Project 4</a></li>
    </ul>
</body>
</html>
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "submission.html" -Content $content

# Scripts - deploy.ps1
$content = @"
=======
"@ | Out-File -FilePath "submission.html" -Encoding UTF8

# Scripts
@"
>>>>>>> Stashed changes
# deploy.ps1 - SFTP upload to WSU server
# Requires Posh-SSH module: Install-Module -Name Posh-SSH

param(
    [string]$Server = "141.217.120.86",
    [string]$Username = "fn9575",
    [string]$RemotePath = "/html/inf6420-projects/"
)

<<<<<<< Updated upstream
`$Password = Read-Host -AsSecureString "Enter password"
`$Credential = New-Object System.Management.Automation.PSCredential (`$Username, `$Password)

$Session = New-SFTPSession -ComputerName $Server -Credential $Credential
Set-SFTPItem -SessionId $Session.SessionId -Path "." -Destination $RemotePath -Recurse
Remove-SFTPSession -SessionId $Session.SessionId
"@ | Out-File -FilePath "scripts/deploy.ps1" -Encoding UTF8

# upload_22.py
$content = @"
=======
$Password = Read-Host -AsSecureString "Enter password"
$Credential = New-Object System.Management.Automation.PSCredential ($Username, $Password)

$Session = New-SFTPSession -ComputerName $Server -Credential $Credential
Set-SFTPItem -SessionId $Session.SessionId -Path "." -Destination $RemotePath -Recurse
Remove-SFTPSession -SessionId $Session.SessionId
"@ | Out-File -FilePath "scripts/deploy.ps1" -Encoding UTF8

@"
>>>>>>> Stashed changes
# upload_22.py - Python SFTP upload
import paramiko
import os

server = "141.217.120.86"
username = "fn9575"
remote_path = "/html/inf6420-projects/"

password = input("Enter password: ")

transport = paramiko.Transport((server, 22))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

for root, dirs, files in os.walk('.'):
    for file in files:
        local_path = os.path.join(root, file)
        remote_file = os.path.join(remote_path, os.path.relpath(local_path))
        sftp.put(local_path, remote_file)

sftp.close()
transport.close()
<<<<<<< Updated upstream
"@
Create-FileWithContent -Path "scripts\upload_22.py" -Content $content

@"
# package_site.ps1 - Create ZIP for submission
Compress-Archive -Path "." -DestinationPath "dist/inf6420-projects.zip" -Force
"@ | Out-File -FilePath "scripts/package_site.ps1" -Encoding UTF8

Write-Log "INF6420 project structure consolidation and population completed. Add images manually to image folders."
=======
"@ | Out-File -FilePath "scripts/upload_22.py" -Encoding UTF8

@"
# package_site.ps1 - Create ZIP for submission
Compress-Archive -Path "." -DestinationPath "dist/inf6420-projects.zip" -Force
"@ | Out-File -FilePath "scripts/package_site.ps1" -Encoding UTF8

Write-Host "Structure created and files populated. Add images manually to image folders."
>>>>>>> Stashed changes

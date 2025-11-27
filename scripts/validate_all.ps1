# validate_all.ps1 - Open W3C validators for all HTML and CSS files in the project
# Run from the root: C:\Users\k8roc\source\repos\inf6420-projects
# This script finds all .html and .css files, constructs validator URLs, and opens them in the default browser

param(
    [switch]$DryRun  # Show URLs without opening browser
)

$baseUrl = "http://141.217.120.86/fn9575/html/inf6420-projects/"

function Get-ValidatorUrls {
    param([string]$FilePath, [string]$Extension)

    $relativePath = $FilePath.Replace((Get-Location).Path + "\", "").Replace("\", "/")
    $fullUrl = $baseUrl + $relativePath

    if ($Extension -eq ".html") {
        $htmlUrl = "https://validator.w3.org/nu/?doc=" + [System.Web.HttpUtility]::UrlEncode($fullUrl)
        return @($htmlUrl)
    } elseif ($Extension -eq ".css") {
        $cssUrl = "https://jigsaw.w3.org/css-validator/validator?uri=" + [System.Web.HttpUtility]::UrlEncode($fullUrl) + "&profile=css3"
        return @($cssUrl)
    }
    return @()
}

$files = Get-ChildItem -Path . -Recurse -Include "*.html", "*.css" | Where-Object { $_.FullName -notlike "*\node_modules\*" -and $_.FullName -notlike "*\.git\*" }

$urls = @()

foreach ($file in $files) {
    $validatorUrls = Get-ValidatorUrls -FilePath $file.FullName -Extension $file.Extension
    $urls += $validatorUrls
}

Write-Host "Found $($urls.Count) validator URLs for $($files.Count) files."

if ($DryRun) {
    $urls | ForEach-Object { Write-Host $_ }
} else {
    foreach ($url in $urls) {
        Start-Process $url
        Start-Sleep -Milliseconds 500  # Brief pause to avoid overwhelming browser
    }
    Write-Host "Opened all validator URLs in browser."
}
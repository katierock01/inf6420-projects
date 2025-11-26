param(
  [string]$Server = "141.217.120.86",
  [string]$User = "fn9575",
  [string]$RemoteBase = "/home/fn9575/html/inf6420-projects"
)

$ErrorActionPreference = 'Stop'

# Resolve project root (this script is in INF6420-Projects/scripts)
$ProjectRoot = Split-Path -Parent $PSScriptRoot

# Resolve local paths
$localIndex        = Join-Path $ProjectRoot 'index.html'
$localSubmission   = Join-Path $ProjectRoot 'submission.html'
$localBrand        = Join-Path $ProjectRoot 'styles/brand.css'
$localBg           = Join-Path $ProjectRoot 'images/background.svg'
$localLogoIcon     = Join-Path $ProjectRoot 'images/logo-icon.svg'
$localLogoLockup   = Join-Path $ProjectRoot 'images/logo-lockup.svg'
$localP22          = Join-Path $ProjectRoot 'rock-Project2.2/rock-project2-2.html'

# Verify required files exist locally
$required = @(
  $localIndex,
  $localSubmission,
  $localBrand,
  $localBg,
  $localLogoIcon,
  $localLogoLockup,
  $localP22
)

$missing = @()
foreach ($p in $required) { if (-not (Test-Path $p)) { $missing += $p } }
if ($missing.Count -gt 0) {
  Write-Host "Missing local files:" -ForegroundColor Yellow
  $missing | ForEach-Object { Write-Host "  - $_" }
  Write-Host "Continue anyway? (y/N)" -NoNewline
  $ans = Read-Host
  if ($ans -ne 'y') { throw "Aborted due to missing files." }
}

# Try WinSCP first; if missing, fall back to OpenSSH sftp
$winScp = Get-Command 'winscp.com' -ErrorAction SilentlyContinue
if ($winScp) {
  # Build WinSCP script with commands
  $scriptLines = @(
    'option batch on',
    'option confirm off',
    # Accept host key automatically for class server; remove -hostkey=* if you want to pin the key
    "open sftp://$User@$Server -hostkey=*",
    "cd $RemoteBase",
    'mkdir -f images',
    'mkdir -f rock-Project2.2',
    'mkdir -f styles'
  )

  # Upload files (quote paths for spaces)
  $scriptLines += @(
    "put `"$localIndex`"",
    "put `"$localSubmission`"",
    "put `"$localBrand`" styles/",
    "put `"$localBg`" images/",
    "put `"$localLogoIcon`" images/",
    "put `"$localLogoLockup`" images/",
    "put `"$localP22`" rock-Project2.2/"
  )

  # Permissions (best-effort; not all servers honor chmod over SFTP)
  $scriptLines += @(
    'chmod 644 index.html',
    'chmod 644 submission.html',
    'chmod 644 styles/brand.css',
    'chmod 644 images/background.svg',
    'chmod 644 images/logo-icon.svg',
    'chmod 644 images/logo-lockup.svg',
    'chmod 644 rock-Project2.2/rock-project2-2.html',
    'chmod 755 .',
    'chmod 755 images',
    'chmod 755 rock-Project2.2',
    'chmod 755 styles'
  )

  $scriptLines += 'exit'

  # Write temp script and execute
  $tempScript = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), "winscp_upload.txt")
  Set-Content -Path $tempScript -Value ($scriptLines -join "`r`n") -Encoding ASCII

  Write-Host "Running WinSCP script: $tempScript" -ForegroundColor Cyan
  Write-Host "When prompted in the terminal, enter your WSU password and accept the host key (Yes)." -ForegroundColor Green

  & $winScp.Source @("/script=$tempScript")
}
else {
  $sftp = Get-Command 'sftp' -ErrorAction SilentlyContinue
  if (-not $sftp) {
    Write-Host "Neither WinSCP nor OpenSSH sftp is available." -ForegroundColor Red
    Write-Host "Install WinSCP: winget install --id WinSCP.WinSCP -e" -ForegroundColor Cyan
    throw "No SFTP client found."
  }

  # Build OpenSSH sftp batch file (auto-accept new host keys and allow password prompt)
  $batch = @(
    "cd $RemoteBase",
    "mkdir images",
    "mkdir rock-Project2.2",
    "mkdir styles",
    "put `"$localIndex`"",
    "put `"$localSubmission`"",
    "cd styles",
    "put `"$localBrand`"",
    "cd ..",
    "cd images",
    "put `"$localBg`"",
    "put `"$localLogoIcon`"",
    "put `"$localLogoLockup`"",
    "cd ..",
    "cd rock-Project2.2",
    "put `"$localP22`"",
    "cd ..",
    "chmod 644 index.html",
    "chmod 644 submission.html",
    "chmod 644 styles/brand.css",
    "chmod 644 images/background.svg",
    "chmod 644 images/logo-icon.svg",
    "chmod 644 images/logo-lockup.svg",
    "chmod 644 rock-Project2.2/rock-project2-2.html"
  )

  $batchFile = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), "sftp_batch.txt")
  Set-Content -Path $batchFile -Value ($batch -join "`n") -Encoding ASCII

  Write-Host "Running OpenSSH sftp with batch: $batchFile" -ForegroundColor Cyan
  Write-Host "You may be prompted to accept the host key and enter your password." -ForegroundColor Green

  & $sftp.Source @("-o","StrictHostKeyChecking=accept-new","-b", $batchFile, "${User}@${Server}")
}

Write-Host "`nDone. Test these URLs:" -ForegroundColor Green
Write-Host "  Hub:     http://$Server/$User/html/inf6420-projects/index.html"
Write-Host "  Project 2.2: http://$Server/$User/html/inf6420-projects/rock-Project2.2/rock-project2-2.html"

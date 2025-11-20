#!/usr/bin/env python3
"""
Direct upload of Project 1 files to WSU server from local file system.
"""
import subprocess
import tempfile
from pathlib import Path

HOST = "141.217.120.86"
USER = "fn9575"
PASSWORD = "Superposition$2u"
PORT = 22
REMOTE_BASE = f"/home/{USER}/html"

# Local file paths
photo_source = r"C:\Users\k8roc\OneDrive\Desktop\inf6080\lab2-encoding-html\img\example.jpg"
html_source = r"C:\Users\k8roc\OneDrive\Desktop\inf6420-projects\rock-INF6420-index.html"

# Files to upload
files = [
    (photo_source, "myphoto.jpeg"),  # Rename example.jpg to myphoto.jpeg
]

# Create SFTP batch commands
batch_lines = [
    f"cd {REMOTE_BASE}",
    "ls -la"
]

# Add put commands
batch_lines.append(f'put "{photo_source}" myphoto.jpeg')

# If HTML file exists, upload it too
if Path(html_source).exists():
    batch_lines.append(f'put "{html_source}" rock-INF6420-index.html')
else:
    print(f"Note: {html_source} not found, skipping HTML upload")

batch_lines.extend(["ls -la", "bye"])

# Write batch file
batch_content = "\n".join(batch_lines)
tmp_batch = Path(tempfile.gettempdir()) / "sftp_direct_upload.txt"
tmp_batch.write_text(batch_content, encoding="utf-8")

print("=" * 60)
print("Direct Upload to WSU Server")
print("=" * 60)
print(f"\nUploading from:")
print(f"  Photo: {photo_source}")
print(f"\nTo: {HOST}:{REMOTE_BASE}")
print(f"  As: myphoto.jpeg\n")

# Run sftp
cmd = ["sftp", "-b", str(tmp_batch), "-P", str(PORT), f"{USER}@{HOST}"]

try:
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = proc.communicate(input=f"{PASSWORD}\n", timeout=30)
    
    print(stdout)
    if stderr and "sftp>" not in stderr:
        print(f"Warnings: {stderr}")
    
    if proc.returncode == 0:
        print("\n✅ Upload complete!")
        print(f"\n🌐 Test at:")
        print(f"   http://{HOST}/{USER}/html/rock-INF6420-index.html")
    else:
        print(f"\n❌ Upload failed with code {proc.returncode}")
        
except Exception as e:
    print(f"\n❌ Error: {e}")
finally:
    if tmp_batch.exists():
        tmp_batch.unlink()

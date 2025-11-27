#!/usr/bin/env python3
"""
Package INF6420 projects for distribution
Creates a clean zip file excluding development files
"""
import os
import shutil
import zipfile
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
DIST_DIR = PROJECT_ROOT / "dist"

# Files and directories to exclude
EXCLUDE_PATTERNS = {
    '.git',
    '.github',
    '.venv',
    '__pycache__',
    'node_modules',
    '*.pyc',
    '.gitignore',
    'deploy-ai.py',
    'cleanup_inf6420.py',
    'audit_layout.py',
    'winscp-upload.ps1',
    'upload-guide.ps1',
    'dist',
    '*.tmp',
    '*.log'
}

def should_exclude(path, root):
    """Check if path should be excluded"""
    rel_path = path.relative_to(root)
    
    # Check each part of the path
    for part in rel_path.parts:
        if part in EXCLUDE_PATTERNS:
            return True
        # Check wildcard patterns
        if part.startswith('.') and part != '.':
            return True
    
    # Check file extensions
    if path.is_file():
        if any(path.match(pattern) for pattern in EXCLUDE_PATTERNS if '*' in pattern):
            return True
    
    return False

def create_package():
    """Create distribution package"""
    print("📦 Creating INF6420 Projects Package\n")
    
    # Create dist directory
    DIST_DIR.mkdir(exist_ok=True)
    
    # Generate package name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = f"inf6420-projects_{timestamp}.zip"
    package_path = DIST_DIR / package_name
    
    print(f"Package: {package_name}")
    print(f"Output: {package_path}\n")
    
    # Create zip file
    file_count = 0
    with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PROJECT_ROOT):
            root_path = Path(root)
            
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not should_exclude(root_path / d, PROJECT_ROOT)]
            
            for file in files:
                file_path = root_path / file
                
                # Skip excluded files
                if should_exclude(file_path, PROJECT_ROOT):
                    continue
                
                # Add to zip
                arcname = file_path.relative_to(PROJECT_ROOT)
                zipf.write(file_path, arcname)
                file_count += 1
                print(f"  ✓ {arcname}")
    
    # Get package size
    size_mb = package_path.stat().st_size / (1024 * 1024)
    
    print(f"\n✅ Package created successfully!")
    print(f"  Files: {file_count}")
    print(f"  Size: {size_mb:.2f} MB")
    print(f"  Location: {package_path}")
    
    return package_path

def main():
    try:
        package_path = create_package()
        
        print("\n📋 Next steps:")
        print(f"  1. Extract and review: {package_path}")
        print("  2. Upload to WSU server via OwlFiles")
        print("  3. Verify deployment at WSU web server")
        
        return 0
    except Exception as e:
        print(f"\n❌ Error creating package: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())

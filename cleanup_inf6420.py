#!/usr/bin/env python3
"""
Cleanup script for INF6420 projects
Reorganizes files into canonical layout and removes legacy folders
"""
import os
import shutil
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent

# Canonical structure
CANONICAL_DIRS = [
    "rock-Project1",
    "rock-Project2.1",
    "rock-Project2.2",
    "rock-Project2.3",
    "rock-Project3",
    "docs",
    "images",
    "styles",
    "scripts"
]

# Files that should be excluded from WSU uploads
EXCLUDED_FILES = {
    ".git",
    ".github",
    ".venv",
    "__pycache__",
    ".gitignore",
    "deploy-ai.py",
    "cleanup_inf6420.py",
    "audit_layout.py",
    "winscp-upload.ps1",
    "upload-guide.ps1"
}

def ensure_canonical_structure():
    """Create canonical directory structure"""
    print("📁 Creating canonical directory structure...")
    for dir_name in CANONICAL_DIRS:
        dir_path = PROJECT_ROOT / dir_name
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ Created: {dir_name}/")
        else:
            print(f"  ⚠ Exists: {dir_name}/")

def create_project_readme(project_dir):
    """Create README template for project directories"""
    readme_path = project_dir / "README.md"
    if not readme_path.exists():
        project_name = project_dir.name
        content = f"""# {project_name}

## Overview
<!-- Describe what this project does -->

## Files
<!-- List key files and their purpose -->

## How to Run
<!-- Instructions for running/viewing this project -->

## Requirements
<!-- Dependencies, if any -->

## Notes
<!-- Any additional information -->
"""
        readme_path.write_text(content, encoding='utf-8')
        print(f"  ✓ Created README in {project_name}/")

def cleanup_legacy_folders():
    """Remove legacy or temporary folders"""
    legacy_patterns = [
        "old_*",
        "backup_*",
        "temp_*",
        "tmp_*",
        "*_old"
    ]
    
    print("\n🧹 Cleaning up legacy folders...")
    for pattern in legacy_patterns:
        for path in PROJECT_ROOT.glob(pattern):
            if path.is_dir():
                print(f"  🗑 Removing: {path.name}/")
                shutil.rmtree(path)

def main():
    print("🚀 INF6420 Project Cleanup Starting...\n")
    
    # Step 1: Create canonical structure
    ensure_canonical_structure()
    
    # Step 2: Create README templates
    print("\n📝 Creating README templates...")
    for dir_name in CANONICAL_DIRS:
        if dir_name.startswith("rock-Project"):
            create_project_readme(PROJECT_ROOT / dir_name)
    
    # Step 3: Cleanup legacy folders
    cleanup_legacy_folders()
    
    print("\n✅ Cleanup complete!")
    print("\nNext steps:")
    print("  1. Review the canonical structure")
    print("  2. Move project files into appropriate directories")
    print("  3. Run audit_layout.py to validate")

if __name__ == "__main__":
    main()

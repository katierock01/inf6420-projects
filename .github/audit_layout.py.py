import os

EXPECTED = {
    "rock-INF6420-index.html": "file",
    "img": "dir",
    "inf6420-projects": {
        "rock-project2.1.docx": "file",
        "rock-project2-2.html": "file",
        "project3": {
            "home.html": "file", "fox.html": "file", "red.html": "file",
            "gray.html": "file", "flying.html": "file",
            "squirrels.css": "file", "showform.php": "file", "images": "dir",
        },
        "project4": {
            "home.html": "file", "fox.html": "file", "red.html": "file",
            "gray.html": "file", "flying.html": "file",
            "squirrels-responsive.css": "file", "images": "dir",
        },
        # Add "6420-final" when you start the final project
    },
}

OBSOLETE = [
    "project1.1", "project2.1", "project2.2", "project3",
    "rock-Project1.1", "rock-Project2.1", "rock-Project2.2", "rock-Project2.3"
]

def walk_project(base, structure, missing):
    for name, kind in structure.items():
        path = os.path.join(base, name)
        if isinstance(kind, dict):
            if not os.path.isdir(path):
                missing.append(f"Missing directory: {path}")
            else:
                walk_project(path, kind, missing)
        else:
            if not os.path.isfile(path):
                missing.append(f"Missing file: {path}")

def main():
    missing, legacy = [], []
    walk_project(os.getcwd(), EXPECTED, missing)
    legacy = [d for d in OBSOLETE if os.path.exists(d)]
    print("Directory tree:\n")
    for root, dirs, files in os.walk(".", topdown=True):
        indent = "  " * root.count(os.sep)
        print(f"{indent}{os.path.basename(root)}/")
        for f in files:
            print(f"{indent}  {f}")
    print("\nAudit report:")
    if missing:
        print("Missing items:")
        for m in missing: print(" -", m)
    if legacy:
        print("Obsolete folders:")
        for l in legacy: print(" -", l)
    if not missing and not legacy:
        print("No structural issues detected.")

if __name__ == "__main__":
    main()

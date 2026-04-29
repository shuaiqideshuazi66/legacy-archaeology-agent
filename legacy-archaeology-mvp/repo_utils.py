import os

def scan_repo(repo_path, exts=(".py", ".js", ".java")):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for name in filenames:
            if name.endswith(exts):
                path = os.path.join(root, name)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        files.append({
                            "path": path,
                            "content": f.read()
                        })
                except Exception:
                    pass
    return files

#!/usr/bin/env python
"""KnowledgeOS Diagnostic & Health Doctor.

Validates the local environment, Python runtime version, folder structure,
git capability, and Notion keys before initializing the system.
"""
from __future__ import annotations
import os, sys
from pathlib import Path

VAULT_DIR = Path(__file__).resolve().parent.parent
DB = VAULT_DIR / "knowledge_index.db"

def main():
    print("=== KnowledgeOS Environment Diagnostic Doctor ===")
    print(f"Vault Root: {VAULT_DIR}\n")
    
    passed = True

    # 1. Check Python Version
    py_ver = sys.version_info
    print(f"[*] Checking Python version...")
    if py_ver.major < 3 or (py_ver.major == 3 and py_ver.minor < 9):
        print(f"  [ERROR] Python version is {py_ver.major}.{py_ver.minor}. KnowledgeOS requires Python 3.9+ for typing annotations.")
        passed = False
    else:
        print(f"  [OK] Python {py_ver.major}.{py_ver.minor}.{py_ver.micro} detected.")

    # 2. Check Directory Structure
    required_dirs = ["Inbox", "Concepts", "Projects", "Experiments", "Research", "Decisions", "People", "MOCs", "Templates"]
    print(f"\n[*] Checking folder structure...")
    missing_dirs = []
    for d in required_dirs:
        p = VAULT_DIR / d
        if not p.exists():
            missing_dirs.append(d)
    
    if missing_dirs:
        print(f"  [WARNING] Missing directories: {', '.join(missing_dirs)}.")
        print(f"            Creating missing directories now...")
        for d in missing_dirs:
            (VAULT_DIR / d).mkdir(parents=True, exist_ok=True)
        print(f"  [OK] Folder structure initialized.")
    else:
        print(f"  [OK] All core vault directories are present.")

    # 3. Check Git Status
    print(f"\n[*] Checking Git configuration...")
    git_dir = VAULT_DIR / ".git"
    if not git_dir.exists():
        print("  [WARNING] Git repository is not initialized. Run 'git init' to track cognitive drift.")
    else:
        import subprocess
        try:
            subprocess.run(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("  [OK] Git is installed and initialized.")
        except Exception:
            print("  [WARNING] Git command line utility was not found in PATH.")

    # 4. Check Database Status
    print(f"\n[*] Checking SQLite Database index...")
    if not DB.exists():
        print(f"  [WARNING] 'knowledge_index.db' is missing. You need to run 'python scripts/rebuild_index.py' to generate it.")
    else:
        size = DB.stat().st_size
        print(f"  [OK] SQLite index found ({size} bytes).")

    # 5. Check Notion API Config
    print(f"\n[*] Checking Notion API keys...")
    local_app_data = os.environ.get("LOCALAPPDATA")
    candidates = [
        os.path.expanduser("~/.hermes/.env"),
    ]
    if local_app_data:
        candidates.append(os.path.join(local_app_data, "hermes", ".env"))
    
    env_found = False
    for path in candidates:
        if os.path.exists(path):
            env_found = True
            break
            
    if os.environ.get("NOTION_API_KEY") or env_found:
        print("  [OK] Notion API Key configuration detected.")
    else:
        print("  [INFO] Notion environment keys are not configured. Notion sync will run in dry-run mode.")

    print("\n--- Diagnostic Summary ---")
    if passed:
        print("[OK] System environment check PASSED. KnowledgeOS is ready for use!")
    else:
        print("[FAIL] System environment check FAILED. Please resolve errors above.")

if __name__ == "__main__":
    main()

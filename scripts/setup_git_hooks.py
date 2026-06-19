#!/usr/bin/env python
"""Setup Git Hooks for KnowledgeOS.

This script creates a local pre-commit hook in the .git/hooks/ directory
to automatically run the schema validator prior to saving any commits.
"""
import os
import sys
from pathlib import Path

VAULT_DIR = Path(__file__).resolve().parent.parent
HOOKS_DIR = VAULT_DIR / ".git" / "hooks"


def main() -> int:
    if not HOOKS_DIR.parent.exists():
        print("❌ Error: Not a Git repository (missing .git/ directory).")
        return 1

    HOOKS_DIR.mkdir(parents=True, exist_ok=True)
    hook_file = HOOKS_DIR / "pre-commit"

    hook_content = """#!/bin/sh
# Run KnowledgeOS schema validation before allowing a commit
echo "🩺 Running KnowledgeOS pre-commit schema validation..."
python scripts/validate_schema.py
EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
  echo "❌ Git Commit Aborted: KnowledgeOS schema validation failed."
  exit $EXIT_CODE
fi
"""

    print(f"[*] Writing pre-commit hook to {hook_file}...")
    hook_file.write_text(hook_content, encoding="utf-8")

    # Set execution permissions (Linux/macOS)
    if os.name == "posix":
        try:
            status = hook_file.stat()
            os.chmod(hook_file, status.st_mode | 0o111)
            print("[OK] Execution permission set.")
        except Exception as e:
            print(f"[WARNING] Could not set execution permission: {e}")

    print("[OK] Git pre-commit hook setup successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

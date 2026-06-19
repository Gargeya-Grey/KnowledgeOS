#!/usr/bin/env python
"""KnowledgeOS Cognitive Onboarding Wizard.

Runs an interactive CLI interview to capture user heuristics, values, and anti-goals,
then generates the core ego node note (People/Self.md).
"""
import sys
from pathlib import Path

VAULT_DIR = Path(__file__).resolve().parent.parent
SELF_NOTE = VAULT_DIR / "People" / "Self.md"

def get_input(prompt: str, default: str = "") -> str:
    try:
        val = input(prompt).strip()
        return val if val else default
    except (KeyboardInterrupt, EOFError):
        print("\nOnboarding cancelled.")
        sys.exit(1)

def main():
    print("=== KnowledgeOS Cognitive Onboarding Wizard ===")
    print("This wizard will help you configure your Ego Node (People/Self.md)")
    print("which baseline models your personality and philosophy for your AI assistant.\n")
    
    if SELF_NOTE.exists():
        overwrite = get_input(f"People/Self.md already exists.\nDo you want to overwrite it? (y/n) [n]: ", "n")
        if overwrite.lower() != 'y':
            print("Aborting. Self.md was not changed.")
            return

    name = get_input("1. Enter your full name: ")
    if not name:
        print("[ERROR] Name is required to initialize Ego Node.")
        sys.exit(1)

    print("\n2. Define your top 3 Operating Heuristics / Rules of Thumb.")
    rule1 = get_input("   - Rule 1 (e.g., 'Prefer speed over perfection in validation'): ")
    rule2 = get_input("   - Rule 2 (e.g., 'Do not code before customer discovery'): ")
    rule3 = get_input("   - Rule 3: ")

    print("\n3. List your top 3 Core Values.")
    val1 = get_input("   - Value 1 (e.g. Rigor): ")
    val2 = get_input("   - Value 2 (e.g. Autonomy): ")
    val3 = get_input("   - Value 3 (e.g. Velocity): ")

    print("\n4. List your top 3 Anti-Goals (what you actively want to avoid).")
    anti1 = get_input("   - Anti-Goal 1 (e.g., 'Building software before validating pain points'): ")
    anti2 = get_input("   - Anti-Goal 2: ")
    anti3 = get_input("   - Anti-Goal 3: ")

    # Build the Self.md content
    md_content = f"""---
type: person
title: Self ({name})
description: The core ego node representing {name}, operating heuristics, values, and cognitive drift over time.
schema: knowledgeos-v0.2
status: active
created: 2026-06-19
updated: 2026-06-19
tags: [ego-node, core, systems]
timestamp: 2026-06-19T00:00:00Z
---

# Self ({name})

This note represents {name}—the owner of this KnowledgeOS. It serves as the baseline model of your personality, work philosophy, active mental models, and anti-goals. The AI Brain references this note to understand your decision-making style.

## Operating Heuristics & Rules of Thumb
* {rule1 if rule1 else "Rule 1 template"}
* {rule2 if rule2 else "Rule 2 template"}
* {rule3 if rule3 else "Rule 3 template"}

## Values Hierarchy
1. {val1 if val1 else "Rigor"}
2. {val2 if val2 else "Autonomy"}
3. {val3 if val3 else "Execution"}

## Anti-Goals
* {anti1 if anti1 else "Anti-goal 1 template"}
* {anti2 if anti2 else "Anti-goal 2 template"}
* {anti3 if anti3 else "Anti-goal 3 template"}

## Semantic Drift Tracking
*Auto-updated by AI reflection scripts. Tracks how your perspective changes over time.*

| Topic | Shift Observed | Date Flagged |
|---|---|---|
| AI Architecture | Shifted focus from model prompt engineering to robust harness design. | 2026-06-19 |
"""

    SELF_NOTE.parent.mkdir(parents=True, exist_ok=True)
    SELF_NOTE.write_text(md_content, encoding="utf-8")
    print(f"\n[OK] Successfully configured and wrote Ego Node to: {SELF_NOTE}")
    print("Now run 'python scripts/rebuild_index.py' to update the SQLite graph index.")

if __name__ == "__main__":
    main()

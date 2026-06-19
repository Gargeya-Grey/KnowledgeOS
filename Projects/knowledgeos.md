---
type: project
title: KnowledgeOS
description: Project hub for KnowledgeOS.
schema: knowledgeos-v0.2
status: active
created: 2026-06-18
tags: [knowledgeos, systems, obsidian, hermes]
project: KnowledgeOS
updated: 2026-06-18
timestamp: 2026-06-18T00:00:00Z
---
# KnowledgeOS

## Objective
Turn the current Obsidian/Hermes vault from a scaffold into a living personal operating system for learning, startup planning, research, and productive work.

## Success Criteria
- Daily capture is easy.
- Weekly synthesis produces useful decisions/actions.
- Active projects are visible from one dashboard.
- Notes reliably connect to domains and projects.
- Scripts work without environment-specific CLI dependencies.
- Role boundaries between Obsidian/Notion/Hermes are documented.
- Template library covers startup, learning, execution, and research.

## Current State
The KnowledgeOS has been upgraded through a complete 5-step strategic build:
- Step 1 (Audit) — Found scaffold issues, placeholder indexes, sqlite3 dependency, hardcoded token, missing project layer.
- Step 2 (Design) — Added domain MOCs, operating loop, active projects, README overhaul.
- Step 3 (Templates) — 26 templates across startup, learning, research, execution.
- Step 4 (Automation) — 9 scripts covering index, search, weekly data, capture, refinement, experiments dashboard, drafting, MOC updates.
- Step 5 (Execution System) — Role boundaries document, execution MOC, operating cadence, decision log.

## Related Knowledge
- [KnowledgeOS MOC](../MOCs/_MOC_KnowledgeOS.md)
- [Execution System MOC](../MOCs/_MOC_Execution_System.md)
- [KnowledgeOS README](../README.md)
- [Active Work MOC](../MOCs/_MOC_Active.md)
- [Template Index](../Templates/_Index.md)
- [Role Boundaries Decision](../Decisions/obsidian-notion-hermes-role-boundaries.md)
- [Refinement Bar Decision](../Decisions/refinement-bar-for-notion-publishing.md)

## Next Actions
- Run `python scripts/rebuild_index.py` to index the vault.
- Review [Experiments Dashboard](../MOCs/_MOC_Experiments.md).
- Explore templates in [Templates Index](../Templates/_Index.md) to start creating notes.

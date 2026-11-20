# PR/MR Description Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the first engineering skill, producing concise PR/MR descriptions grounded in intent, recorded insights, and existing evidence.

**Architecture:** A self-contained, portable `SKILL.md` uses available host tools. A small examples reference clarifies output decisions without adding scripts or dependencies. Existing plugin discovery picks up the skill automatically.

**Tech Stack:** Markdown with simple YAML frontmatter; existing Python repository validator and Claude plugin validator.

**Spec:** `docs/superpowers/specs/2026-11-20-pr-description-design.md` (approved in chat).

## Global Constraints

- Use the applicable repository template’s structure.
- Include implementation insights only when explicitly recorded during implementation, always as bullet points.
- Reuse evidence gathered during implementation.
- Identify missing, failed, inaccessible, or stale evidence and still produce a draft.
- Return a reviewable draft by default.
- Create or update a PR/MR description only on an explicit publishing request.
- No dedicated integration scripts or dependencies initially.
- Running verification, spawning verification subagents, and capturing screenshots belong to a separate future skill.

## Review Focus

1. A source is inaccessible or the why is unresolved: disclose the gap, ask a focused question, and supply a qualified draft without invented motivation.
2. An applicable template requires otherwise optional sections: retain its structure without invented insights or checked-off tests.
3. Evidence comes from a previous revision or contains failures: retain its limits instead of claiming current success.
4. Screenshots exist only locally or diagrams cannot render: offer usable references/fallback prose without fabricated uploads or runtime proof.
5. Publishing was requested but hosting tools are unavailable: return the final draft and explain that publishing did not occur.

## Files and Responsibilities

- Create `plugins/engineering/skills/pr-description/SKILL.md`: discovery metadata, context collection, writing criteria, evidence handling, and explicit publishing behavior.
- Create `plugins/engineering/skills/pr-description/references/examples.md`: three illustrative cases showing template fidelity, recorded insights, and evidence gaps. Load only when an example helps.
- Modify `plugins/engineering/README.md`: skill index, usage examples, and verification boundaries.
- Modify `README.md`, `AGENTS.md`, and `docs/compatibility.md`: replace obsolete empty-scaffold claims and accurately distinguish packaging checks from behavioral exercises.
- Modify `CHANGELOG.md`: add the skill under Unreleased.
- Modify the design status to reflect approval. Remove `plugins/engineering/skills/.gitkeep` once the directory has content.
- Create `docs/validation/pr-description.md`: authoring exercise outcomes and actual checks, with host/version and limitations clearly identified.

## Task 1: Author, integrate, and validate the skill

**Interfaces:** Consumes the approved design, the project’s simple frontmatter convention, and the existing `skills/` discovery layout. Produces one discoverable skill named `pr-description`; no manifest changes are needed.

- [x] **Step 1: Define behavioral exercises before authoring.** In the validation record, describe the raw context and observable acceptance criteria for: a template-backed frontend change with recorded screenshots; a backend change without a template or recorded insights; missing evidence with an unresolved why; stale/failed checks in a required template; explicit publishing with unavailable host tools. Cover all five Review Focus conditions. Do not require exact wording or fixed length.
- [x] **Step 2: Write the skill and examples.** Keep frontmatter to `name` and a discriminating single-line `description`. Collect the target/base, applicable template, conversation and implementation records, linked tickets and supporting references, commit history, and diff. Ask only for unresolved material intent. Preserve recorded evidence provenance. Explain diagrams vs proof, screenshot reuse, concise runnable references, and limitations. On explicit publishing, write only the requested description, preserve relevant existing authored content, read back the resulting description, and report its URL. An unavailable integration returns a draft without claiming publication.
- [x] **Step 3: Update discovery documentation.** Add example requests for drafting and explicitly updating an existing PR/MR. Remove empty-scaffold claims while retaining untested-host qualifications. Link the examples reference from the skill; keep evaluation records outside the installed package. Record design approval without inventing a dated release.
- [x] **Step 4: Exercise the five scenarios.** Use synthetic inputs without network calls, real publication, checks, or screenshots. With native execution, do a transparent author self-review and record concrete resulting drafts/decisions as illustrative walkthroughs, not independent behavioral tests. With subagent execution, provide the skill and raw fixtures to a fresh agent and record observed outputs. In either method, fix only demonstrated failures and disclose the method and its limits.
- [x] **Step 5: Run structural checks.** Run `python3 scripts/validate.py` (expect one plugin and one skill), `claude plugin validate .` (marketplace), `claude plugin validate plugins/engineering` (plugin), and `git diff --check`. A missing listing icon is an existing nonblocking warning; document it rather than adding branding. Review changed files against the approved design and ensure example-only claims have not entered public capability statements.
- [x] **Step 6: Report the result.** Link the skill and validation record; distinguish actual structural checks from synthetic exercises and untested host installation. Do not publish PR/MR descriptions, commit, or push unless requested.

## Plan Self-Review

The single task covers every design behavior, supporting docs, and validation. The Review Focus conditions are assigned to the scenario exercise step. No new executable interface, dependency, host-specific syntax, or verification skill is introduced. The plan is ready for execution-method selection.


## Execution record

Completed using native execution in the existing checkout. The skill and examples were authored directly; this change adds no executable code, so validation used drafting walkthroughs and structural checks rather than tests of generated wording. One fresh read-only reviewer identified two issues, both corrected: ambiguous publication authorization and an unsupported result in an example. See `docs/validation/pr-description.md` for outputs, actual check results, and limitations. No commit, push, or remote description publication was performed.

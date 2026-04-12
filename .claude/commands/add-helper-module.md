---
name: add-helper-module
description: Workflow command scaffold for add-helper-module in wireless-toolkit.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-helper-module

Use this workflow when working on **add-helper-module** in `wireless-toolkit`.

## Goal

Adds a new helper or utility module to extend toolkit functionality (e.g., notes, teaching, weak point review).

## Common Files

- `modules/*_helper.py`
- `modules/weak_point_review.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create a new Python file in the modules/ directory implementing the helper logic.
- Commit the new file with a descriptive message.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.
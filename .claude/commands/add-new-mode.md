---
name: add-new-mode
description: Workflow command scaffold for add-new-mode in wireless-toolkit.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-new-mode

Use this workflow when working on **add-new-mode** in `wireless-toolkit`.

## Goal

Adds a new user workflow mode to the toolkit, such as Easy, Guided, or Advanced mode.

## Common Files

- `modes/*.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create a new Python file in the modes/ directory implementing the new mode.
- Commit the new file with a message describing the mode.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.
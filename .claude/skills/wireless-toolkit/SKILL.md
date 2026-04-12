```markdown
# wireless-toolkit Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill teaches you how to contribute to the `wireless-toolkit` Python codebase, focusing on its development conventions and main workflows. The toolkit is modular, extensible, and organized for collaborative development. You'll learn how to add new user modes, extend functionality with helper modules, and iteratively improve core features like report generation—all while following the project's coding and commit style.

## Coding Conventions

- **Language:** Python (no framework)
- **File Naming:** Use `snake_case` for all file and directory names.
  - Example: `weak_point_review.py`, `report_generator.py`
- **Import Style:** Use relative imports within modules.
  ```python
  from .notes_helper import NotesHelper
  ```
- **Export Style:** Use named exports (define classes, functions, or variables explicitly).
  ```python
  def generate_report(data):
      ...
  ```
- **Commit Messages:** Freeform, concise (average ~33 characters). Describe the change clearly.
  - Example: `add guided mode for user workflow`

## Workflows

### Add New Mode
**Trigger:** When you want to introduce a new way for users to interact with the toolkit (e.g., Easy, Guided, Advanced modes).  
**Command:** `/new-mode`

1. Create a new Python file in the `modes/` directory implementing the new mode.
   - Example: `modes/guided_mode.py`
2. Implement the mode logic as a class or set of functions.
   ```python
   # modes/guided_mode.py
   class GuidedMode:
       def start(self):
           print("Welcome to Guided Mode!")
   ```
3. Commit the new file with a message describing the mode.
   - Example: `add guided mode for user workflow`

---

### Add Helper Module
**Trigger:** When you want to add a new helper or utility feature (e.g., notes, teaching, weak point review).  
**Command:** `/new-helper`

1. Create a new Python file in the `modules/` directory, named with a `_helper.py` suffix if appropriate.
   - Example: `modules/notes_helper.py`
2. Implement the helper logic.
   ```python
   # modules/notes_helper.py
   def add_note(note):
       # logic to add a note
       pass
   ```
3. Commit the new file with a descriptive message.
   - Example: `add notes helper module`

---

### Update Report Generator
**Trigger:** When you need to enhance or fix the report generation process.  
**Command:** `/update-report`

1. Edit `modules/report_generator.py` to implement your changes.
   ```python
   # modules/report_generator.py
   def generate_report(data):
       # improved logic here
       pass
   ```
2. Commit the updated file with a relevant message.
   - Example: `fix report formatting bug`

---

## Testing Patterns

- **Framework:** Not explicitly detected.
- **Test File Pattern:** Test files are named with `.test.` in the filename.
  - Example: `modules/test_report_generator.test.py`
- **Writing Tests:** Place test files alongside modules or in a dedicated test directory. Use standard Python testing practices (e.g., `assert` statements).
  ```python
  # modules/test_report_generator.test.py
  from .report_generator import generate_report

  def test_generate_report():
      result = generate_report({'input': 1})
      assert result is not None
  ```

## Commands

| Command        | Purpose                                                |
|----------------|--------------------------------------------------------|
| /new-mode      | Add a new user workflow mode to the toolkit            |
| /new-helper    | Add a new helper or utility module                     |
| /update-report | Improve or fix the report generation logic             |
```

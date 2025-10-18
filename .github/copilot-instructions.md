# Copilot instructions for simple_clock

This repository is a tiny Python GUI application that shows a digital clock using Tkinter.  Keep suggestions and edits focused, minimal, and runnable on a standard Windows or Linux machine with Python and Tkinter installed.


What this app is
- Single-file Tkinter application: `reloj.py` (Spanish variable names: `ventana`, `etiqueta_reloj`, `actualizar_reloj`).
- Purpose: display current time in HH:MM:SS and update every second.

How to run
- Run directly with Python 3 that has Tkinter available:
  - python3 reloj.py

Key patterns and conventions
- Uses procedural single-file structure (no packages or modules).
- UI updates use `widget.after(ms, func)` to schedule periodic updates (see `etiqueta_reloj.after(1000, actualizar_reloj)`).
- Variables and function names are in Spanish; keep translations consistent when adding code (e.g., `ventana`, `etiqueta_reloj`).
- No external dependencies beyond the Python standard library.

What to change carefully
- Avoid restructuring into complex packages unless you also add an entrypoint and update run instructions.
- Preserve the `after`-based update loop for UI responsiveness; avoid blocking calls in the main thread.

Helpful edits to propose
- Small, incremental improvements: add command-line options (24h/12h), skin/theme options, or a simple settings JSON file.
- Tests are not required for UI behavior, but if adding code logic separate from UI (time formatting, settings parsing), include unit tests using `unittest`.

Files to inspect for context
- `reloj.py` — main and only source file.

Edge cases discovered
- No error handling for missing Tkinter; detect import errors and show a friendly message.
- No packaging or dependency file.

If you need clarification
- Ask where to place additional files (tests, settings) and whether to translate identifiers to English or preserve Spanish names.

Keep suggested PRs small and demonstrable: include a short README, a small test for non-UI logic, and brief run instructions if adding new files.
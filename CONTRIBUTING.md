# Contributing

Vowline is intentionally small. Contributions should improve clarity, compatibility, safety, or verification without turning the skill into a prompt stack.

## Principles

- Keep `skills/vowline/SKILL.md` concise, general, and outcome-first.
- Prefer decision rules over long procedures.
- Do not add tool-specific behavior unless it improves a documented harness adapter or is isolated in compatibility documentation.
- Preserve the side-effect boundary: no deploy, publish, purchase, messaging, production mutation, deletion, or credential rotation without explicit user approval.
- Add or update tests when changing installers, uninstallers, markers, path handling, or verification behavior.
- Keep public docs direct. Avoid hype, long theory, or claims a host runtime cannot guarantee.

## Checks

Run before opening a pull request:

```bash
python3 -m py_compile install.py uninstall.py
python3 -m unittest discover -s tests
```

## Pull request shape

A useful pull request states:

1. The problem.
2. The minimal change.
3. The checks run.
4. Any compatibility impact for supported harnesses.

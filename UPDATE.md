# Update Vowline

This guide is written for AI agents and humans updating an existing Vowline install. Updating means replacing the installed Vowline-owned skill directories and marked bridge blocks with the latest version from this repository.

You do not need a separate updater. The installer is intentionally idempotent: running the relevant install steps again from the latest repository updates existing installs while preserving unrelated user and project instructions.

## Agent Update Contract

If you are an AI agent asked to update Vowline, use this repository as source material:

```text
skills/vowline/
guidance/
```

Do not only update one `SKILL.md`. A correct update refreshes each selected Vowline-owned skill directory and each selected host bridge file.

For each selected harness:

```text
copy latest skills/vowline -> the installed vowline skill directory
replace the existing <!-- vowline:start --> block with the latest guidance file
write generated rule files again where the host uses generated rules
verify the selected install targets
```

Preserve unrelated content before and after marked blocks. If no Vowline block exists, append one. If an older compact Vowline block exists, replace it with the current block.

## Choose Scope

Use the same harness scope that was originally installed unless the user asks to narrow or expand it.

Common scopes:

```text
codex       Update only Codex locations.
core        Update Codex, Claude Code, Windsurf, Cursor, Gemini CLI, and GitHub Copilot.
all         Update core plus community SKILL.md targets.
```

If a user is not sure what they installed, `core` is usually the practical default for mainstream agent hosts. Use `all` only when they want every supported target refreshed.

## Update Yourself

Ask the agent to update its own user-level install:

```text
Update Vowline for yourself by following https://github.com/chojondocho/vowline/blob/main/UPDATE.md. Verify the update.
```

If using the optional script from a fresh clone or pulled checkout:

```bash
git pull
python3 install.py global --harnesses core
python3 install.py verify-global --harnesses core
```

For Codex-only global updates:

```bash
git pull
python3 install.py global --harnesses codex
python3 install.py verify-global --harnesses codex
```

## Update A Project

Ask from inside the project:

```text
Update Vowline in this project by following https://github.com/chojondocho/vowline/blob/main/UPDATE.md. Use project-local paths. Verify the update.
```

If using the optional script from a fresh clone or pulled checkout:

```bash
git pull
python3 install.py project /path/to/project --harnesses core
python3 install.py verify /path/to/project --harnesses core
```

For Codex-only project updates:

```bash
git pull
python3 install.py project /path/to/project --harnesses codex
python3 install.py verify /path/to/project --harnesses codex
```

## Codex Expected State

For Codex global updates, the documented required state is:

```text
~/.agents/skills/vowline/SKILL.md exists and matches the latest skills/vowline/SKILL.md
${CODEX_HOME:-~/.codex}/AGENTS.md contains exactly one current Vowline marked block
```

Recommended compatibility mirror:

```text
${CODEX_HOME:-~/.codex}/skills/vowline/SKILL.md exists when that Codex environment uses CODEX_HOME/skills
```

For Codex project updates, the expected state is:

```text
/path/to/project/.agents/skills/vowline/SKILL.md exists and matches the latest skills/vowline/SKILL.md
/path/to/project/AGENTS.md contains exactly one current Vowline marked block
```

## Verification

At minimum, report:

```text
updated skill directories
updated bridge files or generated rule files
verification command and result
any selected target that was absent, skipped, or not writable
```

Useful checks:

```bash
python3 install.py verify-global --harnesses core
python3 install.py verify /path/to/project --harnesses core
```

When exact content matching matters, compare the installed skill against the current source:

```bash
diff -qr skills/vowline ~/.agents/skills/vowline
```

For Codex, also confirm the bridge file contains exactly one Vowline block:

```bash
grep -c '<!-- vowline:start -->' "${CODEX_HOME:-$HOME/.codex}/AGENTS.md"
grep -c '<!-- vowline:end -->' "${CODEX_HOME:-$HOME/.codex}/AGENTS.md"
```

## Notes

- Updating does not remove unrelated user instructions.
- Updating does not grant permission to deploy, publish, commit, push, send messages, mutate production data, or take other externally visible action.
- Updating a narrower harness scope leaves unselected old Vowline copies untouched. Run the update with the same or broader `--harnesses` scope if you want every previous target refreshed.
- To remove Vowline instead of updating it, follow [UNINSTALL.md](UNINSTALL.md).

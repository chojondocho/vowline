# Uninstall Vowline

This guide is written for AI agents and humans removing Vowline. The goal is complete removal of Vowline-owned files without touching unrelated user instructions.

You do not need to clone this repository or run a script when you can edit the filesystem directly. The scripts are optional helpers that perform the same deletion and verification steps.

## Agent Uninstall Contract

Do not only delete one skill directory. Vowline may be installed in multiple skill locations and may also have marked bridge blocks in host instruction files.

Remove only Vowline-owned skill directories named:

```text
vowline
```

Remove only marked Vowline instruction blocks:

```text
<!-- vowline:start -->
...
<!-- vowline:end -->
```

Preserve all unrelated content before and after those blocks.

## Codex Global Removal

Codex's documented user skill path is `~/.agents/skills`. Vowline may also have a compatibility mirror under `${CODEX_HOME:-~/.codex}/skills` if it was installed by Vowline's script or by a Codex installer/Desktop environment that uses `CODEX_HOME/skills`.

Delete these directories if they exist:

```text
~/.agents/skills/vowline
${CODEX_HOME:-~/.codex}/skills/vowline
```

Then edit this file if it exists:

```text
${CODEX_HOME:-~/.codex}/AGENTS.md
```

Remove exactly the block from `<!-- vowline:start -->` through `<!-- vowline:end -->`. Leave the file in place if it contains other instructions.

Verify:

```text
~/.agents/skills/vowline does not exist
${CODEX_HOME:-~/.codex}/skills/vowline does not exist
${CODEX_HOME:-~/.codex}/AGENTS.md contains no Vowline marked block
```

## Codex Project Removal

For a project at `/path/to/project`, delete:

```text
/path/to/project/.agents/skills/vowline
```

Then remove the Vowline marked block from:

```text
/path/to/project/AGENTS.md
```

Preserve unrelated project instructions.

## Other Supported Agents

Delete any Vowline-owned global skill directories that exist:

```text
~/.claude/skills/vowline
~/.codeium/windsurf/skills/vowline
~/.cursor/skills/vowline
~/.gemini/skills/vowline
~/.copilot/skills/vowline
~/.opencode/skills/vowline
~/.config/opencode/skill/vowline
~/.config/agents/skills/vowline
~/.config/amp/skills/vowline
~/.goose/skills/vowline
~/.cline/skills/vowline
~/.roo-code/skills/vowline
~/.aider/skills/vowline
~/.openclaw/skills/vowline
~/.trae/skills/vowline
```

For project installs, delete matching project-local `vowline` skill directories under:

```text
.claude/skills/
.windsurf/skills/
.cursor/skills/
.gemini/skills/
.github/skills/
.opencode/skill/
.opencode/skills/
.goose/skills/
.cline/skills/
.roo-code/skills/
.aider/skills/
skills/
.trae/skills/
```

Remove Vowline marked blocks from bridge files if present:

```text
CLAUDE.md
GEMINI.md
.github/copilot-instructions.md
~/.claude/CLAUDE.md
~/.gemini/GEMINI.md
~/.codeium/windsurf/memories/global_rules.md
```

Delete generated Vowline rule files if present:

```text
.cursor/rules/vowline.mdc
.windsurf/rules/vowline.md
```

## Optional Scripted Removal

Global:

```bash
python3 uninstall.py global --harnesses codex
python3 uninstall.py verify-global --harnesses codex
```

Project:

```bash
python3 uninstall.py project /path/to/project --harnesses codex
python3 uninstall.py verify /path/to/project --harnesses codex
```

## Report

Report the skill directories removed, bridge files edited, generated rule files deleted, and verification result. If a target path was already absent, say it was already absent rather than treating that as a failure.

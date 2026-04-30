# Install Vowline

This guide is written for AI agents and humans. The goal is to install the canonical Vowline skill plus the smallest host-specific bridge files the selected agent harness can read.

You do not need to run a script when you can edit the filesystem directly. The scripts are optional helpers that perform the same copy, bridge-block replacement, and verification steps.

## Agent Install Contract

If you are an AI agent asked to install Vowline, use this repository as source material:

```text
skills/vowline/
guidance/
```

Copy `skills/vowline` as a directory to each selected skill target. Do not stop after copying `skills/vowline/SKILL.md` into one generic skill directory; Vowline works best when the relevant bridge files are installed too.

When adding guidance to an existing instruction file, preserve unrelated content and replace only the marked Vowline block:

```text
<!-- vowline:start -->
...
<!-- vowline:end -->
```

If no Vowline block exists, append one.

## Codex

Codex's documented skill discovery path is `.agents/skills` for projects and `~/.agents/skills` for user-level skills. Some current Codex installer/Desktop environments also use `$CODEX_HOME/skills`, which defaults to `~/.codex/skills`. Treat that second location as a compatibility mirror, not as the official required Codex path.

Global install:

```text
copy skills/vowline -> ~/.agents/skills/vowline
optionally mirror skills/vowline -> ${CODEX_HOME:-~/.codex}/skills/vowline for Codex installer/Desktop compatibility
append or replace guidance/AGENTS.md inside ${CODEX_HOME:-~/.codex}/AGENTS.md as a marked Vowline block
```

Project install:

```text
copy skills/vowline -> /path/to/project/.agents/skills/vowline
append or replace guidance/AGENTS.md inside /path/to/project/AGENTS.md as a marked Vowline block
```

Verify:

```text
~/.agents/skills/vowline/SKILL.md exists for global installs
/path/to/project/.agents/skills/vowline/SKILL.md exists for project installs
the optional compatibility mirror has SKILL.md if that mirror directory is present
the relevant AGENTS.md file contains exactly one Vowline marked block
```

## Claude Code

Global install:

```text
copy skills/vowline -> ${CLAUDE_CONFIG_DIR:-~/.claude}/skills/vowline
append or replace guidance/CLAUDE.md inside ${CLAUDE_CONFIG_DIR:-~/.claude}/CLAUDE.md as a marked Vowline block
```

Project install:

```text
copy skills/vowline -> /path/to/project/.claude/skills/vowline
append or replace guidance/CLAUDE.md inside /path/to/project/CLAUDE.md as a marked Vowline block
```

## Windsurf

Global install:

```text
copy skills/vowline -> ${WINDSURF_HOME:-~/.codeium/windsurf}/skills/vowline
append or replace guidance/WINDSURF-GLOBAL.md inside ${WINDSURF_HOME:-~/.codeium/windsurf}/memories/global_rules.md as a marked Vowline block
```

Project install:

```text
copy skills/vowline -> /path/to/project/.windsurf/skills/vowline
write guidance/WINDSURF.md -> /path/to/project/.windsurf/rules/vowline.md
```

Windsurf also discovers `.agents/skills`, so a Codex project install may be useful there too.

## Cursor

Global install:

```text
copy skills/vowline -> ${CURSOR_HOME:-~/.cursor}/skills/vowline
```

Project install:

```text
copy skills/vowline -> /path/to/project/.cursor/skills/vowline
write guidance/CURSOR.mdc -> /path/to/project/.cursor/rules/vowline.mdc
```

Cursor's rule file is the reliable bridge. The skill copy is included for the broader `SKILL.md` ecosystem and future compatibility.

## Gemini CLI

Global install:

```text
copy skills/vowline -> ${GEMINI_HOME:-~/.gemini}/skills/vowline
append or replace guidance/GEMINI.md inside ${GEMINI_HOME:-~/.gemini}/GEMINI.md as a marked Vowline block
```

Project install:

```text
copy skills/vowline -> /path/to/project/.gemini/skills/vowline
append or replace guidance/GEMINI.md inside /path/to/project/GEMINI.md as a marked Vowline block
```

## GitHub Copilot

Global install:

```text
copy skills/vowline -> ~/.copilot/skills/vowline
```

Project install:

```text
copy skills/vowline -> /path/to/project/.github/skills/vowline
append or replace guidance/COPILOT.md inside /path/to/project/.github/copilot-instructions.md as a marked Vowline block
```

## Community Skill Targets

When installing for all supported harnesses, also copy `skills/vowline` to the applicable targets below.

Global targets:

```text
~/.config/opencode/skill/vowline
~/.opencode/skills/vowline
~/.config/agents/skills/vowline
~/.config/amp/skills/vowline
~/.goose/skills/vowline
~/.cline/skills/vowline
~/.roo-code/skills/vowline
~/.aider/skills/vowline
~/.openclaw/skills/vowline
~/.trae/skills/vowline
```

Project targets:

```text
/path/to/project/.opencode/skill/vowline
/path/to/project/.opencode/skills/vowline
/path/to/project/.agents/skills/vowline
/path/to/project/.goose/skills/vowline
/path/to/project/.cline/skills/vowline
/path/to/project/.roo-code/skills/vowline
/path/to/project/.aider/skills/vowline
/path/to/project/skills/vowline
/path/to/project/.trae/skills/vowline
```

These community copies are passive skill directories. They do not alter host permissions or execute code.

## Optional Scripted Install

Global:

```bash
python3 install.py global --harnesses codex
python3 install.py verify-global --harnesses codex
```

Project:

```bash
python3 install.py project /path/to/project --harnesses codex
python3 install.py verify /path/to/project --harnesses codex
```

Use `--harnesses core` for Codex, Claude Code, Windsurf, Cursor, Gemini CLI, and GitHub Copilot. Use `--harnesses all` for core plus community targets.

## Repair An Incomplete Install

If a previous install copied only one skill directory, repeat the relevant install steps above. A repaired install should include each selected required skill target and each selected bridge file.

For Codex global installs, the documented required state is:

```text
~/.agents/skills/vowline/SKILL.md exists
${CODEX_HOME:-~/.codex}/AGENTS.md contains exactly one Vowline marked block
```

Recommended compatibility mirror:

```text
${CODEX_HOME:-~/.codex}/skills/vowline/SKILL.md exists when that Codex environment uses CODEX_HOME/skills
```

## Uninstall

See [UNINSTALL.md](UNINSTALL.md). It covers complete removal, partial-removal repair, and verification.

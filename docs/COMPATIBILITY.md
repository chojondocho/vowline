# Compatibility

Vowline keeps one canonical skill at `skills/vowline/SKILL.md` and adds thin adapters for agent harnesses that read rules, memories, or instruction files. The goal is portability without turning the covenant into a host-specific prompt stack.

## Reference Pattern

The compatibility layer follows the documented or commonly used locations below:

- [OpenAI Codex Agent Skills](https://developers.openai.com/codex/skills): `.agents/skills` and `~/.agents/skills`
- [Claude Code Skills](https://code.claude.com/docs/en/skills): `.claude/skills/<skill>/SKILL.md` and `~/.claude/skills/<skill>/SKILL.md`
- [Windsurf Skills](https://docs.windsurf.com/windsurf/cascade/skills): `.windsurf/skills/<skill>/SKILL.md`, `~/.codeium/windsurf/skills/<skill>/SKILL.md`, and `.agents/skills`
- [Windsurf Rules and AGENTS.md](https://docs.windsurf.com/windsurf/cascade/memories): `.windsurf/rules/*.md`, global rules, and `AGENTS.md`
- [Cursor Rules](https://docs.cursor.com/en/context/rules): `.cursor/rules/*.mdc`
- [GitHub Copilot agent skills](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills): `.github/skills`
- [GitHub Copilot repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions): `.github/copilot-instructions.md`

The result is not a claim that every host behaves identically. It means Vowline is placed where each host is known to look, with the least glue needed.

## Harnesses

### Codex

Project:

```text
.agents/skills/vowline/SKILL.md
AGENTS.md
```

Global:

```text
~/.agents/skills/vowline/SKILL.md
${CODEX_HOME:-~/.codex}/AGENTS.md
```

Compatibility mirror:

```text
${CODEX_HOME:-~/.codex}/skills/vowline/SKILL.md
```

The `~/.agents/skills` copy follows the public Codex skills documentation. The `${CODEX_HOME:-~/.codex}/skills` copy is a compatibility mirror for current Codex installer/Desktop environments that use `CODEX_HOME/skills`; it is not the official required Codex skill path.

Direct invocation:

```text
$vowline
```

### Claude Code

Project:

```text
.claude/skills/vowline/SKILL.md
CLAUDE.md
```

Global:

```text
${CLAUDE_CONFIG_DIR:-~/.claude}/skills/vowline/SKILL.md
${CLAUDE_CONFIG_DIR:-~/.claude}/CLAUDE.md
```

Direct invocation:

```text
/vowline
```

### Windsurf

Project:

```text
.windsurf/skills/vowline/SKILL.md
.windsurf/rules/vowline.md
```

Global:

```text
${WINDSURF_HOME:-~/.codeium/windsurf}/skills/vowline/SKILL.md
${WINDSURF_HOME:-~/.codeium/windsurf}/memories/global_rules.md
```

Direct invocation:

```text
@vowline
```

Windsurf also discovers `.agents/skills`, so Codex project installs can be useful there too.

### Cursor

Project:

```text
.cursor/skills/vowline/SKILL.md
.cursor/rules/vowline.mdc
```

Global:

```text
${CURSOR_HOME:-~/.cursor}/skills/vowline/SKILL.md
```

Cursor's rule file is the reliable bridge. The skill copy is included for the broader `SKILL.md` ecosystem and future compatibility.

### Gemini CLI

Project:

```text
.gemini/skills/vowline/SKILL.md
GEMINI.md
```

Global:

```text
${GEMINI_HOME:-~/.gemini}/skills/vowline/SKILL.md
${GEMINI_HOME:-~/.gemini}/GEMINI.md
```

### GitHub Copilot

Project:

```text
.github/skills/vowline/SKILL.md
.github/copilot-instructions.md
```

Global:

```text
~/.copilot/skills/vowline/SKILL.md
```

GitHub Copilot has a personal skill directory, but not a general local global instruction file equivalent to `~/.claude/CLAUDE.md`, so `install.py global` installs the skill and does not write Copilot guidance.

### Community `SKILL.md` Targets

The `all` install also writes skill copies for common community targets:

```text
.opencode/skill/vowline/SKILL.md
.opencode/skills/vowline/SKILL.md
.goose/skills/vowline/SKILL.md
.cline/skills/vowline/SKILL.md
.roo-code/skills/vowline/SKILL.md
.aider/skills/vowline/SKILL.md
skills/vowline/SKILL.md
.trae/skills/vowline/SKILL.md
```

Global equivalents are installed where community tools commonly look. These copies are passive: they do not alter host permissions or execute code.

## Why Two Layers

Native skill hosts use progressive disclosure: they see the skill name and description first, then load the full `SKILL.md` when relevant. Rule/context hosts load short instruction files more eagerly. Vowline uses both layers:

- `SKILL.md` carries the canonical covenant.
- Bridge files carry only the compact fallback contract.
- Marked blocks make repeated installs and uninstalls predictable.

## Boundaries

Vowline does not override system messages, host safety policies, repository rules, organization settings, or tool permissions. It also does not grant permission to deploy, publish, purchase, message people, mutate production data, delete data, or rotate credentials. It tells the agent to prepare the work and request explicit approval first.

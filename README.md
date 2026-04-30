# Vowline

[![check](https://github.com/chojondocho/vowline/actions/workflows/check.yml/badge.svg)](https://github.com/chojondocho/vowline/actions/workflows/check.yml)
[![release](https://img.shields.io/github/v/release/chojondocho/vowline)](https://github.com/chojondocho/vowline/releases)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

<p align="center">
  <img src="assets/vowline-banner.png" alt="Vowline brand banner: one luminous line moving through aligned agent nodes" width="100%">
</p>

**Outcome-first operating instructions for AI agents.**

Vowline is a portable `SKILL.md` package for Codex, Claude Code, Windsurf, Cursor, Gemini CLI, GitHub Copilot, and other skill-compatible agent harnesses. It gives agents a shared working contract for meaningful tasks: understand the real outcome, act with a small safe scope, preserve user intent, ask only when a question matters, verify when practical, and report the result plainly.

Use it when the agent needs judgment rather than a one-line answer: coding, debugging, research, writing, planning, review, design critique, document work, repository work, and handoffs.

## Quick start

The easiest path is to ask the target agent to install Vowline for itself:

```text
Install Vowline for yourself by following https://github.com/chojondocho/vowline/blob/main/INSTALL.md. Verify installation.
```

For a project-local install, ask from inside the project:

```text
Install Vowline into this project by following https://github.com/chojondocho/vowline/blob/main/INSTALL.md. Use project-local paths. Verify installation.
```

You do not need to clone this repository if your agent can read GitHub and write the relevant local files. Vowline is designed to be installed by agents as well as by humans.

## What it changes

Many bad agent answers do not fail because the model lacks raw capability. They fail because the work loop is vague.

| Common failure | Vowline's instruction |
| --- | --- |
| Answers the literal wording but misses the user's real goal | Frame the actual outcome before acting |
| Asks avoidable clarification questions | Proceed with safe assumptions unless the missing fact materially changes the result or creates risk |
| Makes broad edits when a small fix is enough | Inspect first, then make the smallest sufficient change |
| Rewrites tone, behavior, facts, or structure accidentally | Preserve intent, behavior, public interfaces, style, structure, and known facts unless the request requires otherwise |
| Uses tools, searches, or plans past the point of usefulness | Use the smallest sufficient evidence and tool loop |
| Takes externally visible or irreversible action too early | Prepare the work, then ask for explicit approval before acting |
| Reports effort instead of a usable result | Lead with the result, validation, assumptions, and remaining blockers |

The compact covenant is:

```text
Frame -> Preamble -> Effort -> Retrieve -> Act -> Authorize -> Verify -> Report -> Stop
```

In practice:

```text
Find the real outcome.
Proceed unless a missing fact changes the result or creates risk.
Use the smallest sufficient tool and evidence loop.
Preserve intent, behavior, structure, style, and facts.
Ask before irreversible or externally visible actions.
Validate the affected path when practical.
Answer with the result first.
Stop when more work would not materially improve correctness.
```

## Supported agents

Vowline keeps the canonical behavior in `skills/vowline/SKILL.md` and installs thin bridge files for hosts that read rules, memories, or instruction files.

| Agent / harness | Project install writes |
| --- | --- |
| Codex / AGENTS-aware tools | `.agents/skills/vowline/SKILL.md`, `AGENTS.md` |
| Claude Code | `.claude/skills/vowline/SKILL.md`, `CLAUDE.md` |
| Windsurf | `.windsurf/skills/vowline/SKILL.md`, `.windsurf/rules/vowline.md` |
| Cursor | `.cursor/skills/vowline/SKILL.md`, `.cursor/rules/vowline.mdc` |
| Gemini CLI | `.gemini/skills/vowline/SKILL.md`, `GEMINI.md` |
| GitHub Copilot | `.github/skills/vowline/SKILL.md`, `.github/copilot-instructions.md` |
| Community `SKILL.md` targets | OpenCode, Amp, Goose, Cline, Roo Code, Aider, OpenClaw, Trae skill folders |

Codex uses `~/.agents/skills/vowline/SKILL.md` as the documented user-level skill path. The installer also mirrors the skill into `${CODEX_HOME:-~/.codex}/skills/vowline/SKILL.md` for compatibility with Codex environments that use `CODEX_HOME/skills`. Treat that mirror as compatibility support, not as the primary Codex path.

See [INSTALL.md](INSTALL.md), [UNINSTALL.md](UNINSTALL.md), and [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) for exact global and project paths.

## Scripted install

The scripts are optional. They use only the Python standard library and are safe to run repeatedly.

Clone the repository first:

```bash
git clone https://github.com/chojondocho/vowline.git
cd vowline
```

Install into the current user's agent locations:

```bash
python3 install.py global --harnesses core
python3 install.py verify-global --harnesses core
```

Install into one project:

```bash
python3 install.py project /path/to/project --harnesses core
python3 install.py verify /path/to/project --harnesses core
```

Install only selected harnesses:

```bash
python3 install.py project /path/to/project --harnesses codex,claude,windsurf
python3 install.py global --harnesses codex
```

Harness groups:

| Group | Includes |
| --- | --- |
| `core` | Codex, Claude Code, Windsurf, Cursor, Gemini CLI, GitHub Copilot |
| `community` | OpenCode, Amp, Goose, Cline, Roo Code, Aider, OpenClaw, Trae |
| `all` | `core` plus `community` |

The script default is `all`. Pass `--harnesses core` when you want only the mainstream host targets.

## How to use it

After installation, direct invocation is usually optional because the host bridge files carry the fallback contract. Direct invocation is still useful when you want to force the skill for one request:

```text
$vowline review this launch plan for weak assumptions
/vowline rewrite this memo without losing the author's intent
@vowline compare these implementation options and recommend one
$vowline debug this failing test with the smallest safe change
```

Codex commonly uses `$vowline`, Claude Code commonly uses `/vowline`, and Windsurf commonly uses `@vowline`. Other hosts may surface skills or rules differently.

## Repository layout

```text
skills/vowline/SKILL.md      Canonical Vowline contract
guidance/                    Host-specific bridge text
install.py                   Optional installer and verifier
uninstall.py                 Optional uninstaller and verifier
docs/COMPATIBILITY.md        Supported paths and host notes
tests/                       Installer, verifier, and uninstall coverage
```

When Vowline edits an existing instruction file, it uses a marked block and preserves unrelated content:

```text
<!-- vowline:start -->
...
<!-- vowline:end -->
```

Repeated installs replace only that marked block.

## Boundaries

Vowline does not override system messages, platform policies, safety rules, repository instructions, organization settings, or tool permissions. It also does not make every host invoke the skill automatically.

Vowline does not grant permission to deploy, publish, purchase, message people, mutate production data, delete user data, rotate credentials, or take other externally visible or irreversible actions. It tells the agent to prepare the work and ask for explicit approval first.

## Development checks

Run the same basic checks used by the repository:

```bash
python3 -m py_compile install.py uninstall.py
python3 -m unittest discover -s tests
```

The tests cover project installs, global installs, harness selection, idempotent marked-block replacement, legacy cleanup, verification, and uninstall behavior.

## Uninstall

Ask the agent to remove Vowline:

```text
Uninstall Vowline from yourself by following https://github.com/chojondocho/vowline/blob/main/UNINSTALL.md. Verify removal.
```

Or use the optional script:

```bash
python3 uninstall.py global --harnesses core
python3 uninstall.py verify-global --harnesses core
```

For project-local removal:

```bash
python3 uninstall.py project /path/to/project --harnesses core
python3 uninstall.py verify /path/to/project --harnesses core
```

Uninstall removes Vowline-owned skill directories and Vowline marked blocks. It should not remove unrelated user or project instructions.

## Name

`Vowline` means a line of commitment: a small covenant tying the agent to the user's actual outcome. It is not legal trademark clearance.

## License

MIT. See [LICENSE](LICENSE).

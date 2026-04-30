# Vowline

[![check](https://github.com/chojondocho/vowline/actions/workflows/check.yml/badge.svg)](https://github.com/chojondocho/vowline/actions/workflows/check.yml)
[![release](https://img.shields.io/github/v/release/chojondocho/vowline)](https://github.com/chojondocho/vowline/releases)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

<p align="center">
  <img src="assets/vowline-banner.png" alt="Vowline brand banner: one luminous line moving through aligned agent nodes" width="100%">
</p>

**A compact operating covenant for AI agents.**

Vowline gives Codex, Claude Code, Windsurf, Cursor, Gemini CLI, GitHub Copilot, and other `SKILL.md`-compatible agents a shared way to handle meaningful work: understand the real outcome, avoid unnecessary clarification loops, preserve intent, control side effects, verify when practical, and report the result first.

It is not only for coding. Use it for research, writing, planning, review, design critique, document work, handoffs, repository work, and any request where an agent needs judgment rather than a one-line answer.

## Install With Your Agent

Most users do not need to clone this repository by hand. Open the agent you want to equip and paste:

```text
Install Vowline for yourself by following https://github.com/chojondocho/vowline/blob/main/INSTALL.md. Verify installation.
```

Vowline is agent-readable on purpose. The install guide explains how to copy the canonical skill and the host-specific bridge files directly. The Python helpers are optional for people who want a repeatable local command.

## Why Vowline

Many agent failures are not failures of intelligence. They are failures of operating discipline:

- answering the visible wording while missing the user's real goal;
- asking avoidable questions instead of making a safe, useful assumption;
- over-searching, over-planning, or over-editing because the stopping rule is vague;
- changing adjacent facts, tone, code, structure, or intent that should have been preserved;
- taking externally visible or irreversible actions without explicit approval;
- reporting effort instead of a result the user can trust.

Vowline compresses the countermeasure into one reusable covenant.

```text
Frame -> Preamble -> Effort -> Retrieve -> Act -> Authorize -> Verify -> Report -> Stop
```

In practical terms:

```text
Find the real outcome.
Proceed unless a missing fact materially changes the result or creates risk.
Use the smallest sufficient tool and evidence loop.
Preserve intent, behavior, style, structure, and facts.
Ask before irreversible or externally visible actions.
Validate the affected path when practical.
Answer with the result first.
Stop when more work would not materially improve correctness.
```

## Where It Helps

| Work type | What Vowline pushes the agent to do |
| --- | --- |
| Code and repositories | Inspect first, keep changes scoped, preserve behavior, run relevant checks |
| Research | Use authoritative sources, separate evidence from inference, cite important claims |
| Writing and editing | Preserve purpose, audience, tone, and known facts while removing weakness |
| Planning and decisions | State the recommendation, tradeoffs, validation path, and real blockers |
| Review and critique | Surface material risks first instead of nitpicks or reassurance |
| Design and visual work | Respect context, states, accessibility, responsiveness, and actual workflows |
| Handoffs | Leave exact state, evidence, risks, and the next useful action |

## What Gets Installed

Vowline keeps the canonical behavior in `skills/vowline/SKILL.md` and uses small bridge files for hosts that read standing rules or instruction files.

| Harness | Project install |
| --- | --- |
| Codex / AGENTS-aware tools | `.agents/skills/vowline/SKILL.md`, `AGENTS.md` |
| Claude Code | `.claude/skills/vowline/SKILL.md`, `CLAUDE.md` |
| Windsurf | `.windsurf/skills/vowline/SKILL.md`, `.windsurf/rules/vowline.md` |
| Cursor | `.cursor/skills/vowline/SKILL.md`, `.cursor/rules/vowline.mdc` |
| Gemini CLI | `.gemini/skills/vowline/SKILL.md`, `GEMINI.md` |
| GitHub Copilot | `.github/skills/vowline/SKILL.md`, `.github/copilot-instructions.md` |
| Community `SKILL.md` targets | OpenCode, Amp, Goose, Cline, Roo Code, Aider, OpenClaw, Trae skill folders |

For Codex, the documented user skill path is `~/.agents/skills/vowline/SKILL.md`. The installer also mirrors the skill into `${CODEX_HOME:-~/.codex}/skills/vowline/SKILL.md` for compatibility with current Codex installer/Desktop environments that use `CODEX_HOME/skills`. The mirror is useful, but it is not the official required Codex skill path.

See [INSTALL.md](INSTALL.md), [UNINSTALL.md](UNINSTALL.md), and [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) for exact paths.

## Optional Scripted Install

The scripts are optional helpers, not a requirement. They are stdlib-only and idempotent.

Project scope:

```bash
python3 install.py project /path/to/project
python3 install.py verify /path/to/project
```

User/global scope:

```bash
python3 install.py global
python3 install.py verify-global
```

Install a smaller set of harnesses:

```bash
python3 install.py project /path/to/project --harnesses codex,claude,windsurf
python3 install.py global --harnesses core
```

`core` means Codex, Claude Code, Windsurf, Cursor, Gemini CLI, and GitHub Copilot. `all` also writes community `SKILL.md` copies for OpenCode, Amp, Goose, Cline, Roo Code, Aider, OpenClaw, and Trae.

## Use

Direct invocation works when you want to force the skill:

```text
$vowline review this launch plan for weak assumptions
/vowline rewrite this memo without losing the author's intent
@vowline compare these options and recommend one
$vowline debug this failing test without broad refactors
```

After installation, direct invocation is usually optional for substantive work because the host-specific bridge files carry a compact fallback contract.

## Design Boundaries

Vowline does not override system messages, safety policies, repository rules, organization settings, or tool permissions. It does not force automatic invocation in every host.

It also does not grant an agent permission to deploy, publish, message people, mutate production data, delete user data, purchase anything, rotate credentials, or take other externally visible actions. It tells the agent to prepare the work and ask for explicit approval first.

## Repository Checks

Run:

```bash
python3 -m py_compile install.py uninstall.py
python3 -m unittest discover -s tests
```

The tests cover project install, global install, harness selection, idempotent marked-block replacement, legacy cleanup, verification, and uninstall.

## Uninstall

To ask your agent to remove Vowline, paste:

```text
Uninstall Vowline from yourself by following https://github.com/chojondocho/vowline/blob/main/UNINSTALL.md. Verify removal.
```

Optional scripted removal:

```bash
python3 uninstall.py project /path/to/project
python3 uninstall.py global
python3 uninstall.py verify-global
```

## Name

`Vowline` means a line of commitment: a small covenant tying the agent to the user's actual outcome. It is not legal trademark clearance.

## License

MIT. See [LICENSE](LICENSE).

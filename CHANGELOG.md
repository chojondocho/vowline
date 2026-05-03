# Changelog

## 0.3.0 - 2026-05-03

- Hardened the canonical `vowline` tool-use contract to select from runtime-available tools, skills, plugins, hosted capabilities, and tool descriptions when tool choice affects the outcome.
- Added fallback guidance so agents preserve the objective and verification need when a planned tool is unavailable, has the wrong capability, or fails before meaningful work starts.
- Clarified that missing or failed verifiers are not verification, and weaker substitute checks must be reported as weaker evidence or residual risk rather than a pass.
- Refreshed README wording for tool availability, remapping, and verification-preserving behavior.

## 0.2.0 - 2026-05-01

- Reworked the canonical `vowline` skill into a broader cross-cutting operating skill for substantive agent work across tools, skills, and subagents.
- Replaced compact host bridge guidance with the current Vowline activation block.
- Added `UPDATE.md` to document updating existing installs by rerunning the idempotent install flow from the latest repository.
- Refreshed README, compatibility, contribution, and repository-agent guidance for the new operating-skill contract.

## 0.1.0 - Initial release

- Added the canonical `vowline` skill.
- Added compact bridge guidance for Codex, Claude Code, Windsurf, Cursor, Gemini CLI, and GitHub Copilot.
- Added project and user/global install targets, including community `SKILL.md` directories for OpenCode, Amp, Goose, Cline, Roo Code, Aider, OpenClaw, and Trae.
- Added optional stdlib-only install and uninstall helpers with verification commands.
- Added idempotent marked-block replacement and cleanup for earlier `agent-operating-standard` installs.
- Added repository checks and GitHub Actions workflow.
- Documented Codex's official `~/.agents/skills` path and the optional `${CODEX_HOME:-~/.codex}/skills` compatibility mirror.

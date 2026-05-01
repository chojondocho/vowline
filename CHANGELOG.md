# Changelog

## Unreleased

- Reworked the canonical `vowline` skill into a broader cross-cutting operating skill for substantive agent work across tools, skills, and subagents.
- Replaced compact host bridge guidance with the current Vowline activation block.
- Added `UPDATE.md` to document updating existing installs by rerunning the idempotent install flow from the latest repository.
- Added README and repository-agent guidance for update requests and verification.

## 0.1.0 - Initial release

- Added the canonical `vowline` skill.
- Added compact bridge guidance for Codex, Claude Code, Windsurf, Cursor, Gemini CLI, and GitHub Copilot.
- Added project and user/global install targets, including community `SKILL.md` directories for OpenCode, Amp, Goose, Cline, Roo Code, Aider, OpenClaw, and Trae.
- Added optional stdlib-only install and uninstall helpers with verification commands.
- Added idempotent marked-block replacement and cleanup for earlier `agent-operating-standard` installs.
- Added repository checks and GitHub Actions workflow.
- Documented Codex's official `~/.agents/skills` path and the optional `${CODEX_HOME:-~/.codex}/skills` compatibility mirror.

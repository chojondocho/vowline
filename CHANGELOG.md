# Changelog

## 0.4.0 - 2026-05-03

- Consolidated host-specific bridge guidance into a single canonical activation source at `guidance/VOWLINE_ACTIVATION.md`; removed the seven legacy per-host guidance files.
- Made `install.py` render every host bridge file from that single source, prepending the front matter required by Cursor (`alwaysApply: true`) and Windsurf (`trigger: always_on`).
- Added `python3 install.py render-guidance {marked-block|AGENTS.md|CLAUDE.md|GEMINI.md|COPILOT.md|WINDSURF-GLOBAL.md|WINDSURF.md|CURSOR.mdc}` so manual installers can emit the exact rendered text without running the install flow.
- Refreshed the canonical `vowline` skill body with broader operating-mode, evidence, retrieval-budget, tool-use, change-discipline, verification, output-contract, completion, and task-overlay sections.
- Refreshed README, INSTALL, UPDATE, UNINSTALL, and AGENTS guidance to point at the single activation source and the rendering rules.
- Extended the test suite to assert that every host bridge is rendered from `guidance/VOWLINE_ACTIVATION.md` and that install docs document the script-free rendering rules.

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

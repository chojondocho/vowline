# Changelog

## 0.7.0 - 2026-05-26

- Updated the canonical `skills/vowline/SKILL.md` to the benchmark-selected `6057fa00a6c074fe2af5f28b0a11062e69e154acf6296d4c65eb8b63f1cd637c` contract: future-client binding, exact final-surface predicates, public-label preservation, source-backed entity and metric universes, native structured tools, scoped cleanup paths, and bounded faithful proof.
- Refreshed README around the 0.7.0 contract so the public summary points at the current canonical skill rather than the historical 0.6.0 operating table.
- Added a current 0.7.0 deterministic benchmark summary and chart under `docs/benchmarks/`, reporting the exact same-hash `6057fa00` run set as 12 / 13 checked benchmark tasks passed across SkillsBench, IFEval, LiveBench, and Terminal-Bench, with `nginx-request-logging` still open.
- Reclassified the prior `8e427bb4` benchmark page as a historical 0.6.0 baseline instead of the current best-so-far claim.

## 0.6.0 - 2026-05-17

- Reworked the canonical `vowline` skill into the new public-contract operating model: public task binding, a small working ledger, current-public-evidence proof, proof predicates scoped to the visible contract, transferable competence, smallest live write sets, cleanup allowlists, and final reporting that separates current proof from non-proof.
- Updated the activation bridge body to require consistent Vowline use, including for sub-agents, while continuing to render all host bridge files from `guidance/VOWLINE_ACTIVATION.md`.
- Refreshed README around the new `SKILL.md` contract, including the 0.6.0 operating requirements, proof and cleanup discipline, direct invocation examples, and the repository layout for benchmark documentation.
- Removed AI-written README detail sections that incorrectly paraphrased the canonical contract, and replaced them with a direct link to `skills/vowline/SKILL.md` for the full details.
- Added the preliminary 0.6.0 failure-only benchmark summary and chart under `docs/benchmarks/`, reporting the `8e427bb4` no-skill comparison as 8 recovered tasks out of 12 selected no-skill failures, with no proxy judges or LLM-as-judge claims.
- Updated the OpenAI skill metadata short description to match the new canonical Vowline description.

## 0.5.0 - 2026-05-06

- Compressed the canonical `vowline` skill body into a shorter operating contract centered on contract clarity, authority, evidence, output shape, computation, privacy, tool use, verification, and result-first completion.
- Simplified `guidance/VOWLINE_ACTIVATION.md` to a direct bridge directive: `` Always use the skill `vowline` ``.
- Hardened generated-rule verification to compare Cursor and Windsurf rule files against the rendered guidance instead of relying on a brittle display-name substring.
- Preserved the skill's core boundaries for higher-priority instructions, explicit authorization before external side effects, conservative changes, and evidence-backed reporting.

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

# Agent Instructions for Vowline

If you are an AI agent installing Vowline for a user, follow `INSTALL.md`. Do not use a generic skill installer as the whole install unless it also installs the documented skill path and the relevant bridge files.

The install guide is the source of truth because it covers the canonical skill, host-specific bridge files, optional compatibility mirrors, and verification.

You may install by directly copying skill directories and inserting marked bridge blocks as described in `INSTALL.md`. The scripts are optional helpers, not the only valid path.

For Codex global installs, the documented required state is:

```text
~/.agents/skills/vowline/SKILL.md
${CODEX_HOME:-~/.codex}/AGENTS.md with one <!-- vowline:start --> block
```

The installer also writes `${CODEX_HOME:-~/.codex}/skills/vowline/SKILL.md` as a compatibility mirror for current Codex installer/Desktop environments that use `CODEX_HOME/skills`. Do not describe that mirror as an official Codex requirement.

Report the documented path, any compatibility mirror written, and the verification result. If Vowline was previously installed only into `${CODEX_HOME:-~/.codex}/skills/vowline`, follow `INSTALL.md` again to repair the missing documented skill path and bridge file.

For update requests, follow `UPDATE.md`. Updating is a repeat install from the latest repository source, not a partial edit of one `SKILL.md`; refresh the selected Vowline-owned skill directories, replace the selected marked bridge blocks, then verify. Preserve unrelated user and project instructions.

For uninstall requests, follow `UNINSTALL.md`. Do not only delete one skill directory; remove all selected Vowline-owned skill folders and marked bridge blocks, then verify removal.

Expected Codex global removal means `~/.agents/skills/vowline` is gone, any `${CODEX_HOME:-~/.codex}/skills/vowline` compatibility mirror is gone, and `${CODEX_HOME:-~/.codex}/AGENTS.md` no longer contains a `<!-- vowline:start -->` block.

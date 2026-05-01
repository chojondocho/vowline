# Update Vowline

This guide is written for AI agents and humans updating an existing Vowline install. The goal is to refresh Vowline-owned files from the latest repository source while preserving unrelated user and project instructions.

Updating Vowline is a repeat install with replacement semantics:

```text
skills/vowline/  -> canonical skill directory source
guidance/        -> current bridge and generated-rule text
INSTALL.md       -> exact paths, harness groups, and install expectations
```

Do not duplicate the `INSTALL.md` path matrix or the full Vowline bridge block here. When paths, harnesses, or bridge wording change, update the source files above instead of maintaining parallel copies in this guide.

You do not need to run a script when you can edit the filesystem directly. The scripts are optional helpers that perform the same skill-directory replacement, bridge-block replacement, generated-rule rewrite, and verification steps.

## Agent Update Contract

If you are an AI agent asked to update Vowline, inspect `INSTALL.md`, `skills/vowline/`, and `guidance/` before changing files.

Do not update only one installed `SKILL.md`. A correct update refreshes each selected Vowline-owned skill directory and each selected host bridge file or generated rule file.

For each selected harness and target from `INSTALL.md`:

```text
replace the installed Vowline skill directory with latest skills/vowline
replace selected marked Vowline blocks using the current guidance file
rewrite selected generated Vowline rule files from guidance/
verify the selected targets
```

Preserve unrelated content before and after marked blocks. If a selected bridge file does not contain a Vowline block, append the current block from the relevant `guidance/` file. If it contains an older compact Vowline block, replace only that marked block.

## Choose Scope

Use the same harness scope that was originally installed unless the user asks to narrow or expand it. If the original scope is unclear, inspect the existing install targets when practical.

Common scope names are documented in `INSTALL.md`:

```text
codex
core
all
```

Use `core` as the practical default for mainstream agent hosts when the user does not know the prior scope and discovery is not practical. Use `all` only when the user wants every supported target refreshed.

For user-level requests such as "update Vowline for yourself", update the selected global/user locations. For project requests such as "update Vowline in this project", update the selected project-local locations.

## Manual Update

1. Start from the latest repository source, for example a fresh clone, a pulled checkout, or a source tree explicitly selected by the user.
2. Open `INSTALL.md` and locate the selected global or project install section.
3. Repeat the relevant install steps, treating `copy` as `replace` for existing Vowline-owned skill directories.
4. Replace only marked Vowline blocks in existing instruction files.
5. Rewrite selected generated Vowline rule files where the host uses generated rules.
6. Verify the selected targets.

If a selected target is absent, decide whether the requested scope means it should be newly installed or simply reported as absent. If the user asked to update every supported target, do not silently leave an older Vowline copy in an unselected location.

## Optional Scripted Update

If you prefer scripted updates, run the installer from the latest repository source. The script is not required; it is only a helper for the same replacement and verification work described above.

Global:

```bash
git pull
python3 install.py global --harnesses codex
python3 install.py verify-global --harnesses codex
```

Project:

```bash
git pull
python3 install.py project /path/to/project --harnesses codex
python3 install.py verify /path/to/project --harnesses codex
```

Replace `codex` with the selected scope, such as `core` or `all`, when needed.

## Update Prompts

Ask an agent to update its own user-level install:

```text
Update Vowline for yourself by following https://github.com/chojondocho/vowline/blob/main/UPDATE.md. Verify the update.
```

Ask an agent to update a project-local install:

```text
Update Vowline in this project by following https://github.com/chojondocho/vowline/blob/main/UPDATE.md. Use project-local paths. Verify the update.
```

The agent should refresh the selected skill directories, replace selected marked bridge blocks, rewrite selected generated rule files, and verify the result against the relevant `INSTALL.md` expected state.

## Verification

Use the verification criteria from the relevant `INSTALL.md` sections, plus content checks when possible.

Useful checks, whether run manually or through the optional script:

```bash
python3 install.py verify-global --harnesses codex
python3 install.py verify /path/to/project --harnesses codex
diff -qr skills/vowline /selected/skill/path/vowline
grep -c '<!-- vowline:start -->' /selected/bridge/file
grep -c '<!-- vowline:end -->' /selected/bridge/file
```

Replace `codex` and placeholder paths with the selected scope and target paths.

A valid update should confirm:

```text
selected skill directories exist and match latest skills/vowline
selected bridge files contain exactly one current Vowline marked block
selected generated rule files match current guidance/ content where applicable
unrelated user and project instructions were preserved
```

## Repair A Partial Update

If a previous update copied only one `SKILL.md`, repeat the relevant update steps above. A repaired update should include each selected skill target and each selected bridge file or generated rule file.

If an older install exists only in a compatibility mirror or one host-specific path, follow `INSTALL.md` again for the selected scope so the documented target paths are restored.

## Boundaries

Updating does not remove unrelated user or project instructions.

Updating does not grant permission to deploy, publish, commit, push, send messages, mutate production data, rotate credentials, purchase anything, or take other externally visible or irreversible action.

Updating a narrower harness scope leaves unselected old Vowline copies untouched. Run the update with the same or broader scope if you want every previous target refreshed.

## Report

Report the usable result, not just the steps attempted:

```text
updated skill directories
updated bridge files or generated rule files
verification command and result
any selected target that was absent, skipped, or not writable
```

## Uninstall

To remove Vowline instead of updating it, follow [UNINSTALL.md](UNINSTALL.md). It covers complete removal, partial-removal repair, and verification.

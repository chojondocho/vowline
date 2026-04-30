#!/usr/bin/env python3
"""Remove Vowline from AI agent harness instruction locations."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from install import (
    LEGACY_SKILLS,
    MARKERS,
    SRC,
    SKILL,
    SUPPORTED_HARNESSES,
    codex_home,
    claude_home,
    gemini_home,
    global_skill_base_dirs,
    parse_harnesses,
    project_skill_base_dirs,
    read_text,
    remove_path,
    selected_global_skill_paths,
    selected_project_skill_paths,
    windsurf_home,
)


def without_marked_blocks(text: str) -> str:
    out: list[str] = []
    active_end: str | None = None
    starts = {start: end for start, end in MARKERS}
    for line in text.splitlines():
        stripped = line.strip()
        if active_end is not None:
            if stripped == active_end:
                active_end = None
            continue
        if stripped in starts:
            active_end = starts[stripped]
            continue
        out.append(line)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + ("\n" if out else "")


def clean_file(path: Path) -> None:
    if path.exists():
        path.write_text(without_marked_blocks(read_text(path)), encoding="utf-8")


def remove_if_present(path: Path) -> None:
    if path.resolve() == SRC.resolve():
        return
    if path.exists() or path.is_symlink():
        remove_path(path)


def remove_skill_paths(paths: list[Path]) -> None:
    for path in paths:
        remove_if_present(path)


def remove_legacy(base_dirs: list[Path]) -> None:
    for base in base_dirs:
        for name in LEGACY_SKILLS:
            remove_if_present(base / name)


def clean_project_guidance(target: Path, harnesses: tuple[str, ...]) -> None:
    if {"codex", "amp"} & set(harnesses):
        clean_file(target / "AGENTS.md")
    if "claude" in harnesses:
        clean_file(target / "CLAUDE.md")
    if "gemini" in harnesses:
        clean_file(target / "GEMINI.md")
    if "copilot" in harnesses:
        clean_file(target / ".github" / "copilot-instructions.md")
    if "cursor" in harnesses:
        remove_if_present(target / ".cursor" / "rules" / "vowline.mdc")
    if "windsurf" in harnesses:
        remove_if_present(target / ".windsurf" / "rules" / "vowline.md")


def clean_global_guidance(harnesses: tuple[str, ...]) -> None:
    if {"codex", "amp"} & set(harnesses):
        clean_file(codex_home() / "AGENTS.md")
    if "claude" in harnesses:
        clean_file(claude_home() / "CLAUDE.md")
    if "gemini" in harnesses:
        clean_file(gemini_home() / "GEMINI.md")
    if "windsurf" in harnesses:
        clean_file(windsurf_home() / "memories" / "global_rules.md")


def uninstall_project(target: Path, harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> None:
    target = target.expanduser().resolve()
    remove_skill_paths(selected_project_skill_paths(target, harnesses))
    remove_legacy(project_skill_base_dirs(target, harnesses))
    clean_project_guidance(target, harnesses)
    print(f"Removed {SKILL} from project: {target}")
    print(f"Harnesses: {', '.join(harnesses)}")


def uninstall_global(harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> None:
    remove_skill_paths(selected_global_skill_paths(harnesses))
    remove_legacy(global_skill_base_dirs(harnesses))
    clean_global_guidance(harnesses)
    print(f"Removed {SKILL} globally.")
    print(f"Harnesses: {', '.join(harnesses)}")


def contains_vowline_block(path: Path) -> bool:
    if not path.exists():
        return False
    text = read_text(path)
    return MARKERS[0][0] in text or MARKERS[0][1] in text


def verify_project_removed(target: Path, harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> int:
    target = target.expanduser().resolve()
    failures: list[str] = []
    for path in selected_project_skill_paths(target, harnesses):
        if path.exists() or path.is_symlink():
            failures.append(f"skill still present: {path}")

    marked_files: list[Path] = []
    if {"codex", "amp"} & set(harnesses):
        marked_files.append(target / "AGENTS.md")
    if "claude" in harnesses:
        marked_files.append(target / "CLAUDE.md")
    if "gemini" in harnesses:
        marked_files.append(target / "GEMINI.md")
    if "copilot" in harnesses:
        marked_files.append(target / ".github" / "copilot-instructions.md")

    for file_path in marked_files:
        if contains_vowline_block(file_path):
            failures.append(f"Vowline block still present: {file_path}")

    generated_files: list[Path] = []
    if "cursor" in harnesses:
        generated_files.append(target / ".cursor" / "rules" / "vowline.mdc")
    if "windsurf" in harnesses:
        generated_files.append(target / ".windsurf" / "rules" / "vowline.md")

    for file_path in generated_files:
        if file_path.exists() or file_path.is_symlink():
            failures.append(f"generated guidance still present: {file_path}")

    for base in project_skill_base_dirs(target, harnesses):
        for legacy in LEGACY_SKILLS:
            if (base / legacy).exists() or (base / legacy).is_symlink():
                failures.append(f"legacy skill still present: {base / legacy}")

    if failures:
        print("Vowline project uninstall verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Vowline project uninstall verified: {target}")
    print(f"Harnesses: {', '.join(harnesses)}")
    return 0


def verify_global_removed(harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> int:
    failures: list[str] = []
    for path in selected_global_skill_paths(harnesses):
        if path.exists() or path.is_symlink():
            failures.append(f"skill still present: {path}")

    marked_files: list[Path] = []
    if {"codex", "amp"} & set(harnesses):
        marked_files.append(codex_home() / "AGENTS.md")
    if "claude" in harnesses:
        marked_files.append(claude_home() / "CLAUDE.md")
    if "gemini" in harnesses:
        marked_files.append(gemini_home() / "GEMINI.md")
    if "windsurf" in harnesses:
        marked_files.append(windsurf_home() / "memories" / "global_rules.md")

    for file_path in marked_files:
        if contains_vowline_block(file_path):
            failures.append(f"Vowline block still present: {file_path}")

    for base in global_skill_base_dirs(harnesses):
        for legacy in LEGACY_SKILLS:
            if (base / legacy).exists() or (base / legacy).is_symlink():
                failures.append(f"legacy skill still present: {base / legacy}")

    if failures:
        print("Vowline global uninstall verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("Vowline global uninstall verified.")
    print(f"Harnesses: {', '.join(harnesses)}")
    return 0


def add_harness_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--harnesses",
        "--agents",
        default="all",
        help=(
            "comma- or space-separated harnesses to remove; use all, core, community, "
            "or any of: " + ", ".join(SUPPORTED_HARNESSES)
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Uninstall Vowline from AI agent harnesses.")
    sub = parser.add_subparsers(dest="scope", required=True)
    project = sub.add_parser("project", help="remove from a repository or project directory")
    project.add_argument("path", nargs="?", default=".", help="project path; defaults to the current directory")
    add_harness_arg(project)
    global_parser = sub.add_parser("global", help="remove from the current user's global locations")
    add_harness_arg(global_parser)
    verify = sub.add_parser("verify", help="verify removal from a repository or project directory")
    verify.add_argument("path", nargs="?", default=".", help="project path; defaults to the current directory")
    add_harness_arg(verify)
    verify_global = sub.add_parser("verify-global", help="verify removal from the current user's global locations")
    add_harness_arg(verify_global)
    args = parser.parse_args()

    try:
        harnesses = parse_harnesses(args.harnesses)
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))

    if args.scope == "project":
        uninstall_project(Path(args.path), harnesses)
    elif args.scope == "global":
        uninstall_global(harnesses)
    elif args.scope == "verify":
        raise SystemExit(verify_project_removed(Path(args.path), harnesses))
    elif args.scope == "verify-global":
        raise SystemExit(verify_global_removed(harnesses))
    else:  # pragma: no cover
        parser.error(f"unknown command: {args.scope}")


if __name__ == "__main__":
    main()

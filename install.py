#!/usr/bin/env python3
"""Install Vowline across AI agent harnesses.

Stdlib-only, idempotent, and safe to run repeatedly.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

SKILL = "vowline"
LEGACY_SKILLS = ("agent-operating-standard",)
MARKERS = (
    ("<!-- vowline:start -->", "<!-- vowline:end -->"),
    ("<!-- agent-operating-standard:start -->", "<!-- agent-operating-standard:end -->"),
)
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "skills" / SKILL
CORE_HARNESSES = ("codex", "claude", "windsurf", "cursor", "gemini", "copilot")
COMMUNITY_HARNESSES = ("opencode", "amp", "goose", "cline", "roo", "aider", "openclaw", "trae")
SUPPORTED_HARNESSES = CORE_HARNESSES + COMMUNITY_HARNESSES
HARNESS_ALIASES = {
    "all": SUPPORTED_HARNESSES,
    "default": SUPPORTED_HARNESSES,
    "core": CORE_HARNESSES,
    "native": CORE_HARNESSES,
    "community": COMMUNITY_HARNESSES,
    "claude-code": ("claude",),
    "github-copilot": ("copilot",),
    "copilot-coding-agent": ("copilot",),
    "gemini-cli": ("gemini",),
    "roo-code": ("roo",),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def guidance(name: str) -> str:
    return read_text(ROOT / "guidance" / name)


def unique(paths: list[Path]) -> list[Path]:
    seen: set[str] = set()
    out: list[Path] = []
    for path in paths:
        key = str(path)
        if key not in seen:
            seen.add(key)
            out.append(path)
    return out


def parse_harnesses(value: str) -> tuple[str, ...]:
    parts = [part.strip().lower() for part in value.replace(",", " ").split()]
    if not parts:
        return SUPPORTED_HARNESSES

    expanded: list[str] = []
    for part in parts:
        if part in HARNESS_ALIASES:
            expanded.extend(HARNESS_ALIASES[part])
        elif part in SUPPORTED_HARNESSES:
            expanded.append(part)
        else:
            supported = ", ".join((*SUPPORTED_HARNESSES, *sorted(HARNESS_ALIASES)))
            raise argparse.ArgumentTypeError(f"unknown harness {part!r}; expected one of: {supported}")

    out: list[str] = []
    for item in expanded:
        if item not in out:
            out.append(item)
    return tuple(out)


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
    return "\n".join(out)


def replace_block(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    preserved = without_marked_blocks(read_text(path))
    start, end = MARKERS[0]
    block = f"{start}\n{body.rstrip()}\n{end}"
    combined = f"{preserved}\n\n{block}\n" if preserved else f"{block}\n"
    path.write_text(combined, encoding="utf-8")


def write_generated_file(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.rstrip() + "\n", encoding="utf-8")


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def copy_skill(dest: Path) -> None:
    if not SRC.is_dir():
        raise SystemExit(f"missing source skill directory: {SRC}")
    if dest.resolve() == SRC.resolve():
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() or dest.is_symlink():
        remove_path(dest)
    shutil.copytree(SRC, dest)


def remove_skill_dirs(base: Path, names: tuple[str, ...]) -> None:
    for name in names:
        path = base / name
        if path.exists() or path.is_symlink():
            remove_path(path)


def claude_home() -> Path:
    return Path(os.environ.get("CLAUDE_CONFIG_DIR", Path.home() / ".claude")).expanduser()


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()


def windsurf_home() -> Path:
    default = Path.home() / ".codeium" / "windsurf"
    return Path(os.environ.get("WINDSURF_HOME", str(default))).expanduser()


def cursor_home() -> Path:
    return Path(os.environ.get("CURSOR_HOME", str(Path.home() / ".cursor"))).expanduser()


def gemini_home() -> Path:
    return Path(os.environ.get("GEMINI_HOME", str(Path.home() / ".gemini"))).expanduser()


def opencode_home() -> Path:
    return Path(os.environ.get("OPENCODE_HOME", str(Path.home() / ".config" / "opencode"))).expanduser()


def project_skill_paths(target: Path, harness: str) -> list[Path]:
    return {
        "codex": [target / ".agents" / "skills" / SKILL],
        "claude": [target / ".claude" / "skills" / SKILL],
        "windsurf": [target / ".windsurf" / "skills" / SKILL],
        "cursor": [target / ".cursor" / "skills" / SKILL],
        "gemini": [target / ".gemini" / "skills" / SKILL],
        "copilot": [target / ".github" / "skills" / SKILL],
        "opencode": [target / ".opencode" / "skill" / SKILL, target / ".opencode" / "skills" / SKILL],
        "amp": [target / ".agents" / "skills" / SKILL],
        "goose": [target / ".goose" / "skills" / SKILL],
        "cline": [target / ".cline" / "skills" / SKILL],
        "roo": [target / ".roo-code" / "skills" / SKILL],
        "aider": [target / ".aider" / "skills" / SKILL],
        "openclaw": [target / "skills" / SKILL],
        "trae": [target / ".trae" / "skills" / SKILL],
    }[harness]


def global_skill_paths(harness: str) -> list[Path]:
    return {
        "codex": [
            Path.home() / ".agents" / "skills" / SKILL,
            codex_home() / "skills" / SKILL,
        ],
        "claude": [claude_home() / "skills" / SKILL],
        "windsurf": [windsurf_home() / "skills" / SKILL],
        "cursor": [cursor_home() / "skills" / SKILL],
        "gemini": [gemini_home() / "skills" / SKILL],
        "copilot": [Path.home() / ".copilot" / "skills" / SKILL],
        "opencode": [opencode_home() / "skill" / SKILL, Path.home() / ".opencode" / "skills" / SKILL],
        "amp": [Path.home() / ".config" / "agents" / "skills" / SKILL, Path.home() / ".config" / "amp" / "skills" / SKILL],
        "goose": [Path.home() / ".goose" / "skills" / SKILL],
        "cline": [Path.home() / ".cline" / "skills" / SKILL],
        "roo": [Path.home() / ".roo-code" / "skills" / SKILL],
        "aider": [Path.home() / ".aider" / "skills" / SKILL],
        "openclaw": [Path.home() / ".openclaw" / "skills" / SKILL],
        "trae": [Path.home() / ".trae" / "skills" / SKILL],
    }[harness]


def required_global_skill_paths(harness: str) -> list[Path]:
    if harness == "codex":
        return [Path.home() / ".agents" / "skills" / SKILL]
    return global_skill_paths(harness)


def optional_global_skill_paths(harness: str) -> list[Path]:
    if harness == "codex":
        return [codex_home() / "skills" / SKILL]
    return []


def project_skill_base_dirs(target: Path, harnesses: tuple[str, ...]) -> list[Path]:
    paths: list[Path] = []
    for harness in harnesses:
        paths.extend(path.parent for path in project_skill_paths(target, harness))
    return unique(paths)


def global_skill_base_dirs(harnesses: tuple[str, ...]) -> list[Path]:
    paths: list[Path] = []
    for harness in harnesses:
        paths.extend(path.parent for path in global_skill_paths(harness))
    return unique(paths)


def selected_project_skill_paths(target: Path, harnesses: tuple[str, ...]) -> list[Path]:
    paths: list[Path] = []
    for harness in harnesses:
        paths.extend(project_skill_paths(target, harness))
    return unique(paths)


def selected_global_skill_paths(harnesses: tuple[str, ...]) -> list[Path]:
    paths: list[Path] = []
    for harness in harnesses:
        paths.extend(global_skill_paths(harness))
    return unique(paths)


def selected_required_global_skill_paths(harnesses: tuple[str, ...]) -> list[Path]:
    paths: list[Path] = []
    for harness in harnesses:
        paths.extend(required_global_skill_paths(harness))
    return unique(paths)


def selected_optional_global_skill_paths(harnesses: tuple[str, ...]) -> list[Path]:
    paths: list[Path] = []
    for harness in harnesses:
        paths.extend(optional_global_skill_paths(harness))
    return unique(paths)


def add_project_guidance(target: Path, harnesses: tuple[str, ...]) -> None:
    if {"codex", "amp"} & set(harnesses):
        replace_block(target / "AGENTS.md", guidance("AGENTS.md"))
    if "claude" in harnesses:
        replace_block(target / "CLAUDE.md", guidance("CLAUDE.md"))
    if "gemini" in harnesses:
        replace_block(target / "GEMINI.md", guidance("GEMINI.md"))
    if "copilot" in harnesses:
        replace_block(target / ".github" / "copilot-instructions.md", guidance("COPILOT.md"))
    if "cursor" in harnesses:
        write_generated_file(target / ".cursor" / "rules" / "vowline.mdc", guidance("CURSOR.mdc"))
    if "windsurf" in harnesses:
        write_generated_file(target / ".windsurf" / "rules" / "vowline.md", guidance("WINDSURF.md"))


def add_global_guidance(harnesses: tuple[str, ...]) -> None:
    if {"codex", "amp"} & set(harnesses):
        replace_block(codex_home() / "AGENTS.md", guidance("AGENTS.md"))
    if "claude" in harnesses:
        replace_block(claude_home() / "CLAUDE.md", guidance("CLAUDE.md"))
    if "gemini" in harnesses:
        replace_block(gemini_home() / "GEMINI.md", guidance("GEMINI.md"))
    if "windsurf" in harnesses:
        replace_block(windsurf_home() / "memories" / "global_rules.md", guidance("WINDSURF-GLOBAL.md"))


def install_project(target: Path, harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> None:
    target = target.expanduser().resolve()
    if not target.exists():
        raise SystemExit(f"project path does not exist: {target}")

    for path in selected_project_skill_paths(target, harnesses):
        copy_skill(path)
    for base in project_skill_base_dirs(target, harnesses):
        remove_skill_dirs(base, LEGACY_SKILLS)
    add_project_guidance(target, harnesses)
    print(f"Installed {SKILL} for project: {target}")
    print(f"Harnesses: {', '.join(harnesses)}")


def install_global(harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> None:
    for path in selected_global_skill_paths(harnesses):
        copy_skill(path)
    for base in global_skill_base_dirs(harnesses):
        remove_skill_dirs(base, LEGACY_SKILLS)
    add_global_guidance(harnesses)
    print(f"Installed {SKILL} globally.")
    print(f"Harnesses: {', '.join(harnesses)}")


def verify_project(target: Path, harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> int:
    target = target.expanduser().resolve()
    failures: list[str] = []
    for path in selected_project_skill_paths(target, harnesses):
        if not (path / "SKILL.md").exists():
            failures.append(f"missing skill: {path / 'SKILL.md'}")

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
        if not file_path.exists():
            failures.append(f"missing guidance file: {file_path}")
            continue
        text = read_text(file_path)
        if text.count(MARKERS[0][0]) != 1 or text.count(MARKERS[0][1]) != 1:
            failures.append(f"expected exactly one Vowline block in {file_path}")

    generated_files: list[Path] = []
    if "cursor" in harnesses:
        generated_files.append(target / ".cursor" / "rules" / "vowline.mdc")
    if "windsurf" in harnesses:
        generated_files.append(target / ".windsurf" / "rules" / "vowline.md")

    for file_path in generated_files:
        text = read_text(file_path)
        if "Vowline" not in text:
            failures.append(f"missing generated guidance: {file_path}")

    for base in project_skill_base_dirs(target, harnesses):
        for legacy in LEGACY_SKILLS:
            if (base / legacy).exists():
                failures.append(f"legacy skill still present: {base / legacy}")

    if failures:
        print("Vowline verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Vowline project install verified: {target}")
    print(f"Harnesses: {', '.join(harnesses)}")
    return 0


def verify_global(harnesses: tuple[str, ...] = SUPPORTED_HARNESSES) -> int:
    failures: list[str] = []
    for path in selected_required_global_skill_paths(harnesses):
        if not (path / "SKILL.md").exists():
            failures.append(f"missing skill: {path / 'SKILL.md'}")

    for path in selected_optional_global_skill_paths(harnesses):
        if (path.exists() or path.is_symlink()) and not (path / "SKILL.md").exists():
            failures.append(f"incomplete optional compatibility mirror: {path}")

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
        if not file_path.exists():
            failures.append(f"missing guidance file: {file_path}")
            continue
        text = read_text(file_path)
        if text.count(MARKERS[0][0]) != 1 or text.count(MARKERS[0][1]) != 1:
            failures.append(f"expected exactly one Vowline block in {file_path}")

    for base in global_skill_base_dirs(harnesses):
        for legacy in LEGACY_SKILLS:
            if (base / legacy).exists():
                failures.append(f"legacy skill still present: {base / legacy}")

    if failures:
        print("Vowline global verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("Vowline global install verified.")
    print(f"Harnesses: {', '.join(harnesses)}")
    return 0


def add_harness_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--harnesses",
        "--agents",
        default="all",
        help=(
            "comma- or space-separated harnesses to install; use all, core, community, "
            "or any of: " + ", ".join(SUPPORTED_HARNESSES)
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Install or verify Vowline across AI agent harnesses.")
    sub = parser.add_subparsers(dest="command", required=True)

    project = sub.add_parser("project", help="install into a repository or project directory")
    project.add_argument("path", nargs="?", default=".", help="project path; defaults to the current directory")
    add_harness_arg(project)

    global_parser = sub.add_parser("global", help="install into the current user's global agent locations")
    add_harness_arg(global_parser)

    verify = sub.add_parser("verify", help="verify a project installation")
    verify.add_argument("path", nargs="?", default=".", help="project path; defaults to the current directory")
    add_harness_arg(verify)

    verify_global_parser = sub.add_parser("verify-global", help="verify the current user's global installation")
    add_harness_arg(verify_global_parser)

    args = parser.parse_args()
    try:
        harnesses = parse_harnesses(args.harnesses)
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))

    if args.command == "project":
        install_project(Path(args.path), harnesses)
    elif args.command == "global":
        install_global(harnesses)
    elif args.command == "verify":
        raise SystemExit(verify_project(Path(args.path), harnesses))
    elif args.command == "verify-global":
        raise SystemExit(verify_global(harnesses))
    else:  # pragma: no cover
        parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()

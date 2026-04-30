from __future__ import annotations

import importlib.util
import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


install = load_module("vowline_install", ROOT / "install.py")
uninstall = load_module("vowline_uninstall", ROOT / "uninstall.py")


class InstallTests(unittest.TestCase):
    def test_project_install_is_idempotent_and_removes_legacy(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "repo"
            project.mkdir()
            (project / "AGENTS.md").write_text(
                "existing\n\n<!-- agent-operating-standard:start -->\nold\n<!-- agent-operating-standard:end -->\n",
                encoding="utf-8",
            )
            (project / "CLAUDE.md").write_text("existing claude\n", encoding="utf-8")
            legacy_agents = project / ".agents" / "skills" / "agent-operating-standard"
            legacy_claude = project / ".claude" / "skills" / "agent-operating-standard"
            legacy_agents.mkdir(parents=True)
            legacy_claude.mkdir(parents=True)

            install.install_project(project)
            install.install_project(project)

            self.assertTrue((project / ".agents" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".claude" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".windsurf" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".cursor" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".gemini" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".github" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".opencode" / "skill" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".goose" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".aider" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".cursor" / "rules" / "vowline.mdc").exists())
            self.assertTrue((project / ".windsurf" / "rules" / "vowline.md").exists())
            self.assertFalse(legacy_agents.exists())
            self.assertFalse(legacy_claude.exists())
            self.assertEqual((project / "AGENTS.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"), 1)
            self.assertEqual((project / "CLAUDE.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"), 1)
            self.assertEqual((project / "GEMINI.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"), 1)
            self.assertEqual(
                (project / ".github" / "copilot-instructions.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"),
                1,
            )
            self.assertEqual(install.verify_project(project), 0)

    def test_project_uninstall_removes_blocks_and_skills(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "repo"
            project.mkdir()
            install.install_project(project)
            uninstall.uninstall_project(project)

            self.assertFalse((project / ".agents" / "skills" / "vowline").exists())
            self.assertFalse((project / ".claude" / "skills" / "vowline").exists())
            self.assertFalse((project / ".windsurf" / "skills" / "vowline").exists())
            self.assertFalse((project / ".cursor" / "skills" / "vowline").exists())
            self.assertFalse((project / ".gemini" / "skills" / "vowline").exists())
            self.assertFalse((project / ".github" / "skills" / "vowline").exists())
            self.assertFalse((project / ".cursor" / "rules" / "vowline.mdc").exists())
            self.assertFalse((project / ".windsurf" / "rules" / "vowline.md").exists())
            self.assertNotIn("<!-- vowline:start -->", (project / "AGENTS.md").read_text(encoding="utf-8"))
            self.assertNotIn("<!-- vowline:start -->", (project / "CLAUDE.md").read_text(encoding="utf-8"))
            self.assertNotIn("<!-- vowline:start -->", (project / "GEMINI.md").read_text(encoding="utf-8"))
            self.assertNotIn("<!-- vowline:start -->", (project / ".github" / "copilot-instructions.md").read_text(encoding="utf-8"))
            self.assertEqual(uninstall.verify_project_removed(project), 0)

    def test_global_install_respects_config_envs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            old_env = {
                key: os.environ.get(key)
                for key in ("HOME", "CODEX_HOME", "CLAUDE_CONFIG_DIR", "WINDSURF_HOME", "CURSOR_HOME", "GEMINI_HOME", "OPENCODE_HOME")
            }
            try:
                os.environ["HOME"] = str(tmp_path / "home")
                os.environ["CODEX_HOME"] = str(tmp_path / "codex")
                os.environ["CLAUDE_CONFIG_DIR"] = str(tmp_path / "claude")
                os.environ["WINDSURF_HOME"] = str(tmp_path / "windsurf")
                os.environ["CURSOR_HOME"] = str(tmp_path / "cursor")
                os.environ["GEMINI_HOME"] = str(tmp_path / "gemini")
                os.environ["OPENCODE_HOME"] = str(tmp_path / "opencode")
                Path(os.environ["HOME"]).mkdir()
                install.install_global()
                install.install_global()

                self.assertTrue((tmp_path / "home" / ".agents" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "codex" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "claude" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "windsurf" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "cursor" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "gemini" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "home" / ".copilot" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "opencode" / "skill" / "vowline" / "SKILL.md").exists())
                self.assertTrue((tmp_path / "home" / ".goose" / "skills" / "vowline" / "SKILL.md").exists())
                self.assertEqual((tmp_path / "codex" / "AGENTS.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"), 1)
                self.assertEqual((tmp_path / "claude" / "CLAUDE.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"), 1)
                self.assertEqual((tmp_path / "gemini" / "GEMINI.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"), 1)
                self.assertEqual((tmp_path / "windsurf" / "memories" / "global_rules.md").read_text(encoding="utf-8").count("<!-- vowline:start -->"), 1)
                self.assertEqual(install.verify_global(), 0)
            finally:
                for key, value in old_env.items():
                    if value is None:
                        os.environ.pop(key, None)
                    else:
                        os.environ[key] = value

    def test_harness_selection_limits_project_targets(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "repo"
            project.mkdir()

            harnesses = install.parse_harnesses("codex,claude")
            install.install_project(project, harnesses)

            self.assertTrue((project / ".agents" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertTrue((project / ".claude" / "skills" / "vowline" / "SKILL.md").exists())
            self.assertFalse((project / ".cursor").exists())
            self.assertFalse((project / ".windsurf").exists())
            self.assertFalse((project / "GEMINI.md").exists())
            self.assertEqual(install.verify_project(project, harnesses), 0)

    def test_codex_global_verify_rejects_skill_without_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            old_env = {key: os.environ.get(key) for key in ("HOME", "CODEX_HOME")}
            try:
                os.environ["HOME"] = str(tmp_path / "home")
                os.environ["CODEX_HOME"] = str(tmp_path / "codex")
                Path(os.environ["HOME"]).mkdir()

                install.copy_skill(tmp_path / "home" / ".agents" / "skills" / "vowline")

                stderr = io.StringIO()
                with contextlib.redirect_stderr(stderr):
                    self.assertEqual(install.verify_global(install.parse_harnesses("codex")), 1)
                self.assertIn("missing guidance file", stderr.getvalue())
            finally:
                for key, value in old_env.items():
                    if value is None:
                        os.environ.pop(key, None)
                    else:
                        os.environ[key] = value

    def test_codex_global_verify_accepts_documented_path_without_compat_mirror(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            old_env = {key: os.environ.get(key) for key in ("HOME", "CODEX_HOME")}
            try:
                os.environ["HOME"] = str(tmp_path / "home")
                os.environ["CODEX_HOME"] = str(tmp_path / "codex")
                Path(os.environ["HOME"]).mkdir()

                install.copy_skill(tmp_path / "home" / ".agents" / "skills" / "vowline")
                install.replace_block(tmp_path / "codex" / "AGENTS.md", install.guidance("AGENTS.md"))

                self.assertFalse((tmp_path / "codex" / "skills" / "vowline").exists())
                self.assertEqual(install.verify_global(install.parse_harnesses("codex")), 0)
            finally:
                for key, value in old_env.items():
                    if value is None:
                        os.environ.pop(key, None)
                    else:
                        os.environ[key] = value

    def test_codex_global_uninstall_removes_skill_paths_and_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            old_env = {key: os.environ.get(key) for key in ("HOME", "CODEX_HOME")}
            try:
                os.environ["HOME"] = str(tmp_path / "home")
                os.environ["CODEX_HOME"] = str(tmp_path / "codex")
                Path(os.environ["HOME"]).mkdir()

                harnesses = install.parse_harnesses("codex")
                install.install_global(harnesses)
                uninstall.uninstall_global(harnesses)

                self.assertFalse((tmp_path / "home" / ".agents" / "skills" / "vowline").exists())
                self.assertFalse((tmp_path / "codex" / "skills" / "vowline").exists())
                self.assertNotIn("<!-- vowline:start -->", (tmp_path / "codex" / "AGENTS.md").read_text(encoding="utf-8"))
                self.assertEqual(uninstall.verify_global_removed(harnesses), 0)
                stderr = io.StringIO()
                with contextlib.redirect_stderr(stderr):
                    self.assertEqual(install.verify_global(harnesses), 1)
                self.assertIn("missing skill", stderr.getvalue())
            finally:
                for key, value in old_env.items():
                    if value is None:
                        os.environ.pop(key, None)
                    else:
                        os.environ[key] = value

    def test_agent_install_docs_require_manual_install_contract(self) -> None:
        required = ("skills/vowline", "guidance/", "generic skill", "documented", "compatibility mirror")
        install_doc = (ROOT / "INSTALL.md").read_text(encoding="utf-8")
        for phrase in required:
            self.assertIn(phrase, install_doc)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("INSTALL.md", readme)
        self.assertIn("INSTALL.md", agents)
        self.assertIn("Verify installation", readme)

    def test_agent_uninstall_docs_require_manual_uninstall_contract(self) -> None:
        required = ("do not only delete one skill directory", "marked vowline")
        uninstall_doc = (ROOT / "UNINSTALL.md").read_text(encoding="utf-8").lower()
        for phrase in required:
            self.assertIn(phrase, uninstall_doc)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        install_doc = (ROOT / "INSTALL.md").read_text(encoding="utf-8")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("UNINSTALL.md", readme)
        self.assertIn("UNINSTALL.md", install_doc)
        self.assertIn("UNINSTALL.md", agents)


if __name__ == "__main__":
    unittest.main()

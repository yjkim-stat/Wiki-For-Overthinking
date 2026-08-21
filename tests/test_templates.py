"""Where a template is read from when the code and the archive are apart.

A deployment keeps its archive in a repository of its own and points a checkout
of this code at it. `templates/` is the one directory that belongs to both: the
code ships a working set, and the deployment is invited to change how its own
artifacts look.

Resolving per file rather than per directory is what lets both be true. A
deployment that overrides one template goes on receiving every other one from
the code it pulls -- copying the whole directory in order to change a heading is
how a deployment stops getting improvements without ever being told.
"""

from __future__ import annotations

import shutil
import unittest

from pipelines import render
from pipelines.common.paths import Layout, REPO_ROOT
from pipelines.publish import TemplateError, load_template

from .sandbox import Sandbox


class TemplateSearchOrderTests(unittest.TestCase):
    def test_in_place_there_is_one_place_to_look(self):
        layout = Layout(root=REPO_ROOT)
        self.assertEqual(layout.template_dirs, [REPO_ROOT / "templates"])

    def test_a_deployment_falls_back_to_the_code(self):
        with Sandbox() as sandbox:
            layout = sandbox.config().layout
            self.assertEqual(
                layout.template_dirs,
                [sandbox.root / "templates", REPO_ROOT / "templates"],
            )

    def test_the_deployment_directory_is_searched_first(self):
        with Sandbox() as sandbox:
            note = sandbox.root / "templates" / "wiki" / "note.md"
            note.write_text("MINE {{TITLE}}\n", encoding="utf-8")
            layout = sandbox.config().layout
            self.assertEqual(
                load_template(layout.template_dirs, "wiki", "note.md"),
                "MINE {{TITLE}}\n",
            )

    def test_a_template_the_deployment_does_not_have_comes_from_the_code(self):
        with Sandbox() as sandbox:
            shutil.rmtree(sandbox.root / "templates")
            layout = sandbox.config().layout
            shipped = (REPO_ROOT / "templates" / "wiki" / "note.md").read_text(
                encoding="utf-8"
            )
            self.assertEqual(
                load_template(layout.template_dirs, "wiki", "note.md"), shipped
            )

    def test_a_single_directory_is_still_accepted(self):
        shipped = REPO_ROOT / "templates"
        self.assertTrue(load_template(shipped, "wiki", "note.md"))

    def test_a_template_in_neither_place_names_both(self):
        with Sandbox() as sandbox:
            layout = sandbox.config().layout
            with self.assertRaises(TemplateError) as caught:
                load_template(layout.template_dirs, "wiki", "no-such.md")
            message = str(caught.exception)
            self.assertIn(str(sandbox.root), message)
            self.assertIn(str(REPO_ROOT), message)


class RenderWithoutDeploymentTemplatesTests(unittest.TestCase):
    """The case the fallback exists for, end to end.

    A freshly created archive repository holds config and nothing else. Before
    the fallback, its first render died on a missing `templates/wiki/note.md`
    -- with everything else about the deployment correct.
    """

    def test_render_completes_with_no_templates_in_the_deployment(self):
        with Sandbox() as sandbox:
            shutil.rmtree(sandbox.root / "templates")
            cfg = sandbox.config()
            result = render.run(cfg)
            self.assertEqual(result["outputs"]["lecture_notes"], 1)
            self.assertTrue((sandbox.root / "wiki" / "index.md").exists())
            self.assertFalse((sandbox.root / "templates").exists())


if __name__ == "__main__":
    unittest.main()

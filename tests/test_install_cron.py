"""Scheduling one deployment without disturbing anything else on the host.

A crontab is shared state. It holds jobs this repository knows nothing about,
written by somebody who will not be watching when our installer runs, and the
failure that matters is not "the entry was wrong" -- it is "the backup job is
gone". So the properties asserted here are mostly about what the script leaves
alone: unrelated lines survive, a second install replaces rather than appends,
and a crontab that could not be *read* is never *written*.

The tests drive a stub `crontab` binary through `RA_WM_CRONTAB_CMD`. Nothing
here touches the real one, which is also why the stub can be made to fail in
ways a real crontab would only fail on somebody else's machine.
"""

from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from pipelines.common.paths import REPO_ROOT

SCRIPT = REPO_ROOT / "scripts" / "install-cron.sh"

STUB = """#!/usr/bin/env bash
F="${FAKE_CRONTAB_FILE:?}"
case "$1" in
  -l) [ -s "$F" ] || { echo "no crontab for tester" >&2; exit 1; }; cat "$F" ;;
  -)  cat > "$F" ;;
  *)  echo "unexpected: $*" >&2; exit 9 ;;
esac
"""

# A crontab that cannot be read for a reason that is not "there isn't one".
BROKEN = """#!/usr/bin/env bash
case "$1" in
  -l) echo "crontab: cannot open /var/spool/cron: Permission denied" >&2; exit 1 ;;
  -)  cat > "${FAKE_CRONTAB_FILE:?}" ;;
esac
"""

UNRELATED = "30 2 * * * /usr/bin/backup.sh\n"


class InstallCronTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)

        self.crontab_file = base / "crontab.txt"
        self.crontab_file.write_text(UNRELATED, encoding="utf-8")

        self.stub = base / "stub-crontab"
        self.stub.write_text(STUB, encoding="utf-8")
        self.stub.chmod(0o755)

        self.broken = base / "broken-crontab"
        self.broken.write_text(BROKEN, encoding="utf-8")
        self.broken.chmod(0o755)

        self.root = base / "archive"
        self.root.mkdir()
        self.other = base / "archive2"
        self.other.mkdir()

    def _run(self, *argv: str, crontab: Path | None = None) -> subprocess.CompletedProcess:
        env = dict(os.environ)
        env["RA_WM_CRONTAB_CMD"] = str(crontab or self.stub)
        env["FAKE_CRONTAB_FILE"] = str(self.crontab_file)
        env.pop("RA_WM_ROOT", None)
        return subprocess.run(
            ["bash", str(SCRIPT), *argv],
            capture_output=True, text=True, env=env, cwd=str(REPO_ROOT),
        )

    def _crontab(self) -> str:
        return self.crontab_file.read_text(encoding="utf-8")

    # -- printing ------------------------------------------------------------
    def test_print_writes_a_line_and_changes_nothing(self):
        before = self._crontab()
        proc = self._run("--root", str(self.root), "--print")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("daily.sh", proc.stdout)
        self.assertIn(str(self.root), proc.stdout)
        self.assertEqual(self._crontab(), before)

    def test_the_interpreter_is_pinned_to_an_absolute_path(self):
        """cron's PATH is not a login shell's.

        A line carrying a bare `python3` installs cleanly and then fails every
        night into a log nobody has started reading yet, which is the worst
        shape a scheduling bug can take.
        """
        proc = self._run("--root", str(self.root), "--print")
        command = [ln for ln in proc.stdout.splitlines() if "daily.sh" in ln][0]
        self.assertRegex(command, r"PYTHON='/")

    def test_the_schedule_reaches_the_line(self):
        proc = self._run("--root", str(self.root), "--at", "15 4 * * 1", "--print")
        self.assertIn("15 4 * * 1 ", proc.stdout)

    # -- installing ----------------------------------------------------------
    def test_installing_keeps_the_jobs_it_did_not_write(self):
        self._run("--root", str(self.root))
        self.assertIn("/usr/bin/backup.sh", self._crontab())

    def test_installing_twice_replaces_rather_than_appends(self):
        self._run("--root", str(self.root), "--at", "0 7 * * *")
        self._run("--root", str(self.root), "--at", "0 9 * * *")
        body = self._crontab()
        self.assertEqual(body.count("daily.sh"), 1)
        self.assertIn("0 9 * * *", body)
        self.assertNotIn("0 7 * * *", body)

    def test_two_deployments_coexist(self):
        """The tag carries the root, so one host can serve two archives."""
        self._run("--root", str(self.root))
        self._run("--root", str(self.other))
        body = self._crontab()
        self.assertEqual(body.count("daily.sh"), 2)
        self.assertIn(str(self.root), body)
        self.assertIn(str(self.other), body)

    def test_an_empty_crontab_gains_exactly_the_entry(self):
        self.crontab_file.write_text("", encoding="utf-8")
        self._run("--root", str(self.root))
        lines = [ln for ln in self._crontab().splitlines() if ln.strip()]
        self.assertEqual(len(lines), 2, lines)  # the tag comment and the job

    # -- removing ------------------------------------------------------------
    def test_removing_takes_only_its_own(self):
        self._run("--root", str(self.root))
        self._run("--root", str(self.other))
        self._run("--root", str(self.other), "--remove")
        body = self._crontab()
        self.assertEqual(body.count("daily.sh"), 1)
        self.assertIn(str(self.root), body)
        self.assertNotIn(str(self.other), body)
        self.assertIn("/usr/bin/backup.sh", body)

    def test_removing_what_was_never_installed_is_not_an_error(self):
        proc = self._run("--root", str(self.root), "--remove")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(self._crontab(), UNRELATED)

    # -- refusing ------------------------------------------------------------
    def test_a_crontab_that_cannot_be_read_is_never_written(self):
        """The one that would cost somebody else their job.

        `crontab -l` failing because there is no crontab yet is ordinary. It
        failing for any other reason means we do not know what is in there, and
        installing our line would replace the file with only our line.
        """
        before = self._crontab()
        proc = self._run("--root", str(self.root), crontab=self.broken)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("nothing was changed", proc.stderr)
        self.assertEqual(self._crontab(), before)

    def test_a_schedule_of_the_wrong_shape_is_refused(self):
        before = self._crontab()
        proc = self._run("--root", str(self.root), "--at", "0 8 * *")
        self.assertEqual(proc.returncode, 2)
        self.assertEqual(self._crontab(), before)

    def test_a_root_that_does_not_exist_is_refused(self):
        proc = self._run("--root", str(Path(self.tmp.name) / "nope"))
        self.assertEqual(proc.returncode, 2)
        self.assertIn("--force", proc.stderr)

    def test_force_schedules_a_root_that_is_not_there_yet(self):
        target = Path(self.tmp.name) / "nope"
        proc = self._run("--root", str(target), "--force", "--print")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn(str(target), proc.stdout)

    def test_a_percent_in_a_path_is_refused(self):
        """cron reads an unescaped % as a newline and truncates the command."""
        odd = Path(self.tmp.name) / "arch%ive"
        odd.mkdir()
        proc = self._run("--root", str(odd))
        self.assertEqual(proc.returncode, 2)
        self.assertIn("%", proc.stderr)

    def test_collecting_into_the_code_checkout_says_so(self):
        """Not refused -- the single-tree layout is supported. But it is the
        choice that quietly mixes an archive into the repository framework
        updates are pulled into, so it is never made silently."""
        proc = self._run("--print")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("code", proc.stderr.lower())


if __name__ == "__main__":
    unittest.main()

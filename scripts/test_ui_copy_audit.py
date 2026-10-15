"""Minimal tests for the optional static UI copy audit."""

import tempfile
import unittest
from pathlib import Path

from ui_copy_audit import scan


class CopyAuditTests(unittest.TestCase):
    def test_detects_promotional_copy(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "App.tsx"
            path.write_text('<h1>Your command center</h1>\n<p>Unlock insights</p>', encoding="utf-8")
            matches = scan(Path(folder))
            self.assertEqual(2, len(matches))
            self.assertEqual({"fluffy_heading", "marketing_claim"}, {m["rule"] for m in matches})

    def test_accepts_real_workflow_copy(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "App.tsx"
            path.write_text('<h1>Pending Cases</h1>\n<button>Request Documents</button>', encoding="utf-8")
            self.assertEqual([], scan(Path(folder)))

    def test_ignores_non_ui_files(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "README.md"
            path.write_text('Unlock insights', encoding="utf-8")
            self.assertEqual([], scan(Path(folder)))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Find likely AI-marketing filler in enterprise UI source code.

Run: python scripts/ui_copy_audit.py PATH [--strict] [--json]
Heuristic only: review matches in UI context; a literal match is not proof.
No third-party dependencies, no network access, no file modifications.
"""

import argparse
import json
import re
import sys
from pathlib import Path

UI_EXTS = {
    ".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte",
    ".kt", ".xml", ".json", ".arb", ".strings",
}
SKIP_DIRS = {
    ".git", ".next", ".nuxt", "node_modules", "dist", "build", "out",
    "coverage", "vendor", "venv", ".venv", "target", "__pycache__",
}
MAX_BYTES = 1_000_000

# Match high-signal promotional copy, not ordinary operational words.
PATTERNS = (
    ("marketing_claim", re.compile(r"\b(?:unlock (?:the |your )?(?:power|potential|insights)|"
                                    r"unleash (?:the |your )?(?:power|potential)|"
                                    r"redefin(?:e|ing) (?:the way|productivity)|"
                                    r"supercharge (?:your|the)|"
                                    r"work smarter,? not harder)\b", re.I)),
    ("fluffy_heading", re.compile(r"\b(?:your (?:ultimate )?command cent(?:er|re)|"
                                  r"everything you need in one place|"
                                  r"one place to (?:manage|track|see)|"
                                  r"stay (?:ahead of|on top of) what matters|"
                                  r"the future of (?:smarter|seamless)|"
                                  r"operational excellence|"
                                  r"at your fingertips)\b", re.I)),
    ("vague_promise", re.compile(r"\b(?:empowering smarter|"
                                  r"seamless(?:ly)? (?:experience|workflow|collaboration)|"
                                  r"transform (?:how|the way) you|"
                                  r"manage (?:it|everything) with ease|"
                                  r"smarter decisions start here|"
                                  r"experience (?:the|a) next level)\b", re.I)),
)


def source_files(path: Path):
    if path.is_file():
        if path.suffix.lower() in UI_EXTS:
            yield path
        return
    for candidate in path.rglob("*"):
        if not candidate.is_file() or candidate.suffix.lower() not in UI_EXTS:
            continue
        if any(part in SKIP_DIRS or part.startswith(".") for part in candidate.relative_to(path).parts[:-1]):
            continue
        yield candidate


def scan(root: Path):
    results = []
    for file in source_files(root):
        try:
            if file.stat().st_size > MAX_BYTES:
                continue
            data = file.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            continue
        for line_no, line in enumerate(data.splitlines(), start=1):
            for rule, regex in PATTERNS:
                for match in regex.finditer(line):
                    results.append({
                        "path": str(file),
                        "line": line_no,
                        "column": match.start() + 1,
                        "rule": rule,
                        "match": match.group(0),
                        "context": line.strip()[:180],
                    })
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="UI source directory or file")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if possible filler is found")
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    args = parser.parse_args(argv)
    if not args.path.exists():
        parser.error("Path does not exist: " + str(args.path))

    findings = scan(args.path)
    if args.json:
        print(json.dumps({"count": len(findings), "findings": findings}, indent=2))
    else:
        for finding in findings:
            print("{path}:{line}:{column}: {rule}: {match}".format(**finding))
        print("Potential UI-copy issues: {}. Review context manually.".format(len(findings)))
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    sys.exit(main())

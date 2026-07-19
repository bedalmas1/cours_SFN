#!/usr/bin/env python3
"""Build a session working prompt from the numbered syllabus section."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADINGS = re.compile(
    r"^###\s+Séquence\s+([1-8])\s*[-–—]\s*(.+?)\s*$", re.MULTILINE
)
OBJECTIVE = re.compile(
    r"^Objectif général\s*:\s*(.+?)(?=\n\s*\n)", re.MULTILINE | re.DOTALL
)
MARKERS = (
    "[INSÉRER LE TITRE DE LA SÉQUENCE]",
    "[INSÉRER L’OBJECTIF GÉNÉRAL]",
    "[INSÉRER LE DÉROULÉ PRÉVU OU LE COPIER DEPUIS LE SYLLABUS]",
)


class PreparationError(Exception):
    """Report invalid input or an incompatible repository structure."""


def project_root(start: Path) -> Path:
    """Find the closest ancestor containing the required course files."""
    for path in (start.resolve(), *start.resolve().parents):
        required = (
            path / "syllabus" / "syllabus_overall.md",
            path / "syllabus" / "template_sequence.md",
            path / "sessions",
        )
        if all(candidate.exists() for candidate in required):
            return path
    raise PreparationError("Could not find the course-iot-decision root.")


def extract(text: str, number: int) -> tuple[str, str, str]:
    """Extract the title, objective, and remaining details for a sequence."""
    headings = list(HEADINGS.finditer(text))
    index = next(
        (i for i, heading in enumerate(headings) if int(heading.group(1)) == number),
        None,
    )
    if index is None:
        raise PreparationError(f"Sequence {number} was not found in the syllabus.")
    heading = headings[index]
    end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
    section = text[heading.end():end].strip()
    next_section = re.search(r"^##\s+", section, re.MULTILINE)
    if next_section:
        section = section[:next_section.start()].rstrip()
    objective_match = OBJECTIVE.search(section)
    if not objective_match:
        raise PreparationError(f"Sequence {number} has no general objective.")
    objective = " ".join(objective_match.group(1).split())
    details = (
        section[:objective_match.start()] + section[objective_match.end():]
    ).strip()
    if not details:
        raise PreparationError(f"Sequence {number} has no detailed schedule.")
    return heading.group(2).strip(), objective, details


def fill(template: str, title: str, objective: str, details: str) -> str:
    """Replace each required placeholder exactly once."""
    for marker in MARKERS:
        if template.count(marker) != 1:
            raise PreparationError(f"Expected one template marker: {marker}")
    return (
        template.replace(MARKERS[0], title)
        .replace(MARKERS[1], objective)
        .replace(MARKERS[2], details)
    )


def session_dir(root: Path, number: int) -> Path:
    matches = [p for p in (root / "sessions").glob(f"s{number:02d}_*") if p.is_dir()]
    if len(matches) != 1:
        raise PreparationError(
            f"Expected one sessions/s{number:02d}_* directory; found {len(matches)}."
        )
    return matches[0]


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fill the course sequence template from the numbered syllabus section."
    )
    parser.add_argument("number", type=int, choices=range(1, 9))
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = arguments()
    try:
        root = args.project_root.resolve() if args.project_root else project_root(Path.cwd())
        syllabus = (root / "syllabus" / "syllabus_overall.md").read_text("utf-8")
        template = (root / "syllabus" / "template_sequence.md").read_text("utf-8")
        title, objective, details = extract(syllabus, args.number)
        generated = fill(template, title, objective, details)
        if args.stdout:
            sys.stdout.buffer.write(generated.encode("utf-8"))
            return 0

        output = args.output.resolve() if args.output else session_dir(
            root, args.number
        ) / "sequence_prompt.md"
        if output.exists() and not args.force:
            raise PreparationError(f"Refusing to overwrite {output}; use --force.")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(generated, encoding="utf-8", newline="\n")
        print(f"Prepared sequence {args.number}: {title}")
        print(f"Objective: {objective}")
        print(f"Output: {output}")
        return 0
    except (OSError, PreparationError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

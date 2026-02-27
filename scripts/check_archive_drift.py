# -*- coding: utf-8 -*-
"""CI check: every archived OpenSpec change's deltas must be reflected in the
current capability specs.

Structural check only: for each archived change we require every
ADDED/MODIFIED/REMOVED requirement heading named in its delta file to be
consistent with the capability spec it targets. We deliberately do not
attempt a semantic diff of requirement prose.
"""
import os
import re
import sys

SECTION_RE = re.compile(r"^## (ADDED|MODIFIED|REMOVED) Requirements\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^### Requirement: (.+)$", re.MULTILINE)


def extract_requirement_headings(delta_text):
    """Pure: [(action, requirement_title), ...] -- the action is the
    enclosing ## ADDED/MODIFIED/REMOVED Requirements section."""
    out, action = [], None
    for line in delta_text.splitlines():
        m = SECTION_RE.match(line)
        if m:
            action = m.group(1); continue
        t = TITLE_RE.match(line)
        if t and action:
            out.append((action, t.group(1).strip()))
    return out


def find_drifted_requirements(delta_headings, capability_spec_text):
    """Pure: which ADDED/MODIFIED requirement titles are missing from the
    capability spec text.
    """
    drifted = []
    for action, title in delta_headings:
        if action not in ("ADDED", "MODIFIED"):
            continue
        if title not in capability_spec_text:
            drifted.append((action, title))
    return drifted


def check_archive_drift(archived_changes):
    """Pure: archived_changes is [{'delta_text':..., 'capability_spec_text':...}, ...].

    Returns the full list of drifted (change_index, action, title) tuples.
    """
    drift = []
    for idx, change in enumerate(archived_changes):
        headings = extract_requirement_headings(change["delta_text"])
        for action, title in find_drifted_requirements(headings, change["capability_spec_text"]):
            drift.append((idx, action, title))
    return drift


def main():
    # Real filesystem walk of openspec/changes/archive and openspec/specs
    # lives here; kept out of the pure functions above.
    archive_dir = "openspec/changes/archive"
    specs_dir = "openspec/specs"
    archived_changes = []
    if os.path.isdir(archive_dir):
        for change_id in sorted(os.listdir(archive_dir)):
            delta_path = os.path.join(archive_dir, change_id, "delta.md")
            if not os.path.exists(delta_path):
                continue
            with open(delta_path) as f:
                delta_text = f.read()
            capability = change_id.split("-")[0]
            spec_path = os.path.join(specs_dir, capability, "spec.md")
            spec_text = ""
            if os.path.exists(spec_path):
                with open(spec_path) as f:
                    spec_text = f.read()
            archived_changes.append({"delta_text": delta_text, "capability_spec_text": spec_text})

    drift = check_archive_drift(archived_changes)
    if drift:
        print("METRIC archive_drift_detected=1 count=%d" % len(drift))
        for idx, action, title in drift:
            print("drift: change #%d %s Requirement - %s not reflected in capability spec" % (idx, action, title))
        return 1
    print("METRIC archive_drift_detected=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())

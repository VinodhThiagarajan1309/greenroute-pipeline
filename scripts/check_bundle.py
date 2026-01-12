"""Structural check of databricks.yml.

`databricks bundle validate` needs a workspace and a token, so it belongs in the
deploy pipeline, not in a pull-request check. What a PR CAN tell us is whether
the bundle file still declares every target correctly -- which is the failure
we actually keep hitting.
"""
import sys

import yaml

REQUIRED_TARGETS = ("dev", "staging", "prod")


def main():
    with open("databricks.yml") as fh:
        cfg = yaml.safe_load(fh)

    problems = []
    if not cfg.get("bundle", {}).get("name"):
        problems.append("bundle.name is missing")

    targets = cfg.get("targets") or {}
    for name in REQUIRED_TARGETS:
        target = targets.get(name)
        if target is None:
            problems.append("target %r is not declared" % name)
            continue
        workspace = target.get("workspace") or {}
        if not workspace.get("host"):
            problems.append("target %r has no workspace host" % name)

    prod = targets.get("prod") or {}
    if prod.get("mode") != "production":
        problems.append("target 'prod' must set mode: production")

    if problems:
        for p in problems:
            print("databricks.yml: %s" % p)
        return 1
    print("databricks.yml: %d targets declared, all valid" % len(targets))
    return 0


if __name__ == "__main__":
    sys.exit(main())

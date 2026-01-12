"""GreenRoute pipeline package.

Capabilities live one package per concept under `greenroute`:

- `common` -- shared Spark I/O and metrics helpers, used by every capability. Not
  specific to any one of them; if it's specific, it doesn't belong here.

As capabilities land (scheduling, service catalog, payments, and so on) they get
their own subpackage under `greenroute`. Keep this docstring's list current -- it
is the map of what this package owns.
"""

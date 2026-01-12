"""Shared helpers used by every GreenRoute capability.

Nothing in this package is specific to one capability. If you're about to add
something that only one capability cares about, it belongs in that capability's
own package, not here.

The I/O helpers are re-exported here so capability modules can write
``from greenroute.common import read_table``. The re-export is lazy on purpose:
importing this package must not pull in pyspark, because the pure decision
functions -- and the tests that cover them -- do not need a Spark session.
"""

_IO_NAMES = ("spark_session", "read_table", "write_table", "quarantine", "LAYERS")


def __getattr__(name):
    if name in _IO_NAMES:
        from greenroute.common import io
        return getattr(io, name)
    raise AttributeError("module %r has no attribute %r" % (__name__, name))


def __dir__():
    return sorted(list(globals()) + list(_IO_NAMES))

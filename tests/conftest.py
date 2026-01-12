"""Shared pytest fixtures.

No SparkSession fixture here on purpose: for now the suite only exercises pure
functions (see `src/greenroute/common/io.py` and
`src/greenroute/common/metrics.py`), and starting a SparkSession per test run
would make CI slow for no benefit yet.
"""
import pytest

from greenroute.common import metrics


@pytest.fixture(autouse=True)
def reset_metrics_registry():
    """Reset the in-process metrics registry before and after every test.

    Autouse so no test can accidentally see another test's emitted metrics.
    """
    metrics.reset()
    yield
    metrics.reset()

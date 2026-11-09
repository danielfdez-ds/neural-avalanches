"""Smoke tests: verify the test infrastructure works from day one.

Real tests arrive in Hito 2; for now CI just needs something green
to run (pytest exits with code 5 when it finds zero tests, which
GitHub Actions treats as a failure).
"""


def test_ci_pipeline_works():
    """Trivial by design: green CI before real tests exist."""
    assert 2 + 2 == 4

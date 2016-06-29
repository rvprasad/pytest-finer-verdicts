import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Treat non-assertion failures as test errors."""
    outcome = yield
    test_report = outcome.get_result()

    if call.excinfo and test_report.outcome == 'failed':
        when = call.when
        excinfo = call.excinfo
        if call.when == "call" and \
                isinstance(excinfo.value, AssertionError):
            longrepr = item.repr_failure(excinfo)
        else:
            when = 'setup' if when == 'call' else when
            longrepr = item._repr_failure_py(excinfo,
                                             style=item.config.option.tbstyle)
        test_report.longrepr = longrepr
        test_report.when = when

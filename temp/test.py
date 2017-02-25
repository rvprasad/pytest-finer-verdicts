import pytest


def test_pass():
    assert 70 <= 75


def test_fail():
    assert 75 <= 70


def test_error():
    raise RuntimeError()


def test_pytest_fail():
    pytest.fail("Fail")


def test_pytest_raises():
    with pytest.raises(ValueError):
        raise IndexError()

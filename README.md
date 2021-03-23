# pytest-finer-verdicts
A pytest plugin to treat non-assertion failures as test errors.

# Getting the plugin 
The plugin can be installed via `pip install pytest-finer-verdicts`.  Similarly, it can be uninstalled via `pip uninstall pytest-finer-verdicts`.

## Usage
Consider the following snippet in a file _test.py_ (available as _temp/test.py_ in the repository).
```
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
```
**With pytest-finer-verdicts plugin**, `py.test test.py -v` will produce the following output.
```
collected 5 items 

test.py::test_pass PASSED
test.py::test_fail FAILED
test.py::test_error ERROR
test.py::test_pytest_fail FAILED
test.py::test_pytest_raises ERROR

================================== ERRORS ===================================
_______________________ ERROR at setup of test_error ________________________

    def test_error():
>       raise RuntimeError()
E       RuntimeError

test.py:13: RuntimeError
___________________ ERROR at setup of test_pytest_raises ____________________

    def test_pytest_raises():
        with pytest.raises(ValueError):
>           raise IndexError()
E           IndexError

test.py:22: IndexError
================================= FAILURES ==================================
_________________________________ test_fail _________________________________

    def test_fail():
>       assert 75 <= 70
E       assert 75 <= 70

test.py:9: AssertionError
_____________________________ test_pytest_fail ______________________________

    def test_pytest_fail():
>       pytest.fail("Fail")
E       Failed: Fail

test.py:17: Failed
================ 2 failed, 1 passed, 2 error in 0.05 seconds ================
```

Notice how `test_error` and `test_pytest_raises` are flagged as _test errors_ by the plugin.


## Attribution

Copyright (c) 2016-2018, Venkatesh-Prasad Ranganath, Christer Jansson

Licensed under BSD 3-clause "New" or "Revised" License (https://choosealicense.com/licenses/bsd-3-clause/)

**Authors:** Venkatesh-Prasad Ranganath, Christer Jansson

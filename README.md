# pytest-finer-verdicts
A pytest plugin to treat non-assertion failures as test errors.

# Getting the plugin 
The plugin can be installed via `pip install pytest-finer-verdicts`.  Similarly, it can be uninstalled via `pip uninstall pytest-finer-verdicts`.

## Usage
Consider the following snippet in a file _test.py_.
```
class Engine:
    def rotations(self):
        return 51
    def getTemp(self):
        return 75


def test_pass():
    o = Engine()
    while o.rotations() < 50:
        pass
    assert o.getTemp() <= 75


def test_fail():
    o = Engine()
    while o.rotations() < 50:
        pass
    assert o.getTemp() <= 70


def test_error():
    o = Engine()
    while o.rotations() < 50:
        pass
    raise RuntimeError()
    assert o.getTemp() <= 75
```
**Without pytest-finer-verdicts**, `py.test test.py -v` will produce the following output.

```
collected 3 items

test.py::test_pass PASSED
test.py::test_fail FAILED
test.py::test_error FAILED

=================================== FAILURES ===================================
__________________________________ test_fail ___________________________________

    def test_fail():
        o = Engine()
        while o.rotations() < 50:
            pass
>       assert o.getTemp() <= 70
E       assert 75 <= 70
E        +  where 75 = <bound method Engine.getTemp of <test.Engine object at 0x10597c6a0>>()
E        +    where <bound method Engine.getTemp of <test.Engine object at 0x10597c6a0>> = <test.Engine object at 0x10597c6a0>.getTemp

test.py:19: AssertionError
__________________________________ test_error __________________________________

    def test_error():
        o = Engine()
        while o.rotations() < 50:
            pass
>       raise RuntimeError()
E       RuntimeError

test.py:26: RuntimeError
====================== 2 failed, 1 passed in 0.04 seconds ======================
```

**With pytest-finer-verdicts plugin**, `py.test test.py -v` will produce the following output.
```
    collected 3 items

    test.py::test_pass PASSED
    test.py::test_fail FAILED
    test.py::test_error ERROR

    ==================================== ERRORS ====================================
    _________________________ ERROR at setup of test_error _________________________

        def test_error():
            o = Engine()
            while o.rotations() < 50:
                pass
    >       raise RuntimeError()
    E       RuntimeError

    test.py:26: RuntimeError
    =================================== FAILURES ===================================
    __________________________________ test_fail ___________________________________

        def test_fail():
            o = Engine()
            while o.rotations() < 50:
                pass
    >       assert o.getTemp() <= 70
    E       assert 75 <= 70
    E        +  where 75 = <bound method Engine.getTemp of <test.Engine object at 0x105885e80>>()
    E        +    where <bound method Engine.getTemp of <test.Engine object at 0x105885e80>> = <test.Engine object at 0x105885e80>.getTemp

    test.py:19: AssertionError
    ================= 1 failed, 1 passed, 1 error in 0.04 seconds ==================
```

Notice how `test_error` is flagged as a _test error_ by the plugin.

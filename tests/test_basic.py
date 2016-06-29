class TestBasic:
    def test_pass(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def test_pass(self):
                    assert 1 == 1
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_pass PASSED"])

    def test_failure(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def test_fail(self):
                    assert 1 == 2
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_fail FAILED"])

    def test_error(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def test_error(self):
                    raise RuntimeError("Boom")
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_error ERROR"])

    def test_skip(self, testdir):
        testdir.makepyfile("""
            import pytest
            class TestClass():
                def test_pass(self):
                    assert 1 == 1

                @pytest.mark.skip
                def test_skip(self):
                    assert 1 == 2
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines([
            "*TestClass::test_pass PASSED",
            "*TestClass::test_skip SKIPPED"])

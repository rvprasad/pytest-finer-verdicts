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

    def test_pytest_fail(self, testdir):
        testdir.makepyfile("""
            import pytest
            class TestClass():
                def test_pytest_fail(self):
                    pytest.fail("PyTest.Fail")
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*Failed: PyTest.Fail"])

    def test_pytest_raises_passed(self, testdir):
        testdir.makepyfile("""
            import pytest
            class TestClass():
                def test_pytest_raises(self):
                    with pytest.raises(ValueError):
                        raise ValueError()
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*test_pytest_raises PASSED"])

    def test_pytest_raises_error(self, testdir):
        testdir.makepyfile("""
            import pytest
            class TestClass():
                def test_pytest_raises(self):
                    with pytest.raises(ValueError):
                        raise IndexError()
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*test_pytest_raises ERROR"])

    def test_pytest_raises_failed(self, testdir):
        testdir.makepyfile("""
            import pytest
            class TestClass():
                def test_pytest_raises(self):
                    with pytest.raises(ValueError):
                        pass
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*test_pytest_raises FAILED"])

    def test_pass_with_fixtures(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def setup(self):
                    print("setup")

                def teardown(self):
                    print("teardown")

                def test_pass(self):
                    assert 1 == 1
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_pass PASSED"])

    def test_failure_with_fixtures(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def setup(self):
                    print("setup")

                def teardown(self):
                    print("teardown")

                def test_fail(self):
                    assert 1 == 2
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_fail FAILED"])

    def test_error_with_fixtures(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def setup(self):
                    print("setup")

                def teardown(self):
                    print("teardown")

                def test_error(self):
                    raise RuntimeError("Boom")
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_error ERROR"])

    def test_skip_with_fixtures(self, testdir):
        testdir.makepyfile("""
            import pytest
            class TestClass():
                def setup(self):
                    print("setup")

                def teardown(self):
                    print("teardown")

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

    def test_pytest_fail_with_fixtures(self, testdir):
        testdir.makepyfile("""
            import pytest
            class TestClass():
                def setup(self):
                    print("setup")

                def teardown(self):
                    print("teardown")

                def test_pytest_fail(self):
                    pytest.fail("PyTest.Fail")
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*Failed: PyTest.Fail"])

    def test_failure_in_setup(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def setup(self):
                    assert 1 == 2

                def test_pass(self):
                    assert 1 == 1
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_pass ERROR"])

    def test_failure_in_teardown(self, testdir):
        testdir.makepyfile("""
            class TestClass():
                def teardown(self):
                    assert 1 == 2

                def test_pass(self):
                    assert 1 == 1
        """)
        result = testdir.runpytest("-v")
        result.stdout.fnmatch_lines(["*TestClass::test_pass ERROR"])

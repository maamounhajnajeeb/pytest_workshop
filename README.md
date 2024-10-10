This readme is inspired by this [workshop](https://www.youtube.com/watch?v=ofPHJrAOaTE&t=2027s)

## Pytest command helper flags:
- -v: stands for verbose output
    explanation: increase pytest's verbosity, [docs link](https://docs.pytest.org/en/8.3.x/how-to/output.html#verbosity)
- -x: exist instantly on the first failure
- --collect-only: only show which tests were collected
- --lf/--ff:</br>
    1] --lf, --last-failed - to only re-run the failures.</br>
    2] --ff, --failed-first - to run the failures first and then the rest of the tests.</br>
    [docs link](https://docs.pytest.org/en/stable/how-to/cache.html#how-to-re-run-failed-tests-and-maintain-state-between-test-runs)
- --tb: Control traceback generation
    this flag accepts one positional argument: \[long, short, line, and more...\]
    see argument option and more on [this link](https://docs.pytest.org/en/8.3.x/how-to/output.html#modifying-python-traceback-printing)
- -l: show local variables in tracebacks
- -s: disable stdout capturing, [docs link](https://docs.pytest.org/en/8.3.x/how-to/output.html#modifying-python-traceback-printing)


## Pytest pytest.ini file settings:
### addopts: (stands for add options)
This settings can hold any number of the previous flags, and it will apply it automatically when testing(kind of presistent options throught the tests).</br>
[docs link](https://docs.pytest.org/en/stable/reference/reference.html#confval-addopts)

#### example:
in you pytest.ini file if addopts like this:</br>
addopts = -v</br>
this means when you are running: pytest path/to/test/unit</br>
you are doing this: pytest path/to/test/unit -v


## Asserting expected exceptions
full details on: [docs link](https://docs.pytest.org/en/stable/how-to/assert.html#matching-exception-messages)</br>
note: read more about match attribute within the context manager.

small example
```python
def divide(x, y):
    return x / y

def test_raises():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)
```


## Custom Markers
Multiple custom markers can be registered, by defining each one in its own line, as shown in the below example.
```ini
# content of pytest.ini
[pytest]
markers =
    webtest: mark a test as a webtest.
    slow: mark test as slow.
```

You can ask which markers exist for your test suite:
```shell
$ pytest --markers
@pytest.mark.webtest: mark a test as a webtest.
@pytest.mark.slow: mark test as slow.
```

ok, what's all about, why to use markers?
we can do this:
```python
import pytest

@pytest.mark.webtest
def test_property_api():
    return ....
```

then in our terminal we can run tests that marked as webtest only, not the whole tests, like this:
```shell
pytest path/to/your/tests -m "webtest"
```

or if you want to disable tests to one of the marked tests, just do:
```shell
pytest path/to/your/tests -m "no webtest"
```

You can add -v to test command to show which tests are run


## Dealing with tests that cannot succeed with skipif and xfail
full details on: [docs link](https://docs.pytest.org/en/stable/how-to/skipping.html)</br>
You can mark test functions that cannot be run on certain platforms or that you expect to fail so pytest can deal with them accordingly and present a summary of the test session, while keeping the test suite green.

A skip means that you expect your test to pass only if some conditions are met, otherwise pytest should skip running the test altogether. Common examples are skipping windows-only tests on non-windows platforms, or skipping tests that depend on an external resource which is not available at the moment (for example a database).

An xfail means that you expect a test to fail for some reason. A common example is a test for a feature not yet implemented, or a bug not yet fixed. When a test passes despite being expected to fail (marked with pytest.mark.xfail), it’s an xpass and will be reported in the test summary.

```shell
pytest -rxXs  # show extra info on xfailed, xpassed, and skipped tests
```

### Skipping test functions
```python
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown(): ...
```

```python
@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_function(): ...
```

### XFail: mark test functions as expected to fail
```shell
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_function(): ...
```


## Parametrizing Tests
Parametrizing is type of markers


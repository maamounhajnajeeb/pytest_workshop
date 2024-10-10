This readme is inspired by this [workshop](https://www.youtube.com/watch?v=ofPHJrAOaTE&t=2027s)

## Pytest command helper flags:
- -v: stands for verbose output
    explanation: increase pytest's verbosity, [docs link](https://docs.pytest.org/en/8.3.x/how-to/output.html#verbosity)
- -x: exist instantly on the first failure
- --collect-only: only show which tests were collected
- --lf/--ff:
    1] --lf, --last-failed - to only re-run the failures.
    2] --ff, --failed-first - to run the failures first and then the rest of the tests.
    [docs link](https://docs.pytest.org/en/stable/how-to/cache.html#how-to-re-run-failed-tests-and-maintain-state-between-test-runs)
- --tb: Control traceback generation
    this flag accepts one positional argument: \[long, short, line, and more...\]
    see argument option and more on [this link](https://docs.pytest.org/en/8.3.x/how-to/output.html#modifying-python-traceback-printing)
- -l: show local variables in tracebacks
- -s: disable stdout capturing, [docs link](https://docs.pytest.org/en/8.3.x/how-to/output.html#modifying-python-traceback-printing)


## Pytest pytest.ini file settings:
### addopts: (stands for add options)
[docs link](https://docs.pytest.org/en/stable/reference/reference.html#confval-addopts)
This settings can hold any number of the previous flags, and it will apply it automatically when testing.

#### example:
in you pytest.ini file if addopts like this:</br>
addopts = -v</br>
this means when you are running: pytest path/to/test/unit</br>
you are doing this: pytest path/to/test/unit -v

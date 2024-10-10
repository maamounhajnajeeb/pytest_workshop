# hooks/reporting/conftest.py

def pytest_report_header():
    return ["extrainfo: line 1"]

def pytest_terminal_summary(terminalreporter):
    if terminalreporter.verbosity >= 1:
        terminalreporter.section("my special section")
        terminalreporter.line("report something here")

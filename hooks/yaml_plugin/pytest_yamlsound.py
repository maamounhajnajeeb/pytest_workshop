import yaml, pytest


def pytest_collect_file(parent, path):
    if path.ext == ".yml" and path.basename.startswith("test"):
        return YamlFile.from_parent(parent, fspath=path)


class YamlException(Exception):
    """Custom exception for error reporting."""


class YamlFile(pytest.File):
    def collect(self):
        raw = yaml.safe_load(self.fspath.open())
        for spec in raw:
            name = spec["name"]
            yield YamlItem.from_parent(self, name=name, spec=spec)


class YamlItem(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec

    def runtest(self):
        test_type = self.spec.get("type")
        if test_type != "check-compression":
            raise YamlException(f"unknown test type: {test_type}")
        codec = self.spec.get("codec")
        if codec != "mp3":
            raise YamlException(f"unknown codec: {codec}")
        # pseudo check
        inputfile = self.spec.get("inputfile")
        compression = self.spec.get("compression")
        real_comp = "15%"
        if compression != real_comp:
            raise YamlException(
                f"compression of {inputfile} was {real_comp}, "
                f"expected {compression}")

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            return f"spec failed: {excinfo.value}"
        return super().repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, 0, f"usecase: {self.name}"

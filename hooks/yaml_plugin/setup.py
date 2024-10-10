# hooks/yaml_plugin/setup.py
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='pytest-yamlsound', version='0.1',
        description='yaml-based soundcheck',
        author='yourname',
        author_email='you@example.com',
        url='http://www.example.com/url/',
        py_modules=['pytest_yamlsound'],
        license="MIT",
        entry_points={'pytest11': ['yamlsound = pytest_yamlsound']},
        install_requires=['pytest>=5.4.0', 'PyYAML'],
    )

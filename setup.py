"""Setup for rdflib-pyld-compat."""
from setuptools import setup, Command
import os

# Extract version number
import re
VERSIONFILE = "rdflib_pyld_compat/__init__.py"
verfilestr = open(VERSIONFILE, "rt").read()
match = re.search(
    r"^__version__ = '(\d\.\d.\d+(\.\d+)?)'",
    verfilestr,
    re.MULTILINE)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))


class Coverage(Command):
    """Class to allow coverage run from setup."""

    description = "run coverage"
    user_options = []

    def initialize_options(self):
        """Empty initialize_options."""
        pass

    def finalize_options(self):
        """Empty finalize_options."""
        pass

    def run(self):
        """Run coverage program."""
        os.system("coverage run --source=rdflib_pyld_compat setup.py test")
        os.system("coverage report")
        os.system("coverage html")
        print("See htmlcov/index.html for details.")

setup(
    name='rdflib-pyld-compat',
    version=version,
    packages=['rdflib_pyld_compat'],
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: Apache Software License",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    author='Simeon Warner',
    author_email='simeon.warner@cornell.edu',
    description='Conversion between rdflib and PyLD data formats for compatibility',
    long_description=open('README').read(),
    url='http://github.com/zimeon/rdflib-pyld-compat',
    install_requires=[
        "rdflib>=4.2.0",
        "pyld",
        "testfixtures"
    ],
    test_suite="tests",
    cmdclass={
        'coverage': Coverage,
    },
)

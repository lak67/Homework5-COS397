# DevOps Exercise

This project is Shell Software's implementation of a Python package for sorting integer 
lists using the DevOps software development approach.
[![Sort Lib](https://github.com/lak67/Homework5-COS397/actions/workflows/main.yml/badge.svg)](https://github.com/lak67/Homework5-COS397/actions/workflows/main.yml)
> **Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

## pre-commit-config.yaml: Linting with Black and Flake8
The .pre-commit-config.yaml file limits the maxima file size to 200kb. It detects AWS credentials, but allows there to be missing credentials using an argument. Black uses version 22.8.0 and uses the --diff arg to show what is changed in a file. The pyproject.toml file specifies more settings for the black tool including: line-length and includes different python versions. Flake8 uses version 5.0.4 and has a maximum line length of 120 and excludes the files under .git, __pycache__ files, and build files. 
To run the linting locally first install all dependencies, then run the pre-commit command.
> python3 -m pip install -r requirements-dev.txt
> pre-commit run --all-files

## Implementation of Sorting Algorithms


## Implementation of Testing (Using PyTests)

## Implementation of Linting

Linting is implemented in the .pre-commit-config file to lint before commits, as well as in the .github/workflows/main.yml file (which lints, tests, and packages).

## Modification of the GitHub actions workflow so that it tests and builds the package for all three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10.

The Github actions workflow was edited by editing the main.yml file found under .github/workflows/. In this file for each job a matrix was specified with an OS argument and python-version argument. The OS argument specifies all three operating systems [ubuntu-latest, windows-latest, macos-latest] and python versions [3.9.0, 3.10.0]. 

## Badges added to this README.md File

1. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
    >**Warning**: Do not upload to the authoritative Python Package Index (PyPI).  

After the build in the packaging job of the github actions workflow, the distribution files created are uploaded to PyPI.

Possible work division, three sub-teams:
1. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
1. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
1. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).


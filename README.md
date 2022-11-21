# DevOps Exercise

This project is Shell Software's implementation of a Python package for sorting integer 
lists using the DevOps software development approach.

> **Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

You will need to:
1. Add .pre-commit-config.yml which:  
    1. Limits maxima file size.
    1. Runs the bllack and flake8 linters.
    1. Detect presence of aws credentials private keys. 
The .pre-commit-config.yaml file limits the maxima file size to 200kb. It detects AWS credentials, but allows there to be missing credentials using an argument. Black uses version 22.8.0 and uses the --diff arg to show what is changed in a file. The pyproject.toml file specifies more settings for the black tool including: line-length and includes different python versions. Flake8 uses version 5.0.4 and has a maximum line length of 120 and excludes the files under .git, __pycache__ files, and build files. 
    To run the linting locally first install all dependencies, then run the pre-commit command.
    python3 -m pip install -r requirements-dev.txt
    pre-commit run --all-files
1. Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory,
code should be documented using standard Python practices (there are several [docstring 
styles](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
select one and be consistent).


1. Implement testing using the [pytest](https://docs.pytest.org/en/6.2.x/) framework, see test directory.
1. Implement linting, style checking using both [flake8](https://flake8.pycqa.org/en/latest/) and 
[black](https://black.readthedocs.io/en/stable/). 
1. Modify the GitHub actions workflow so that it tests and builds the package for all 
three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about [Distributing Python packages](https://docs.python.org/3/distributing/index.html).
1. Modify this file to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
1. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
    >**Warning**: Do not upload to the authoritative Python Package Index (PyPI).  


Possible work division, three sub-teams:
1. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
1. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
1. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).


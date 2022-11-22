# DevOps Exercise

This project is Shell Software's implementation of a Python package for sorting integer 
lists using the DevOps software development approach.
[![Sort Lib](https://github.com/lak67/Homework5-COS397/actions/workflows/main.yml/badge.svg)](https://github.com/lak67/Homework5-COS397/actions/workflows/main.yml)
> **Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

## pre-commit-config.yaml: Linting with Black and Flake8
The .pre-commit-config.yaml file limits the maxima file size to 200kb. It detects AWS credentials, but allows there to be missing credentials using an argument. Black uses version 22.8.0 and uses the --diff arg to show what is changed in a file. The pyproject.toml file specifies more settings for the black tool including: line-length and includes different python versions. Flake8 uses version 5.0.4 and has a maximum line length of 120 and excludes the files under .git, __pycache__ files, and build files. 
To run the linting locally first install all dependencies.
> python3 -m pip install -r requirements-dev.txt

> pre-commit install 

Once the dependencies are installed, pre-commit can be run. 
> pre-commit run --all-files

## Implementation of Sorting Algorithms
Standard Python implementations of bubble sort, quicksort, and insertion sort have been defined in `/basic_sort_shell_software/int_sort.py`. The implementations for the sorting algorithms have been replicated from the following sources:

Bubble sort, by 9 contributors on [GeeksforGeeks](https://www.geeksforgeeks.org/python-program-for-bubble-sort/)

Quicksort, by 8 contributors on [GeeksforGeeks](https://www.geeksforgeeks.org/python-program-for-quicksort/)

Insertion sort, by 5 contributors on [GeeksforGeeks](https://www.geeksforgeeks.org/python-program-for-insertion-sort/)

## Implementation of Testing (Using PyTests)

## Implementation of Linting

Linting is implemented in the .pre-commit-config file to lint before commits, as well as in the .github/workflows/main.yml file (which lints, tests, and packages).

## Modification of the GitHub actions workflow so that it tests and builds the package for all three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10.

The Github actions workflow was edited by editing the main.yml file found under .github/workflows/. In this file for each job a matrix was specified with an OS argument and python-version argument. The OS argument specifies all three operating systems [ubuntu-20.04, windows-latest, macos-latest] and python versions [3.9.0, 3.10.0].

Due to issue [#401](https://github.com/actions/setup-python/issues/401) in actions/setup-python, Ubuntu has issues setting up with python version 3.10.0. To fix this, ubuntu-20.04 is used rather than ubuntu-latest. 

![Successful Workflow](https://mcusercontent.com/6310a52cdfd4835b6f5b53169/images/a038ffe4-7c12-10b3-5a6f-edb7adaa72dd.png)
## Badges added to this README.md File
The badges added to this workflow states if the workflow passes. 



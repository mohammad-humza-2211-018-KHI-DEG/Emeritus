# Xloop-Emeritus Data Engineering Bootcamp
This is a repository of **Xloop-Emeritus Data Engineering Bootcamp** also known as **2211-deg** or **DEG**. One can find resources for **daily activities** for the hands-on self-study session (after lunch/prayer).


**The daily activities allow you to train skills that will be crucial to perform well in a capstone project**.
## Contents of a repository
- `tasks` - a folder with the resources for daily activities
- `.gitignore` - a file specyfying what files to avoid in `git` vesion control
- `requirements.txt`- a file with list of Python modules and their versions to be installed to use the 
root of the repository.
- `README.md` - this very file
- `setup.py` - the file used for settuping Python projects

## Working on daily activities and solution development
The student is encouraged to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) this repository and keep the solutions in **private** fork of this repository.

## Formatting code
In order to install the autoformatting pipeline, use:

`pre-commit install`

All updated files will be reformatted and linted before the commit.

To reformat and lint all files in the project, use:

`pre-commit run --all-files`

The used linters are configured in `.pre-commit-config.yaml`.

# Python Examples

This repo is to share examples of git workflow, easy Python set-up, test-driven development, 
and general programming ideas.

### Installation

#### Getting the code

1. Hit the green "Code" button on this repo.
1. Choose your preferred option to download the code - Github Desktop would be the easiest
and best since it can update over time, but a zip file also works.

#### Installing an editor

Many editors to choose from but these are popular and work on Windows:
1. [Visual Studio](https://visualstudio.microsoft.com/)
1. [Atom](https://atom.io/)

#### Installing Python

1. Starting from this project folder
1. Install Python from the [Downloads](https://www.python.org/downloads/) page
1. This should also install [pip](https://pip.pypa.io/en/stable/getting-started/) - test with command `pip` 
1. (OPTIONAL) Install [venv](https://docs.python.org/3/library/venv.html). Initialize virtual environment folder - `python -m venv .venv`. 
Start venv with `./.venv/Scripts/activate.bat`. This tool is useful to isolate your project dependencies, but not strictly necessary.
1. Install the project dependencies with `pip install -r requirements.txt`

#### Tests

Run `pytest` - this will be installed as part of the project dependencies.

The tests can be used to run assertions on any code you've written. 

Note that the test files must be named `{module}_test.py` and the test functions 
must be called `test_{name_of_test}` - otherwise `pytest` can't locate them


### Development

New files and tests can be made in the same pattern as the existing ones. 

You can also run python files as executables to run the code without a test like so:

`python {file_name}.py`


Disclaimer - not a Python expert :)

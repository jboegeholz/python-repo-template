# python-repo-template
A Blueprint for a python project

## Motivation
Making setting up a Python project structure / repository easier
According to
https://creatronix.de/how-to-structure-your-python-project/

## Usage
1. Use this repository via use as template
2. Give your project a name
3. Clone your project from your IDE oder via git CLI
4. Delete unnecessary files (e.g. setup.py, pyproject.toml, .travis.yml, Jenkinsfile)
4. Create a virtual environment
5. Install dependencies
6. Run tests
7. Start coding



## Dependencies
### Installing 
    pip install -r requirements.txt

### Adding Dependencies
    pip install <dependency-name>

### Updating
    pip install -r requirements_to_freeze.txt --upgrade
    pip freeze > requirements.txt 

## Running Tests
1. Open a terminal
2. pytest

## Packaging
1. Open a terminal
2. python setup.py sdist bdist_wheel
3. twine upload dist/*

## TODOS
Add a .github/workflows/template-cleanup.yml


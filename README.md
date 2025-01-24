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
4. Delete unnecessary files 
   1. e.g. setup.py, pyproject.toml, setup.cfg when not building a package
   2. .travis.yml, Jenkinsfile when not using CI / CD
5. Create a virtual environment
6. Install dependencies
7. Run tests
8. Start coding


## Dependencies
### Installing 

```bash
    pip install -r requirements.txt
```

### Adding Dependencies
    pip install <dependency-name>

### Updating
    pip install -r requirements_to_freeze.txt --upgrade
    pip freeze > requirements.txt 

## Running Tests

```bash
    pytest --cov=python_repo_template/ tests/
```

## Packaging
1. Open a terminal
2. git tag -am "Version 0.1" 0.1 
3. python setup.py sdist bdist_wheel
4. twine upload dist/*

## TODOS
Add a .github/workflows/template-cleanup.yml
Migrate to Circle CI https://circleci.com/docs/migrating-from-travis/


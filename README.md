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
4. Create a virtual environment
5. Delete unnecessary files e.g. travis.yml, Jenkinsfile when not using CI / CD
6. Install dependencies
7. Run tests
8. Start coding


## Dependencies
### Installing 

```bash
    pip install poetry
```
### Poetry + PyCharm venv

```bash
    poetry env use ./venv/bin/python3
```

### Adding Dependencies

    poetry add <package-name>

### Updating

```bash
  poetry update
```
## Running Tests

```bash
    pytest --cov=python_repo_template/ tests/
```

## Packaging
If you want to publish your Package on pypi.org  you need to aadd your Access Token to the Poetry config first:
```bash
poetry config pypi-token.pypi <dein-token>
```
then you can build your package:
```bash
  poetry build
```
and publish it
```bash
poetry publish --build
```


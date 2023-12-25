import subprocess
from python_repo_template.__main__ import main


def test_python_repo_template_main():
    assert main() == 0


def test_python_repo_template_integration():
    assert subprocess.run(['./python_repo_template/__main__.py']).returncode == 0
import subprocess
import sys

from python_repo_template.__main__ import main


def test_python_repo_template_main():
    assert main() == 0


def test_python_repo_template_integration():
    spr = subprocess.run([sys.executable, "-m", 'python_repo_template.__main__'])
    assert spr.returncode == 0
#!/usr/bin/env python

import sys

from python_repo_template import get_hello_from_submodule


def main():
    print(get_hello_from_submodule())
    return 0


if __name__ == '__main__':
    sys.exit(main())
#!/usr/bin/env python

import sys

from python_repo_template import get_hello_from_submodule, do_some_logging
from python_repo_template import MyClass
import logging

logger = logging.getLogger("my_application") # don't use __name__ here!


def setup_logging():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # stream handler
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)

    # file handler
    fh = logging.FileHandler('my_application.log', encoding="UTF-8")
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.setLevel(logging.INFO)

def main():
    setup_logging()
    logger.info("hello from main")
    do_some_logging()
    my_class = MyClass()
    my_class.do_some_logging()
    print(get_hello_from_submodule())
    return 0


if __name__ == '__main__':
    sys.exit(main())
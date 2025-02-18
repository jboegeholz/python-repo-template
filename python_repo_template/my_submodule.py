import logging

logger = logging.getLogger("my_application.my_module")


def do_some_logging():
    logger.info("Hello from mymodule")

def get_hello_from_submodule() -> str:
    return "Hello from sub-module"

def add_two_ints(a:int, b:int) -> int:
    return a + b
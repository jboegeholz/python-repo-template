import logging

logger = logging.getLogger("my_application.MyClass")


class MyClass:
    def do_some_logging(self):
        logger.error("do_some_logging: right here - right now")
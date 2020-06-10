from .logger import Logger
from sys import stdout, stderr

import traceback


class PrintLogger(Logger):
    def error(self, ex):
        message = ''.join(
            traceback.format_exception(
                etype=type(ex),
                value=ex,
                tb=ex.__traceback__
            )
        )
        print(message, file=stderr)

    def info(self, message):
        print(message, file=stdout)

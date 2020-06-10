from .logger import Logger
from siblings.environment import configuration as c

import requests
import traceback


class HttpLogger(Logger):
    def __init__(self):
        configuration = c.Configuration()
        self._url = configuration.http_logging_url

    def error(self, ex):
        message = ''.join(
            traceback.format_exception(
                etype=type(ex),
                value=ex,
                tb=ex.__traceback__
            )
        )
        requests.post(self._url, data=message)

    def info(self, message):
        requests.post(self._url, data=message)

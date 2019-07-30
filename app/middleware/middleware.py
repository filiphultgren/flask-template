from flask import Flask, request
import logging


class Middleware:
    def __init__(self, app: Flask):
        self.app = app
        self.logger = logging.getLogger(__name__)

    def setup(self):
        app = self.app
        logger = self.logger

        @app.before_request
        def do_something_before_a_request():
            auth = request.headers.get('Authorization')

            logger.info(f'Got auth {auth}')

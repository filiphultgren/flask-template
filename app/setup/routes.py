from flask import Flask
import handlers.test


class RoutesStartup:
    def __init__(self, app: Flask):
        self.app = app

    def setup(self):
        self.app.register_blueprint(handlers.test.blueprint)

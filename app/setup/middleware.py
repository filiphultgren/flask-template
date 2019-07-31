from flask import Flask
import middleware.middleware


# Here we just add the blueprints to the existing Flask app.
class MiddlewareStartup:
    def __init__(self, app: Flask):
        self.app = app

    def setup(self):
        # We only need to register this once and then everything is ready to go
        self.app.register_blueprint(middleware.middleware.blueprint)

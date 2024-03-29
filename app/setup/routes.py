from flask import Flask
import handlers.test


# Here we just add the blueprints to the existing Flask app.
class RoutesStartup:
    def __init__(self, app: Flask):
        self.app = app

    def setup(self):
        # We only need to register this once and then everything is ready to go
        self.app.register_blueprint(handlers.test.blueprint)
        # If you want to add a new handler file, remember to add the new blueprint from that file

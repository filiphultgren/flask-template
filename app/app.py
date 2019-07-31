from flask import Flask
from setup.routes import RoutesStartup
from setup.middleware import MiddlewareStartup
import logging
import sys


if __name__ == '__main__':
    app = Flask(__name__)

    # Setup
    # The logger needs to be initialized
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # The middleware is being initialized
    MiddlewareStartup(app).setup()

    # The routes are added
    RoutesStartup(app).setup()

    app.run(host='0.0.0.0', debug=True)

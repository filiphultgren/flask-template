from flask import Flask
from setup.routes import RoutesStartup
from middleware.middleware import Middleware
import logging
import sys


if __name__ == '__main__':
    app = Flask(__name__)

    # Setup
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    Middleware(app).setup()

    RoutesStartup(app).setup()

    app.run(host='0.0.0.0', debug=True)

from flask import request, Blueprint, Response
import json
import logging

blueprint = Blueprint('middleware', __name__)


# So here we can do something before every request or after. Depending on our needs.
# E.g. we can authenticate every request here.
class Middleware:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    @blueprint.before_app_request
    def do_something_before_a_request():
        logger = logging.getLogger(__name__)
        auth = request.headers.get('Authorization')

        if auth == 'no_valid_user':
            logger.info('User not authorized')
            return Response(json.dumps({'message': 'Unauthorized'}), status=401, mimetype='application/json')

    def do_something_else_before_a_request(self):
        auth = request.headers.get('Authorization')

        self.logger.info(f'Got auth {auth}')


# Almost the same here as in the handlers.
middleware = Middleware()
blueprint.before_app_request(middleware.do_something_else_before_a_request)

from flask import Blueprint, request, Response
import json
from services.test import TestService
from services.another import AnotherService
import logging

# A Blueprint can be seen as a "copy" of a Flask app. We use it here so we don't need to import the initiated instance
# of the Flask app
blueprint = Blueprint('catches', __name__)


# A handler is where the endpoints lives. A handler then call the necessary services in order to complete the request
# and send back a response. This is just for separation of concern. So we can re-use the services in other
# endpoints/handlers.
class TestHandler:

    def __init__(self):
        self.test_service = TestService()
        self.another_service = AnotherService()
        self.logger = logging.getLogger(__name__)

    def post(self):
        try:
            if request.json:
                some_parameter = request.json.get('some_parameter') or ''
            else:
                some_parameter = 'No body provided.'
            resp = self.test_service.test(some_parameter)
        except Exception as e:
            return Response(json.dumps({'message': '{}'.format(e)}), status=500, mimetype='application/json')

        return resp

    def get_something(self):
        try:
            resp = self.another_service.another()
        except Exception as e:
            return Response(json.dumps({'message': '{}'.format(e)}), status=500, mimetype='application/json')

        return resp

    # But if you want to you use the cool function decorator app.route we need to make the class method to a static
    # method. So in this case we don't have access to self.
    @staticmethod
    @blueprint.route('/test2', methods=['POST', 'GET'])
    def another_endpoint():
        try:
            if request.method == 'GET':
                return Response(json.dumps({'message': 'You used method GET'}), status=200, mimetype='application/json')
            else:
                return Response(json.dumps({'message': 'You used method POST'}), status=200, mimetype='application/json')
        except Exception as e:
            return Response(json.dumps({'message': '{}'.format(e)}), status=200, mimetype='application/json')


# In order to add methods in a class that has access to self, we need to first initiate the class as below
test_handler = TestHandler()
# Then we can manually add it to the blueprint
blueprint.add_url_rule('/test',  # This is the endpoint's name
                       view_func=test_handler.post,  # This is the function that will be called when a request is
                                                     # sent to this endpoint.
                       methods=['POST', 'DELETE']  # This is where you specify which methods are allowed to be used
                                                   # for this endpoint
                       )
blueprint.add_url_rule('/another', view_func=test_handler.get_something, methods=['GET'])
# I suggest that this way of adding endpoints is used, so class instances can be utilized.

from flask import Response
import json
import logging


# This is a service. A service is something that contains functionality and can be used by whatever endpoint/handler.
# Here we can add/subtract/manipulate data. Do some request to other micro services and so on. Then when everything is
# complete we can return a response.
class TestService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def test(self, some_parameter):

        # Do stuff here

        return Response(json.dumps({'some_parameter': some_parameter}), status=200, mimetype='application/json')

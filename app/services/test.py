from flask import Response
import json
import logging


class TestService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def test(self, some_parameter):

        # Do stuff here

        return Response(json.dumps({'some_parameter': some_parameter}), status=200, mimetype='application/json')

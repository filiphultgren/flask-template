from flask import Blueprint, request, abort, Response
import json
from services.test import TestService
import logging

blueprint = Blueprint('catches', __name__)


class TestHandler:

    def __init__(self):
        self.test_service = TestService()
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


test_handler = TestHandler()
blueprint.add_url_rule('/test', view_func=test_handler.post, methods=['POST'])

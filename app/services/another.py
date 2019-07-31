from flask import Response
import json
import logging


class AnotherService:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def another(self):

        # Do stuff here

        return Response(json.dumps({'another_thingy': 'result'}), status=200, mimetype='application/json')

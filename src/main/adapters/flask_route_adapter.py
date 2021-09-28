import asyncio
import json
from types import SimpleNamespace
from flask import jsonify, request
from src.application.protocols.controller import Controller


def adaptRoute(controller: Controller):
    def execute():
        parameters = dict()
        parameters.update(request.json)
        data = json.loads(json.dumps(parameters),
                          object_hook=lambda d: SimpleNamespace(**d))
        http_response = asyncio.run(controller.handle(data))
        return jsonify(http_response)

    return execute

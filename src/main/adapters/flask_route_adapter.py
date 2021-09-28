import asyncio
import json
from types import SimpleNamespace
from flask import jsonify, request
from src.application.protocols.controller import Controller


def adaptRoute(controller: Controller):
    def get_params() -> SimpleNamespace:
        parameters = dict()
        parameters.update(request.json)
        parameters.update(request.args.to_dict())
        data = json.loads(json.dumps(parameters),
                          object_hook=lambda d: SimpleNamespace(**d))
        return data

    def execute():
        http = asyncio.run(controller.handle(get_params()))
        return jsonify(http.body), http.status

    return execute

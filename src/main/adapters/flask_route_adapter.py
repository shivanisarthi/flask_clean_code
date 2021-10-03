import asyncio
from collections import namedtuple
from flask import jsonify, request
from src.application.controllers import Controller


def adaptRoute(controller: Controller):
    def tranform(current_dict):
        return namedtuple('Obj', current_dict.keys())(*current_dict.values())

    def get_params():
        parameters = dict()
        parameters.update(request.json)
        parameters.update(request.args.to_dict())
        data = tranform(parameters)
        return data

    def execute():
        http = asyncio.run(controller.handle(get_params()))
        if http.status >= 200 and http.status <= 299:
            return jsonify(http.body), http.status
        else:
            return dict(message=http.body.args[0]), http.status

    return execute

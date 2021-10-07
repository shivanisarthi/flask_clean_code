import asyncio
from collections import namedtuple
from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import View
from src.application.controllers import Controller


class AdaptController(View):
    def __init__(self, controller: Controller) -> None:
        super().__init__()
        self.controller = controller

    def __to_namedtuple(self, current_dict):
        return namedtuple("request", current_dict.keys())(*current_dict.values())

    def __adapt_args(self, args_params):
        args_dict = dict()
        if request.json:
            args_dict.update(request.json)
        args_dict.update(request.args.to_dict())
        args_dict.update(args_params)
        transform = self.__to_namedtuple(args_dict)
        return transform

    def dispatch_request(self, *args, **kwargs) -> ResponseReturnValue:
        transform_args = self.__adapt_args(kwargs)
        http = asyncio.run(self.controller.handle(transform_args))
        if http.status >= 200 and http.status <= 299:
            return jsonify(http.body), http.status
        return dict(message=http.body.args[0]), http.status


def make_adapter():
    return AdaptController

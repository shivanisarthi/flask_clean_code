from abc import ABCMeta, abstractmethod
from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True)
class HttpResponse:
    body: Any
    status: int


class Controller():

    async def perform(self, request: Any) -> HttpResponse:
        raise NotImplementedError

    async def handle(self, request: Any) -> HttpResponse:
        errors = self.validation(request)
        if (errors):
            return self.bad_request(errors)
        try:
            return await self.perform(request)
        except Exception as e:
            return self.server_error(e)

    def validation(self, request: Any) -> Any:
        return None

    def ok(self, data) -> HttpResponse:
        return HttpResponse(data, status=200)

    def no_content(self) -> HttpResponse:
        return HttpResponse('', 204)

    def server_error(self, err: Exception) -> HttpResponse:
        return HttpResponse(err, status=500)

    def bad_request(self, err: Exception) -> HttpResponse:
        return HttpResponse(err, status=400)

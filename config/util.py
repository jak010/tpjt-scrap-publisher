from __future__ import annotations
from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponse
import json

from typing import Tuple, List, Type
from functools import wraps

from apps.layer.exceptions import MemberAPIException, BaseAPIException

api_exception_types = Type[BaseAPIException]


class UnAuthorizedResponse(HttpResponse):
    status_code = 401

    def __init__(self):
        super().__init__(content_type="application/json")
        self.content = json.dumps({
            "desg": "UnAuthorized User"
        })


def login_required(view):
    def view_func(*args, **kwargs):
        view_object, wsgi_request = args
        if isinstance(view_object.request.user, AnonymousUser):
            return UnAuthorizedResponse()

        return view(*args, **kwargs)

    return view_func


class Exceptable:
    """ View에서 Exception 명시하기 """

    def __init__(self, expects: List[api_exception_types]):
        self.exec = expects

    def __call__(self, view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):

            if self.exec:
                for exe in self.exec:
                    if isinstance(exe, MemberAPIException):
                        raise self.exec

            view = view_func(*args, **kwargs)
            return view

        return wrapper

    def notify(self):
        raise NotImplementedError

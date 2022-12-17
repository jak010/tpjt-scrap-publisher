from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponse
import json


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

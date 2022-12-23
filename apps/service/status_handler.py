from __future__ import annotations

from typing import TypedDict, Callable, Tuple, Dict
from django.views import View
from ..exceptions import member_exceptions

from django.http import JsonResponse, HttpResponse
from django.core.handlers.exception import response_for_exception, get_exception_response
from django.urls import get_resolver, get_urlconf

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect


class BackoffTypeDict(TypedDict):
    target: Callable
    args: Tuple
    kwargs: dict
    elapsed: float
    exception: Exception


class MemberServiceHttpExceptor:

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        # backoff_wrapper: BackoffTypeDict = args[0]

        # raise backoff_wrapper['exception']
        try:
            raise args[0]
        except member_exceptions.MemberLoginFailError as e:
            print("?")
            return JsonResponse(
                status=400,
                data={
                    "error": "MEMBER LOGIN FAIL",
                    "message": "CHECK ON LOGIN_ID or LOGIN_FAIL"
                }
            )

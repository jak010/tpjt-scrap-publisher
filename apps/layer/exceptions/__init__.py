from django.http import JsonResponse
from django.core.exceptions import BadRequest
from http import HTTPStatus


class BaseAPIException(Exception):
    """ BUSINESS EXCEPTION"""
    status_code = None
    error = None
    debug = None

    def __call__(self, *args, **kwargs):
        return self._exception_response()

    def _exception_response(self):
        return JsonResponse(
            status=self.status_code,
            data={
                'error': self.error,
                'debug': self.debug
            }
        )


class MemberAPIException(BaseAPIException):
    """ MEMBER API EXCEPTION """


class CommonException(Exception):
    """ COMMON EXCEPTION"""
    status_code = None
    error = None
    message = None

    def __init__(self, message=None):
        self.message = message

    def error_response(self):
        return JsonResponse(
            status=self.status_code,
            data={
                'error': self.error,
                'message': self.message
            }
        )


class BadRequestError(CommonException):
    status_code = HTTPStatus.BAD_REQUEST
    error = "BAD REQUEST"

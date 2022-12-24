from django.http import JsonResponse


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
    """ MEMBER API EXCEPTIOn """

# from apps.member.exceptions import BaseAPIException, BadRequestError
#
#
# class APIExceptionMiddleWare:
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#
#     def process_exception(self, request, exception):
#         """ Exception Handler """
#         if isinstance(exception, BaseAPIException):
#             return exception()
#         if isinstance(exception, BadRequestError):
#             return BadRequestError(exception.message) \
#                 .error_response()

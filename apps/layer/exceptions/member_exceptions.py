from http import HTTPStatus

from . import MemberAPIException


class MemberAuthenticateFailError(MemberAPIException):
    """ 인증에 실패함 """
    status_code = HTTPStatus.UNAUTHORIZED
    error = "MEMBER AUTHENTICATE FAIL"
    debug = "CHECK ON LOGIN_ID or LOGIN_PASSWORD"


class MemberLoginFailError(MemberAPIException):
    """ 로그인에 실패함 """
    status_code = HTTPStatus.FORBIDDEN
    error = "MEMBER LOGIN FAIL"
    debug = "PLEASE CHECK IF YOU ARE LOGGED IN"

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


class MemberDuplicateError(MemberAPIException):
    """ 멤버 생성에 실패함 """
    status_code = HTTPStatus.NOT_ACCEPTABLE
    error = "ALREADY EXIST MEMBER"
    debug = "PLEASE OTHER CREDENTIAL INPUT"

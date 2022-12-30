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


class MemberCreateFailError(MemberAPIException):
    """ 멤버 생성에 실패함 """
    status_code = HTTPStatus.NOT_ACCEPTABLE
    error = "MEMBER CREATE FAIL"
    debug = "PLEASE OTHER CREDENTIAL INPUT"


class MemberDoesNotExit(MemberAPIException):
    """ 존재하지 않는 사용자 """
    status_code = HTTPStatus.NOT_ACCEPTABLE
    error = "Member Does Not Exist"
    debug = "PLEASE OTHER EMAIL"


class MemberPasswordNotMatched(MemberAPIException):
    """ 패스워드가 일치하지 않음
      Eg. Password 제한에 사용하기
    """
    status_code = HTTPStatus.NOT_ACCEPTABLE
    error = "Member Password Does Not Matched"
    debug = "PLEASE OTHER PASSWORD"


class MemberDeActivateLogin(MemberAPIException):
    """ 사용가의 로그인이 허용되지 않음"""
    status_code = HTTPStatus.NOT_ACCEPTABLE
    error = "DeActivate Member LOGIN"
    debug = "BLOCK MEMBER"

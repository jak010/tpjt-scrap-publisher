from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore

from ..exceptions.member_exceptions import MemberAuthenticateFailError


def member_authenticate(request, login_email: str, login_password: str):
    """ 사용자 인증하기 """
    auth = authenticate(
        username=login_email,
        password=login_password
    )

    print(auth)
    if auth is None: raise MemberAuthenticateFailError()

    login(request, auth)

    return auth


def member_session(request, auth) -> SessionStore:
    """ 사용자 session 찾기 """
    return SessionStore(session_key=request.session.session_key)

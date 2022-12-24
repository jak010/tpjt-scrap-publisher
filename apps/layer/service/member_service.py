from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore

from ..exceptions.member_exceptions import MemberAuthenticateFailError


class MemberAuthenticateService:

    def __init__(self, login_email: str, login_password: str):
        self._login_email = login_email
        self._login_password = login_password

    def check_authenticate(self):
        auth = authenticate(
            username=self._login_email,
            password=self._login_password
        )

        if auth is None: raise MemberAuthenticateFailError

        return auth


class MemberLoginService:

    @classmethod
    def login(cls, request, auth):
        login(request, auth)
        return cls(request, auth)

    def __init__(self, request, auth):
        self._request = request
        self.auth = auth

    @property
    def session(self) -> SessionStore:
        return SessionStore(session_key=self._request.session.session_key)

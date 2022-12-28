from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.db import transaction, IntegrityError

from apps.layer.exceptions.member_exceptions import MemberAuthenticateFailError
from apps.layer.exceptions.member_exceptions import MemberDuplicateError
from apps.orm import Member


def member_authenticate(request, login_email: str, login_password: str):
    """ 사용자 인증하기 """
    auth = authenticate(
        username=login_email,
        password=login_password
    )

    if auth is None: raise MemberAuthenticateFailError()

    login(request, auth)

    return auth


def get_session(request, auth) -> SessionStore:
    """ 사용자 session 찾기 """
    return SessionStore(session_key=request.session.session_key)


def create_member(member_create_form_dto) -> Member:
    """ 사용자 생성하기 """
    try:
        with transaction.atomic():
            new_member = Member(
                email=member_create_form_dto.get_email,
            )
            new_member.set_password(member_create_form_dto.get_password)
            new_member.save()

            return new_member
    except IntegrityError:
        raise MemberDuplicateError()

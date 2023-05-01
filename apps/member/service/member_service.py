from __future__ import annotations

from django.contrib.auth import authenticate, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from django.db import transaction, IntegrityError

Member = get_user_model()


class MemberDuplicateError(Exception):
    """ Member가 중복됨 """


class MemberEmailAlreadyExistError(Exception):
    """ Email이 존재함 """


def get_session(request) -> SessionStore:
    """ 사용자 session 찾기 """
    return SessionStore(session_key=request.session.session_key)


def login(request, email: str, password: str) -> Member:
    """ 사용자 인증하기 """
    return authenticate(request=request, username=email, password=password)


def create_member(email: str, password: str):
    """ 사용자 생성하기 """
    member = Member.objects.filter(email=email).first()
    if member:
        raise MemberEmailAlreadyExistError()

    with transaction.atomic():
        new_member = Member(email=email)
        new_member.set_password(password)
        new_member.save()


def get_members():
    """ 모든 사용자 정보 가져오기 """
    return [{
        'member_id': member.id,
        'email': member.email,
        'last_login': member.last_login,
        'date_of_join': member.date_of_join,
        'is_active': member.is_active,
        'groups': [{
            'group_id': group.id,
            'name': group.name
        } for group in member.groups.all()]
    } for member in Member.objects.all() \
        .prefetch_related('groups')]

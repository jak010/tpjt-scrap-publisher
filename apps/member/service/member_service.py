from __future__ import annotations

from django.contrib.auth import authenticate, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from django.db import transaction, IntegrityError

Member = get_user_model()


def get_session(request) -> SessionStore:
    """ 사용자 session 찾기 """
    return SessionStore(session_key=request.session.session_key)


def member_authenticate(request, login_email: str, login_password: str) -> Member:
    """ 사용자 인증하기 """
    return authenticate(
        request=request,
        username=login_email,
        password=login_password
    )


def create_member(email: str, password: str) -> Member:
    """ 사용자 생성하기 """
    try:
        with transaction.atomic():
            new_member = Member(email=email)
            new_member.set_password(password)
            new_member.save()

            return new_member
    except IntegrityError:
        raise Exception("Member Create Fail")


# XXX: 더 고민해보자.
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

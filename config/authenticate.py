from __future__ import annotations

from django.contrib.auth import backends, get_user_model, hashers, login

Member = get_user_model()


class AuthenticateBackend(backends.BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs) -> Member:
        try:
            member = Member.objects.get(email=username)

            if not hashers.check_password(password, member.password):
                return None

            if member.is_active == 0:
                return None

        except Member.DoesNotExist as e:
            return None

        login(request, member)

        return member

    def get_user(self, user_id):
        """
          Notes: Custom Authenticate 에서 이 method를 오버라이딩 안해주면 request.user에서 접근이 불가능함
        """
        try:
            return Member.objects.get(id=user_id)  # <-- tried to get by email here
        except Member.DoesNotExist:
            return None

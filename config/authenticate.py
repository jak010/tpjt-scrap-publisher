from django.contrib.auth import backends, get_user_model, hashers, login

from apps.layer.exceptions import member_exceptions

Member = get_user_model()


class AuthenticateBackend(backends.BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            member = Member.objects.get(email=username)

            if not hashers.check_password(password, member.password):
                raise member_exceptions.MemberPasswordNotMatched()

            if member.is_active == 0:
                raise member_exceptions.MemberDeActivateLogin()

        except Member.DoesNotExist as e:
            raise member_exceptions.MemberDoesNotExit()

        login(request, member)

        return member

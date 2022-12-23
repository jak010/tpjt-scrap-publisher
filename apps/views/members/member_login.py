from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse, JsonResponse
from django.views import View

from .dto import MemberLoginFormDto


class MemberLoginView(View):

    def post(self, *args, **kwargs):
        """ Django Session 기반 유저 로그인 """

        member_login_form_dto = MemberLoginFormDto(self.request.POST)
        member_login_form_dto.is_valid()

        auth = authenticate(
            username=member_login_form_dto.get_email,
            password=member_login_form_dto.get_password
        )

        if auth is None:
            return HttpResponse(400)
        else:
            login(self.request, user=auth)

        session = SessionStore(
            session_key=self.request.session.session_key
        )

        return JsonResponse(status=200, data={
            'session_key': session.session_key,
            "expire_date": session.get_expiry_date()
        })

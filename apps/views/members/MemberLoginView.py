from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse, JsonResponse
from django.views import View


class MemberLoginView(View):

    def post(self, *args, **kwargs):
        """ Django Session 기반 유저 로그인 """
        email = self.request.POST.get("email", None)
        password = self.request.POST.get("password", None)

        auth = authenticate(
            username=email,
            password=password
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

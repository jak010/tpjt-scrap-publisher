from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse, JsonResponse
from django.views import View


class MemberLoginFormData(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    @property
    def get_email(self):
        return self.cleaned_data['email']

    @property
    def get_password(self):
        return self.cleaned_data['password']


class MemberLoginView(View):

    def post(self, *args, **kwargs):
        """ Django Session 기반 유저 로그인 """

        member_login_form_data = MemberLoginFormData(self.request.POST)
        member_login_form_data.is_valid()

        auth = authenticate(
            username=member_login_form_data.get_email,
            password=member_login_form_data.get_password
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

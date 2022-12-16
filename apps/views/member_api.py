from django.views.generic import View
from django.http import JsonResponse, HttpResponse

from django.db import IntegrityError

from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore

from ..orm import Member


class MemberListView(View):
    def get(self, *args, **kwargs):
        """ 사용자 목록조회하기 """
        members = Member.objects.all()

        items = [{
            'id': member.id,
            'email': member.email
        } for member in members]

        return JsonResponse(status=200, data={'items': items})


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


class MemberCreateView(View):

    def post(self, *args, **kwargs):
        """ 사용자 생성하기  """
        email = self.request.POST.get("email", None)
        password = self.request.POST.get('password', None)

        try:
            new_member = Member(
                email=email,
            )
            new_member.set_password(password)
            new_member.save()
        except IntegrityError:
            return JsonResponse(
                status=400,
                data={
                    "desg": "Already Exists Member"
                }
            )

        return JsonResponse(status=201, data={
            "member_id": new_member.id
        })

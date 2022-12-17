from django.db import IntegrityError
from django.http import JsonResponse
from django.views import View

from apps.orm import Member


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

from django.views.generic import View
from django.http import JsonResponse

from django.db import IntegrityError

from ..auth import Member


class MemberCreateView(View):

    def post(self, *args, **kwargs):
        email = self.request.POST.get("email", None)
        password = self.request.POST.get('password', None)

        try:
            new_member = Member(
                email=email,
                password=password  # TODO: passwod 저장할 떄 암호화 적용하기
            )
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

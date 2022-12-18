from django.db import IntegrityError
from django.http import JsonResponse
from django.views import View

from apps.orm import Member
from .dto.MemberCreateDto import MemberCreateFormDto


class MemberCreateView(View):

    def post(self, *args, **kwargs):
        """ 사용자 생성하기  """
        member_create_form_dto = MemberCreateFormDto(self.request.POST)
        member_create_form_dto.is_valid()

        try:
            new_member = Member(
                email=member_create_form_dto.get_email,
            )
            new_member.set_password(member_create_form_dto.get_password)
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

from django.http import JsonResponse
from django.views import View

from apps.layer.exceptions.member_exceptions import MemberDuplicateError
from apps.layer.service import member_service
from config.util import Exceptable
from .dto.MemberCreateDto import MemberCreateFormDto


class MemberCreateView(View):

    @Exceptable(expects=[
        MemberDuplicateError
    ])
    def post(self, *args, **kwargs):
        """ 사용자 생성하기  """
        member_create_form_dto = MemberCreateFormDto(self.request.POST)
        member_create_form_dto.is_valid()

        new_member = member_service.create_member(
            member_create_form_dto=member_create_form_dto
        )

        return JsonResponse(status=201, data={
            "member_id": new_member.id
        })

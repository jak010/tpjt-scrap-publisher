from __future__ import annotations

from typing import Union, Any

from django.http import JsonResponse
from django.views import View

from apps.layer.exceptions import member_exceptions
from apps.layer.service import member_service
from .dto.MemberCreateDto import MemberCreateFormDto

from http import HTTPStatus


class MemberCreateView(View):

    def post(self, *args, **kwargs) -> Union[
        JsonResponse,
        Any[
            member_exceptions.MemberCreateFailError
        ]
    ]:
        """ 사용자 생성하기  """
        member_create_form_dto = MemberCreateFormDto(self.request.POST)
        member_create_form_dto.is_valid()

        new_member = member_service.create_member(
            member_create_form_dto=member_create_form_dto
        )

        return JsonResponse(
            status=HTTPStatus.CREATED,
            data={
                "member_id": new_member.id
            })

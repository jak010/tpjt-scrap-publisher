from __future__ import annotations

from django.http.response import JsonResponse
from django.views import View

from apps.layer.exceptions import BadRequestError
from apps.layer.service.announce_service import AnnounceEmailService
from config.util import login_required
from .dto.email_publish_on_member_dto import EmailPublishOnMemberDto


class EmailPublishOnMemberView(View):

    @login_required
    def post(self, *args, **kwargs):
        """ 사용자에 이메일로 전송하기 """

        dto = EmailPublishOnMemberDto(self.request.POST)
        if not dto.is_valid():
            raise BadRequestError(dto.errors.get_json_data())

        announce_email_sevice = AnnounceEmailService(dto=dto)
        announce_email_sevice.publish(
            sender=self.request.user,
            with_schedule=True
        )

        return JsonResponse(status=201, data={
            "desg": "Success", 'data': dto.get_receiver
        })

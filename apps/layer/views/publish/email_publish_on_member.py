from __future__ import annotations

from django.http.response import JsonResponse
from django.views import View
from libs.announce.email.send_box import EmailSendBox

from apps.layer.exceptions import BadRequestError
from config.util import login_required
from libs.announce.email import (
    EmailMessage
)
from libs.rss.factory import rss_factory
from .dto.email_publish_on_member_dto import EmailPublishOnMemberDto


class EmailPublishOnMemberView(View):

    @login_required
    def post(self, *args, **kwargs):
        """ 사용자에 이메일로 전송하기 """

        dto = EmailPublishOnMemberDto(self.request.POST)
        if not dto.is_valid():
            raise BadRequestError(dto.errors.get_json_data())

        rss = rss_factory(domain=dto.get_domain, sub_domain=dto.get_sub_domain)

        email_send_box = EmailSendBox(
            sender=self.request.user,
            email_message=EmailMessage(
                email_subject=dto.get_subject,
                email_content_title=rss.get_entires_first.get_title,
                email_content_body=rss.get_entires_first.get_summary,
                receviers=dto.get_receiver
            )
        )
        result = email_send_box.publish()

        return JsonResponse(
            status=201,
            data={
                'message': result
            }
        )

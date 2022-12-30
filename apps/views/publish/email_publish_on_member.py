from __future__ import annotations

from django.http.response import JsonResponse, HttpResponse
from django.views import View

from apps.layer.exceptions import BadRequestError
from apps.models import PublishMemberHistory
from config.util import login_required
from libs.notify.email_sender import EmailSender
from libs.rss_requstor.utils import get_rss
from .dto.email_publish_on_member_dto import EmailPublishOnMemberDto


class EmailPublishOnMemberView(View):
    """ 사용자에 이메일로 전송하기 """

    @login_required
    def post(self, *args, **kwargs):

        email_publish_on_member_dto = EmailPublishOnMemberDto(self.request.POST)
        if not email_publish_on_member_dto.is_valid():
            raise BadRequestError(email_publish_on_member_dto.errors.get_json_data())  # XXX: 개선필요함

        rss = get_rss(email_publish_on_member_dto=email_publish_on_member_dto)

        try:
            # Email Publish
            email_sender = EmailSender(
                subject=rss.get_title,
                body=rss.get_summary,
                receviers=[email_publish_on_member_dto.get_receiver]
            )
            result = email_sender.publish()

            # Email Send History
            if result != 0:
                publish_history = PublishMemberHistory(
                    sender=self.request.user,
                    receiver=email_publish_on_member_dto.get_receiver,
                    title=rss.get_title,
                    content=rss.get_summary,
                    description=rss.get_summary_detail
                )
                publish_history.save()
        except ConnectionError:
            return HttpResponse(status=409)

        return JsonResponse(status=201, data={
            "desg": "Success"
        })

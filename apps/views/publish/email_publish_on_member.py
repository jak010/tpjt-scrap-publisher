from __future__ import annotations

from django.http.response import JsonResponse, HttpResponse
from django.views import View

from apps.layer.exceptions import BadRequestError
from config.util import login_required
from libs.announce.email_sender import EmailSender
from libs.rss_requstor.utils import rss_factory
from .dto.email_publish_on_member_dto import EmailPublishOnMemberDto

from django.core.cache import cache


class EmailPublishOnMemberView(View):
    @login_required
    def post(self, *args, **kwargs):
        """ 사용자에 이메일로 전송하기 """

        dto = EmailPublishOnMemberDto(self.request.POST)
        if not dto.is_valid():
            raise BadRequestError(dto.errors.get_json_data())

        rss = rss_factory(email_publish_on_member_dto=dto)

        try:
            email_sender = EmailSender(
                rss=rss,
                sender=self.request.user,
                receviers=[dto.get_receiver],
                with_cached=True
            )
            email_sender.publish()
        except ConnectionError:
            return HttpResponse(status=409)

        return JsonResponse(status=201, data={
            "desg": "Success"
        })

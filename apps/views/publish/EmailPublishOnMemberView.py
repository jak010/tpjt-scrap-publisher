from __future__ import annotations

from django.core.mail import EmailMessage
from django.http.response import JsonResponse
from django.views import View

from apps.models import PublishMemberHistory
from apps.orm import Member
from libs.rss_requstor.tistory_rss import TistoryRss, TistoryRssData


class EmailPublishOnMemberView(View):
    """ 사용자에 이메일로 전송하기 """

    def post(self, *args, **kwargs):
        to_email = self.request.POST.get('to_email', None)

        # TODO: 로그인한 사용자의 세션으로 변경하기
        member = Member.objects.get(email="test01@test.com")

        tistory_rss = TistoryRss(sub_domain="jakpentest")
        rss = TistoryRssData(tistory_rss.get_entires[0])

        # Email Publish
        email_message = EmailMessage(
            subject=rss.get_title,
            body=rss.get_summary,
            to=[to_email]
        )
        email_message.content_subtype = "html"
        email_message.send()

        # Email Send History
        publish_history = PublishMemberHistory(
            sender=member,
            receiver=to_email,
            title=rss.get_title,
            content=rss.get_summary,
            description=tistory_rss.get_url
        )

        publish_history.save()

        return JsonResponse(status=201, data={
            "desg": "Success"
        })

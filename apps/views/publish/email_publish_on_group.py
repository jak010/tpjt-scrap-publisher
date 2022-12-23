from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.http.response import JsonResponse
from django.views import View

from apps.models import PublishGroupHistory
from libs.rss_requstor.tistory_rss import TistoryRss, TistoryRssData


class EmailPublishOnGroupView(View):
    """ 그룹에 이메일로 전송하기 """

    def post(self, *args, **kwargs):
        group_id = self.kwargs['group_id']

        group = Group.objects.get(pk=group_id)
        group_members = group.user_set.all()
        group_subscribes = group.groupsubscribe_set.all()

        for group_member in group_members:
            for group_subscribe in group_subscribes:

                if group_subscribe.domain == 'tistory':
                    rss = TistoryRss(sub_domain=group_subscribe.sub_domain)
                    latest_rss = TistoryRssData(rss.get_entires[0])

                    # Email Send
                    email_message = EmailMessage(
                        subject=latest_rss.get_title,
                        body=latest_rss.get_summary,
                        to=[group_member.email]
                    )
                    email_message.content_subtype = "html"
                    result = email_message.send()

                    # Email Send History
                    if result != 0:
                        publish_history = PublishGroupHistory(
                            group=group,
                            member=group_member,
                            subscribe=group_subscribe
                        )
                        publish_history.save()

        return JsonResponse(status=201, data={
            "desg": "Success"
        })

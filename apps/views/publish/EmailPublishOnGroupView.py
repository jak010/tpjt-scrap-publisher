from django.views import View
from django.http.response import JsonResponse

from django.contrib.auth.models import Group

from apps.models import PublishGroupHistory
from apps.orm import Member


class EmailPublishOnGroupView(View):
    """ 그룹에 이메일로 전송하기 """

    def post(self, *args, **kwargs):
        group_id = self.kwargs['group_id']

        group = Group.objects.get(pk=group_id)
        group_members = group.user_set.all()
        group_subscribes = group.groupsubscribe_set.all()

        for group_member in group_members:

            for group_subscribe in group_subscribes:
                # Email Send
                # TODO: Implementation

                # Email Send History
                publish_history = PublishGroupHistory(
                    group=group,
                    member=group_member,
                    subscribe=group_subscribe
                )

                publish_history.save()

        return JsonResponse(status=201, data={
            "desg": "Success"
        })

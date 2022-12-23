from django.contrib.auth.models import Group
from django.http.response import JsonResponse
from django.views import View

from ... import orm


class GroupMemberJoinView(View):

    def post(self, *args, **kwargs):
        """ 그룹에 멤버 추가하기  """
        email = self.request.POST.get("email", None)

        # Group Search
        group_id = self.kwargs['group_id']
        group = Group.objects.get(pk=group_id)

        # Member Search
        member = orm.Member.objects.get(email=email)

        # Member Append in Group
        member.groups.add(group)

        return JsonResponse(
            status=201,
            data={
                "MSG": "Member Success Joined Group!",
                'member': member.email,
                'group': group.name
            }
        )

from django.contrib.auth.models import Group
from django.views import View

from django.http.response import HttpResponse, JsonResponse
from django.db import IntegrityError

from ..orm import Member


class GroupView(View):

    def get(self, *args, **kwargs):
        """ 그룹 목록 조회하기 """
        all_group = Group.objects.all()

        items = [{
            'group_id': group.id,
            'group_name': group.name
        } for group in all_group]

        return JsonResponse(
            status=200,
            data={'items': items}
        )

    def post(self, *args, **kwargs):
        """ 그룹 생성하기 """
        group_name = self.request.POST.get('group_name', None)
        if group_name is None:
            return HttpResponse(status=400)

        try:
            new_group = Group.objects.create(
                name=group_name
            )
        except IntegrityError as e:
            return JsonResponse(status=200, data={
                'msg': e.args[1]
            })

        return JsonResponse(
            status=200,
            data={
                'group_id': new_group.id,
                'group_name': new_group.name
            }
        )


class GroupDetailView(View):
    def get(self, *args, **kwargs):
        """ Group 정보 가져오기 """
        group_id = int(self.kwargs['group_id'])

        group = Group.objects.get(id=group_id)

        return JsonResponse(status=200, data={
            'group_id': group.id,
            'group_name': group.name,
            'member': [{
                'member_id': member.id,
                'email': member.email
            } for member in group.user_set.all()]
        })


class GroupMemberView(View):

    def post(self, *args, **kwargs):
        """ 그룹에 멤버 추가하기  """
        email = self.request.POST.get("email", None)
        group_name = self.request.POST.get("group_name", None)

        member = Member.objects.get(email=email)
        group = Group.objects.get(name=group_name)
        member.groups.add(group)

        return JsonResponse(
            status=201,
            data={
                "MSG": "Member Success Joined Group!",
                'member': member.email,
                'group': group.name
            }
        )

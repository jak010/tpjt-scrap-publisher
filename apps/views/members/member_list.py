from django.http import JsonResponse
from django.views import View

from apps.orm import Member

from config.response import Success


class MemberListView(View):
    def get(self, *args, **kwargs):
        """ 사용자 목록조회하기 """
        members = Member.objects.all()

        items = [{
            'member_id': member.id,
            'email': member.email,
            'last_login': member.last_login,
            'date_of_join': member.date_of_join,
            'is_active': member.is_active,
            'groups': [{
                'group_id': group.id,
                'name': group.name
            } for group in member.groups.all()]  # TODO: Cause N+1 Problem !
        } for member in members]

        return JsonResponse(
            status=Success.OK,
            data={
                'items': items
            }
        )

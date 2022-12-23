from django.http import JsonResponse
from django.views import View

from apps.orm import Member


class MemberListView(View):
    def get(self, *args, **kwargs):
        """ 사용자 목록조회하기 """
        members = Member.objects.all()

        items = [{
            'id': member.id,
            'email': member.email
        } for member in members]

        return JsonResponse(status=200, data={'items': items})

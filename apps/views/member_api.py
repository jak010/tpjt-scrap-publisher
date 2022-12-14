from django.views.generic import View
from django.http import JsonResponse

from ..auth import Member


class MemberCreateView(View):

    def post(self, *args, **kwargs):
        email = self.request.POST.get("email", None)
        password = self.request.POST.get('password', None)

        new_member = Member(
            email=email,
            password=password
        )
        new_member.save()

        return JsonResponse(data={})

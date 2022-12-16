from django.contrib.auth.models import Group
from django.views import View

from django.http.response import HttpResponse, JsonResponse
from django.db import IntegrityError


class GroupCreateView(View):

    def post(self, *args, **kwargs):
        group_name = self.request.POST.get('group_name', None)
        if group_name is None:
            return HttpResponse(status=400)

        try:
            new_group = Group.objects.create(name=group_name)
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

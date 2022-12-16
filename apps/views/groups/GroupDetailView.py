from django.contrib.auth.models import Group
from django.views import View

from django.http.response import HttpResponse, JsonResponse
from django.db import IntegrityError


class GroupDetailView(View):
    def get(self, *args, **kwargs):
        """ Group DetailView """
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

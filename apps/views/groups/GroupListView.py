from django.contrib.auth.models import Group
from django.views import View

from django.http.response import HttpResponse, JsonResponse
from django.db import IntegrityError


class GroupListView(View):

    def get(self, *args, **kwargs):
        """ All Group List View """
        all_group = Group.objects.all()

        return JsonResponse(
            status=200,
            data={
                'items': [{
                    'group_id': group.id,
                    'group_name': group.name
                } for group in all_group]}
        )

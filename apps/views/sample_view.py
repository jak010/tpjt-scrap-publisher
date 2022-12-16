from django.http.response import JsonResponse
from django.views import View
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from ..orm import TistoryModel, Member


class SampleView(View):

    def get(self, *args, **kwargs):
        user_id = self.request.GET.get("user_id", None)
        print("Sample")

        user = get_object_or_404(Member, pk=user_id)

        print(user.get_all_permissions())
        print(user.has_perm('apps.ca_tistory_model'))

        return JsonResponse(status=200, data={})

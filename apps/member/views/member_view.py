from __future__ import annotations

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views import View

Member = get_user_model()


class MemberListView(View):
    def get(self, request):
        return JsonResponse(data={})

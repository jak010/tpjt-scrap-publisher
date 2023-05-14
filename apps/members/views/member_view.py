from __future__ import annotations

from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

Member = get_user_model()


class MemberView(TemplateView):
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={})

# class MemberListView(View):
#     def get(self, request):
#         return JsonResponse(data={})
#

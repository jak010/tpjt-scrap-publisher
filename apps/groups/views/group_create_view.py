from ..models import GroupMember
from django.views.generic import TemplateView
from django.http.response import JsonResponse

from ..forms import GroupCreateForm


class GroupCreateView(TemplateView):
    template_name = 'pages/group/group_create.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={'form': GroupCreateForm()})

    def post(self):

        print(self.requests)

        return self.render_to_response(context={'form': GroupCreateForm()})

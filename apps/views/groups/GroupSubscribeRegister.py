from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.models import Group

from ... import orm


class GroupSubscribeRegisterView(View):

    def post(self, *args, **kwargs):
        # Path Parameter
        group_id = self.kwargs['group_id']

        # Request Body
        author = self.request.POST.get('author', None)
        sub_domain = self.request.POST.get("sub_domain", None)
        domain = self.request.POST.get("domain", None)
        top_level_domain = self.request.POST.get('top_level_domain', None)

        group = Group.objects.get(pk=group_id)
        group_subscribe = orm.GroupSubScribe.objects.create(
            author=author,
            sub_domain=sub_domain,
            domain=domain,
            top_level_domain=top_level_domain,
            group=group
        )
        group_subscribe.save()

        return JsonResponse(status=200, data={})

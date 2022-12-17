from django.contrib.auth.models import Group
from django.http.response import JsonResponse
from django.views import View


class GroupDetailView(View):
    def get(self, *args, **kwargs):
        """ Group DetailView """
        group_id = int(self.kwargs['group_id'])

        group = Group.objects.get(id=group_id)
        group_members = group.user_set.all()
        group_subscribes = group.groupsubscribe_set.all()

        return JsonResponse(status=200, data={
            'group_id': group.id,
            'group_name': group.name,
            'members': [{
                'member_id': member.id,
                'email': member.email
            } for member in group_members],
            'subscribes': [{
                'reference_id': subscribe.pk,
                'url': subscribe.url
            } for subscribe in group_subscribes]
        })

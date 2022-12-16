from django.http.response import JsonResponse
from django.views import View
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from ..orm import Member

from libs.rss_requstor.tistory_rss import TistoryRss, TistoryRssData


class SampleView(View):

    def get(self, *args, **kwargs):
        """ Tistory RSS 가져오기 """
        group = Group.objects.get(id=2)

        group_subscribe = group.groupsubscribe_set.all()

        for subscribe in group_subscribe:

            if subscribe.domain == 'tistory':
                rss = TistoryRss(sub_domain=subscribe.sub_domain)

                for entry in rss.get_entires:
                    t = TistoryRssData(entry)
                    print(t.get_title, t.get_published)

        return JsonResponse(status=200, data={
            'group_id ': group.id,
            'group_name ': group.name,
            'subscribe': [{
                'reference_id': subscribe.reference_id,
                'link': subscribe.url,
                'date_of_create': subscribe.date_of_create
            } for subscribe in group_subscribe]
        })

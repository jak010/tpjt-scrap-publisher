from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.models import Group

from ..orm import TistoryModel
from ..libs.rss_requstor.tistory_rss import TistoryRss, TistoryRssData


class TistoryScrapView(View):

    def post(self, *args, **kwargs):
        rss = TistoryRss(sub_domain="jakpentest")

        for entry in rss.get_entires:
            e = TistoryRssData(entry)
            print(e)

        return JsonResponse(status=200, data={})


class TistorySubscribeView(View):

    def post(self, *args, **kwargs):
        author = self.request.POST.get('author', None)
        url = self.request.POST.get('url', None)
        group_id = self.request.POST.get('group_id', None)

        group = Group.objects.get(pk=group_id)

        tistory_subscribe = TistoryModel.objects.create(
            author=author,
            url=url,
            group=group
        )
        tistory_subscribe.save()

        return JsonResponse(status=200, data={})

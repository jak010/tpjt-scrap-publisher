from django.views import View
from django.http.response import JsonResponse

from ..libs.rss_requstor.tistory_rss import TistoryRss, TistoryRssData


class TistoryScrapView(View):

    def post(self, *args, **kwargs):
        rss = TistoryRss(sub_domain="jakpentest")

        for entry in rss.get_entires:
            e = TistoryRssData(entry)
            print(e)

        return JsonResponse(status=200, data={})

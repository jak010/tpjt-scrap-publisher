from django.http.response import JsonResponse
from django.views import View
from django.contrib.syndication.views import Feed

from ..models import TistoryModel


class ArticleTistoryView(Feed):
    title = "Recent Tistory"
    linke = "/rss"
    description = "asdsad"

    def items(self):
        return TistoryModel.objects.filter(
            date_of_create__isnull=False
        ).order_by("-date_of_create")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

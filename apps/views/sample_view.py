from django.http.response import JsonResponse
from django.views import View
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from ..orm import Member

from libs.rss_requstor.tistory_rss import TistoryRss, TistoryRssData

# from django.contrib.auth.decorators import login_required

from config.util import login_required
from django.core.cache import cache, caches
from django.core.mail import EmailMessage

from libs.cache_container import RedisList
from libs.constant import CacheKey
from libs.announce.utils import deserialized_email


class SampleView(View):

    def get(self, *args, **kwargs):
        redis_list = RedisList(
            cache_key=CacheKey.EMAIL_CACHE_KEY
        )

        print(redis_list.size())

        # for email_message in deserialized_email(redis_list.get_all()):
        #     print(email_message)

        return JsonResponse(status=200, data={})

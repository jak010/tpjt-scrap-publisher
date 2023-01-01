from django.http.response import JsonResponse
from django.views import View

# from django.contrib.auth.decorators import login_required

from libs.cache_container import RedisList
from libs.constant import CacheKey


class SampleView(View):

    def get(self, *args, **kwargs):
        redis_list = RedisList(
            cache_key=CacheKey.EMAIL_CACHE_KEY
        )

        print(redis_list.size())

        # for email_message in deserialized_email(redis_list.get_all()):
        #     print(email_message)

        return JsonResponse(status=200, data={})

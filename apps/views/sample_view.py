from django.http.response import JsonResponse
from django.views import View
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from ..orm import Member

from libs.rss_requstor.tistory_rss import TistoryRss, TistoryRssData

# from django.contrib.auth.decorators import login_required

from config.util import login_required


class SampleView(View):

    @login_required
    def get(self, *args, **kwargs):

        return JsonResponse(status=200, data={})

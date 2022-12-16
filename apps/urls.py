# from django.conf.urls import url  # django 4.x 버전 부터는 deprecated 처리

from django.urls import path

from .views import (
    member_api,
    group_api,
    email_send_api,
    article_scrap_api
)

urlpatterns = [

    # Member
    path("member", member_api.MemberCreateView.as_view()),
    path("member/list", member_api.MemberListView.as_view()),
    path("member/login", member_api.MemberLoginView.as_view()),

    # Email Sender
    path("email/send", email_send_api.EmailSendView.as_view()),

    # Article Scrapper
    # path("article/scrap", article_scrap_api.ArticleTistoryView.as_view())
    path("article/tistory", article_scrap_api.TistoryScrapView.as_view()),

    # Group View
    path("group", group_api.GroupView.as_view()),
    path("group/member", group_api.GroupMemberView.as_view())
]

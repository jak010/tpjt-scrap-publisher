# from django.conf.urls import url  # django 4.x 버전 부터는 deprecated 처리

from django.urls import path

from .views import (
    member_api,
    email_send_api,
    article_scrap_api
)

urlpatterns = [

    # Member
    path("member", member_api.MemberCreateView.as_view()),

    # Email Sender
    path("email/send", email_send_api.EmailSendView.as_view()),

    # Article Scrapper
    path("article/scrap", article_scrap_api.ArticleTistoryView.as_view())
]

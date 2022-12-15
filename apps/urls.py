# from django.conf.urls import url  # django 4.x 버전 부터는 deprecated 처리

from django.urls import include, path

from .views import (
    greeting,
    member_api,
    email_send_api
)

urlpatterns = [
    path("", greeting.GreetingView.as_view()),

    # Member
    path("member", member_api.MemberCreateView.as_view()),

    # Email Sender
    path("email/send", email_send_api.EmailSendView.as_view())
]

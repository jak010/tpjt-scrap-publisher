# from django.conf.urls import url  # django 4.x 버전 부터는 deprecated 처리

from django.urls import path, re_path

from .views import (
    member_api,
    group_api,
    email_send_api,
    tistory_subscribe_api,
    sample_view
)

app_name = "apps"

urlpatterns = [

    # Member
    path("member", member_api.MemberCreateView.as_view(), name="member_create"),
    path("member/list", member_api.MemberListView.as_view(), name="member_list"),
    path("member/login", member_api.MemberLoginView.as_view(), name="login"),

    # Email Sender
    path("email/send", email_send_api.EmailSendView.as_view()),

    # Group View
    path("group", group_api.GroupView.as_view()),
    path("group/member", group_api.GroupMemberView.as_view()),
    path("group/<int:group_id>", group_api.GroupDetailView.as_view()),

    # SubScribeView
    path("subscribe/tistory", tistory_subscribe_api.TistorySubscribeView.as_view()),
    path("sample", sample_view.SampleView.as_view())
]

# from django.conf.urls import url  # django 4.x 버전 부터는 deprecated 처리

from django.urls import path

from .views import (
    groups,
    members
)

from .views import (
    email_send_api,
    sample_view
)

app_name = "apps"

urlpatterns = [

    # Member
    path("member", members.MemberCreateView.as_view(), name="member_create"),
    path("member/list", members.MemberListView.as_view(), name="member_list"),
    path("member/login", members.MemberLoginView.as_view(), name="member_login"),

    # Email Sender
    path("email/send", email_send_api.EmailSendView.as_view()),

    # Group View
    path("group/list", groups.GroupListView.as_view()),
    path("group/create", groups.GroupCreateView.as_view()),
    path("group/<int:group_id>", groups.GroupDetailView.as_view()),
    path("group/<int:group_id>/member", groups.GroupMemberJoinView.as_view()),
    path(
        "group/<int:group_id>/subscribe",
        groups.GroupSubscribeRegisterView.as_view(),
        name='group_subscribe_register'
    ),

    # SubScribeView
    # path("subscribe/tistory", tistory_subscribe_api.TistorySubscribeView.as_view()),
    path("sample", sample_view.SampleView.as_view())
]

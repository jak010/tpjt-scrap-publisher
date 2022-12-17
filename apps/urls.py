from django.urls import path

from .views import (
    groups,
    members,
    publish
)

app_name = "apps"

urlpatterns = [

    # Member
    path("member", members.MemberCreateView.as_view(), name="member_create"),
    path("member/list", members.MemberListView.as_view(), name="member_list"),
    path("member/login", members.MemberLoginView.as_view(), name="member_login"),

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

    # Publish View
    path("publish/email/groups/<int:group_id>", publish.EmailPublishOnGroupView.as_view()),
    path("publish/email/member", publish.EmailPublishOnMemberView.as_view()),
]

from django.urls import path

from apps.layer.views import (
    groups,
    members,
    publish,
    sample_view
)

from django.http import HttpResponse

app_name = "apps"


def member_exception(request):
    print(request)
    return HttpResponse(status=200)


urlpatterns = [
    # Sample
    path("sample", sample_view.SampleView.as_view()),

    # Member
    path("member", members.MemberCreateView.as_view(), name="member_create"),
    path("member/list", members.MemberListView.as_view(), name="member_list"),
    path("member/login", members.MemberLoginView.as_view(), name="member_login"),
    path("member/exception", member_exception, name="member_exception"),

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
    path("publish/email/group/<int:group_id>", publish.EmailPublishOnGroupView.as_view()),
    path("publish/email/member", publish.EmailPublishOnMemberView.as_view()),
]

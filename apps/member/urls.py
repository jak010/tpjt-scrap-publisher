from django.urls import path

from apps import member

from django.http import HttpResponse

from .views import (
    MemberListView,
    MemberCreateView
    # MemberCreateView,
    # MemberLoginView,
    # MemberListView,
    # MemberDetailView
)

from . import views

app_name = "apps"


def member_exception(request):
    print(request)
    return HttpResponse(status=200)


urlpatterns = [

    # Member
    path("", MemberListView.as_view(), name="member_list"),
    path("/create", views.member_view.member_create_view, name="member_create")

    # path("member", MemberCreateView.as_view(), name="member_create"),
    # path("member/list", MemberListView.as_view(), name="member_list"),
    # path("member/login", MemberLoginView.as_view(), name="member_login"),
    # path("member/exception", member_exception, name="member_exception"),
]

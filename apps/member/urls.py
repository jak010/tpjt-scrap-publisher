from __future__ import annotations

from django.urls import path

from apps.member.views import (
    member_view,
    member_login_view,
    member_signup_view,
    member_profile_view
)

app_name = "apps"

urlpatterns = [
    path("base", member_view.MemberView.as_view(), name="member_view"),

    path("create", member_signup_view.MemberCreateView.as_view(), name="member_create"),
    path("login", member_login_view.MemberLoginView.as_view(), name="member_login"),
    path("profile", member_profile_view.MemberProfileView.as_view(), name="member_profile")
]

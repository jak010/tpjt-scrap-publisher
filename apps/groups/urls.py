from django.urls import path

from .views import (
    group_create_view
)

app_name = "group"

urlpatterns = [
    path('group/create', group_create_view.GroupCreateView.as_view(), name="create")

]

from django.conf.urls import url  # django 4.x 버전 부터는 deprecated 처리

from .views import (
    greeting
)

urlpatterns = [
    url("^$", greeting.GreetingView.as_view()),
]

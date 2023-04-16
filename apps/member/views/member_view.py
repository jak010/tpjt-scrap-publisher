from django.http import JsonResponse
from django.views import View

from django import forms

from django.contrib.auth import get_user_model

from ..service import member_service

Member = get_user_model()


class MemberCreateForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)


class MemberListView(View):
    def get(self, request):
        print(request)
        return JsonResponse(data={})


class MemberCreateView(View):

    def post(self, request):
        form = MemberCreateForm(request.POST)
        if form.is_valid():
            member_service.create_member(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

        return JsonResponse(data={})


from django.shortcuts import render


def member_create_view(request):
    return render(request, "src/member/create.html", {
        'name': 'hello'
    })

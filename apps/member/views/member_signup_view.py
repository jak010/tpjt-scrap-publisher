from __future__ import annotations

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from apps.member.form import MemberSignUpForm
from apps.member.service import member_service

from django.shortcuts import render


class MemberCreateView(TemplateView):
    template_name = "src/member/signup.html"

    def get(self, *args, **kwargs):
        return self.render_to_response(
            context={'form': MemberSignUpForm()}
        )

    def post(self, request):
        form = MemberSignUpForm(request.POST)

        if not form.is_valid():
            return HttpResponseRedirect(request.path)

        try:
            member_service.create_member(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
        except member_service.MemberEmailAlreadyExistError:
            messages.error(request, "이미 존재하는 사용자입니다. 다시 입력해주세요")
            return self.render_to_response(context={'form': MemberSignUpForm()})

        return HttpResponseRedirect("login")

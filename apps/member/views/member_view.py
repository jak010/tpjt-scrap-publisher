from __future__ import annotations

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from apps.member.form import MemberCreateForm, MemberLoginForm
from ..service import member_service

Member = get_user_model()


class MemberListView(View):
    def get(self, request):
        return JsonResponse(data={})


class MemberCreateView(TemplateView):
    template_name = "src/member/signup.html"

    def post(self, request):
        form = MemberCreateForm(request.POST)

        if not form.is_valid():
            return HttpResponseRedirect(request.path)

        try:
            member_service.create_member(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

        except member_service.MemberEmailAlreadyExistError:
            messages.error(request, "이미 존재하는 사용자입니다. 다시 입력해주세요")

        return self.render_to_response(context={})


class MemberLoginView(TemplateView):
    template_name = "src/member/login.html"

    def post(self, request):
        form = MemberLoginForm(request.POST)

        if form.is_valid():
            result = member_service.login(
                request=self.request,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if result is not None:
                return self.render_to_response(context={
                    'result': 'error',
                    'message': result
                })
            return redirect('index')

        return self.render_to_response(context={})

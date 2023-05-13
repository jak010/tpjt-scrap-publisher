from __future__ import annotations

from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.member.form import MemberLoginForm
from apps.member.service import member_service


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

from __future__ import annotations

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from apps.members.form import MemberLoginForm
from apps.members.service import member_service


class MemberLoginView(TemplateView):
    template_name = "src/member/login.html"

    def get(self, *args, **kwargs):
        return self.render_to_response(
            context={'form': MemberLoginForm()}
        )

    def post(self, request):
        form = MemberLoginForm(request.POST)
        if not form.is_valid():
            return self.render_to_response(context={'form': MemberLoginForm()})

        try:
            member_service.login(
                request=self.request,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
        except PermissionDenied:
            messages.error(request, "Permission Denined")
            return self.render_to_response(
                context={
                    'form': MemberLoginForm(),
                    'message': 'Login Failed'
                })

        return HttpResponseRedirect('/members/profile')

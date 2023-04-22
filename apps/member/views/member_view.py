from django.http import JsonResponse
from django.views import View

from django.views.generic import TemplateView

from django.contrib.auth import get_user_model

from apps.member.form import MemberCreateForm

from ..service import member_service

Member = get_user_model()


class MemberListView(View):
    def get(self, request):
        return JsonResponse(data={})


class MemberCreateView(TemplateView):
    template_name = "src/member/create.html"

    def post(self, request):
        form = MemberCreateForm(request.POST)
        if form.is_valid():
            member_service.create_member(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

        return self.render_to_response(context={})

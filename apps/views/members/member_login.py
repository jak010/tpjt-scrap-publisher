from __future__ import annotations

import backoff as check
from django.http import JsonResponse
from django.views import View

from apps.layer.exceptions import member_exceptions
from apps.layer.service import member_service
from config.response import Success
from config.util import Exceptable
from .dto import MemberLoginFormDto


class MemberLoginView(View):

    @Exceptable(
        expects=[
            member_exceptions.MemberAuthenticateFailError,  # Credential을 잘못 입력한 경우
            member_exceptions.MemberLoginFailError  # member의 active 상태가 0인 경우
        ]
    )
    def post(self, *args, **kwargs):
        """ Django Session 기반 유저 로그인 """

        member_login_form_dto = MemberLoginFormDto(self.request.POST)
        member_login_form_dto.is_valid()

        member_authenticate = member_service.member_authenticate(
            request=self.request,
            login_email=member_login_form_dto.get_email,
            login_password=member_login_form_dto.get_password
        )

        member_session = member_service.get_session(
            request=self.request,
            auth=member_authenticate
        )

        return JsonResponse(
            status=Success.OK.value,
            data={
                'session_key': member_session.session_key,
                "expire_date": member_session.get_expiry_date()
            }
        )

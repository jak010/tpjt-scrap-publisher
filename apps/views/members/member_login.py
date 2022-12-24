from __future__ import annotations

from typing import Union

import backoff as check
from django.http import JsonResponse
from django.views import View

from apps.layer.exceptions import member_exceptions
from apps.layer.service.member_service import MemberAuthenticateService, MemberLoginService
from .dto import MemberLoginFormDto


class MemberLoginView(View):

    @check.on_exception(
        check.expo, max_tries=1, raise_on_giveup=True,
        exception=(
                member_exceptions.MemberAuthenticateFailError,
        )
    )
    def post(self, *args, **kwargs):
        """ Django Session 기반 유저 로그인 """

        member_login_form_dto = MemberLoginFormDto(self.request.POST)
        member_login_form_dto.is_valid()

        member_authenticate_service: Union[
            MemberAuthenticateService,
            member_exceptions.MemberAuthenticateFailError
        ] = MemberAuthenticateService(
            login_email=member_login_form_dto.get_email,
            login_password=member_login_form_dto.get_password
        )

        member_login_service = MemberLoginService.login(
            request=self.request,
            auth=member_authenticate_service.check_authenticate()
        )

        return JsonResponse(status=200, data={
            'session_key': member_login_service.session.session_key,
            "expire_date": member_login_service.session.get_expiry_date()
        })

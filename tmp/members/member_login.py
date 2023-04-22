# from __future__ import annotations
#
# from typing import Union, Any
#
# from django.http import JsonResponse
# from django.views import View
#
# from apps.member.exceptions import (
#     BadRequestError
# )
# from apps.member.exceptions import member_exceptions
# from apps.member.service import member_service
# from config.response import Success
# from apps.member.dto import MemberLoginFormDto
#
#
# class MemberLoginView(View):
#
#     def post(self, *args, **kwargs) -> Union[
#         JsonResponse,
#         Any[
#             member_exceptions.MemberDoesNotExit,
#             member_exceptions.MemberPasswordNotMatched,
#             member_exceptions.MemberDeActivateLogin,
#         ]
#     ]:
#         """ Django Session 기반 유저 로그인 """
#
#         member_login_form_dto = MemberLoginFormDto(self.request.POST)
#         if not member_login_form_dto.is_valid():
#             raise BadRequestError(member_login_form_dto.errors.get_json_data())  # XXX: 개선필요함
#
#         member_service.member_authenticate(
#             request=self.request,
#             login_email=member_login_form_dto.get_email,
#             login_password=member_login_form_dto.get_password
#         )
#
#         member_session = member_service.get_session(
#             request=self.request
#         )
#
#         return JsonResponse(
#             status=Success.OK.value,
#             data={
#                 'session_key': member_session.session_key,
#                 "expire_date": member_session.get_expiry_date()
#             }
#         )

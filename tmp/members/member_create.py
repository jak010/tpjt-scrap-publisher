# from __future__ import annotations
#
# from http import HTTPStatus
#
# from django.http import JsonResponse
# from django.views import View
#
# from apps.member.dto.MemberCreateDto import MemberCreateFormDto
# from apps.member.service import member_service
#
#
# class MemberCreateView(View):
#
#     def post(self, *args, **kwargs):
#         """ 사용자 생성하기  """
#         member_create_form_dto = MemberCreateFormDto(self.request.POST)
#         if not member_create_form_dto.is_valid():
#             raise BadRequestError(member_create_form_dto.errors.get_json_data())  # XXX: 개선필요함
#
#         new_member = member_service.create_member(
#             email=member_create_form_dto.get_email,
#             password=member_create_form_dto.get_password
#         )
#
#         return JsonResponse(
#             status=HTTPStatus.CREATED,
#             data={
#                 "member_id": new_member.id
#             })

# from django.http import JsonResponse
# from django.views import View
#
# from apps.member.service import member_service
# from config.response import Success
#
#
# class MemberListView(View):
#     def get(self, *args, **kwargs):
#         """ 사용자 목록조회하기 """
#
#         return JsonResponse(
#             status=Success.OK.value,
#             data={
#                 'items': member_service.get_members()
#             }
#         )
#
#
# class MemberDetailView(View):
#     def get(self, *args, **kwargs):
#         """ 사용자 목록조회하기 """
#
#         return JsonResponse(data={})

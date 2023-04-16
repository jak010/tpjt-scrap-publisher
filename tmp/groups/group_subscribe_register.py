# from django.contrib.auth.models import Group
# from django.http.response import JsonResponse
# from django.views import View
#
# from .dto.GroupSubScribeFormDto import GroupSubScribeFormDto
# # from apps import orm
#
# from apps.member.exceptions import BadRequestError
#
#
# class GroupSubscribeRegisterView(View):
#
#     def post(self, *args, **kwargs):
#         # Path Parameter
#         group_id = self.kwargs['group_id']
#
#         group_subscribe_form_dto = GroupSubScribeFormDto(self.request.POST)
#         if not group_subscribe_form_dto.is_valid():
#             raise BadRequestError(group_subscribe_form_dto.errors.get_json_data())
#
#         group = Group.objects.get(pk=group_id)
#
#         group_subscribe = orm.GroupSubScribe.objects.create(
#             author=group_subscribe_form_dto.get_author,
#             sub_domain=group_subscribe_form_dto.get_sub_domain,
#             domain=group_subscribe_form_dto.get_domain,
#             top_level_domain=group_subscribe_form_dto.get_top_level_domain,
#             group=group
#         )
#         group_subscribe.save()
#
#         return JsonResponse(status=200, data={})

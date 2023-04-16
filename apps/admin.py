from django.contrib import admin

#
# from .models import (
#     Member,
#     GroupSubScribe,
#     PublishGroupHistory,
#     PublishMemberHistory,
#     RecommandLink
# )
#
# from django.utils.translation import gettext as _
#
#
# # Register your models here.
# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Member', {'fields': [
#             'email',
#             'password',
#             'last_login',
#         ]}),
#         ('Member Info', {'fields': [
#             'is_active',
#             'is_staff',
#             'is_superuser'
#         ]}),
#     ]
#
#     list_display = (
#         _('email'),
#         'last_login',
#         'is_active',
#         'is_staff',
#         'is_superuser')
#
#     search_fields = ['email']
#
#
# @admin.register(RecommandLink)
# class RecommandLinkAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Link', {'fields': [
#             'sub_domain', 'domain', 'top_level_domain'
#         ]}),
#         ('Score', {'fields': [
#             'rate', 'like', 'hit'
#         ]})
#     ]
#
#     list_display = (
#         'reference_id',
#         'sub_domain', 'domain', 'top_level_domain',
#         'rate', 'like', 'hit'
#     )
#
#
# admin.site.register(GroupSubScribe)
# admin.site.register(PublishGroupHistory)
# admin.site.register(PublishMemberHistory)

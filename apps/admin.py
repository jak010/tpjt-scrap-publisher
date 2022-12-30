from django.contrib import admin

from .models import (
    Member,
    GroupSubScribe,
    PublishGroupHistory,
    PublishMemberHistory,
    RecommandLink
)


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Member', {'fields': [
            'email',
            'password',
            'last_login',
        ]}),
        ('Member Info', {'fields': [
            'is_active',
            'is_staff',
            'is_superuser'
        ]}),
    ]

    list_display = (
        'email',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser')

    search_fields = ['email']


admin.site.register(Member, MemberAdmin)
admin.site.register(GroupSubScribe)
admin.site.register(PublishGroupHistory)
admin.site.register(PublishMemberHistory)
admin.site.register(RecommandLink)

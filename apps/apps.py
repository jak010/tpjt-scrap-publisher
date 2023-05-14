from django.apps import AppConfig


# class AppsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'apps'


class MemberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.members'


class GroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.groups'

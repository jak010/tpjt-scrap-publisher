from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models

from .group_subscribe import GroupSubScribe

member = get_user_model()


class PublishGroupHistory(models.Model):
    class Meta:
        db_table = "publish_group_history"
        verbose_name = '이메일 전송 내역(그룹)'
        verbose_name_plural = '이메일 전송 내역(그룹)'

    reference_id = models.AutoField(primary_key=True)

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(member, on_delete=models.SET_NULL, null=True)
    subscribe = models.ForeignKey(GroupSubScribe, on_delete=models.SET_NULL, null=True)

    date_of_create = models.DateTimeField(auto_now_add=True)

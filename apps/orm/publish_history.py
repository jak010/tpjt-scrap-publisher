from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models

from .group_subscribe import GroupSubScribe

member = get_user_model()


class PublishHistory(models.Model):
    class Meta:
        db_table = "publish_history"

    reference_id = models.AutoField(primary_key=True)

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(member, on_delete=models.SET_NULL, null=True)
    subscribe = models.ForeignKey(GroupSubScribe, on_delete=models.SET_NULL, null=True)

    date_of_create = models.DateTimeField(auto_now_add=True)

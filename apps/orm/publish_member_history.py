from django.contrib.auth import get_user_model
from django.db import models

member = get_user_model()


class PublishMemberHistory(models.Model):
    class Meta:
        db_table = "publish_member_history"

    reference_id = models.AutoField(primary_key=True)

    sender = models.ForeignKey(member, on_delete=models.SET_NULL, null=True)
    receiver = models.CharField(max_length=128, null=False)
    title = models.CharField(max_length=256)
    content = models.TextField()
    description = models.CharField(max_length=512)

    date_of_create = models.DateTimeField(auto_now_add=True)

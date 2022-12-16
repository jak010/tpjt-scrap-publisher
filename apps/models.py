from .orm import (
    Member,
    TistoryModel
)

from django.contrib.auth import get_user_model
from django.db import models

member = get_user_model()


# Create your models here.


class EmailHistory(models.Model):
    class Meta:
        db_table = "email_history"

    reference_id = models.AutoField(primary_key=True)

    sender = models.CharField(
        max_length=36,
        db_column="sender"
    )
    receiver = models.ForeignKey(
        member,
        on_delete=models.SET_NULL,
        null=True,
        db_column="receiver"
    )

    date_of_send = models.DateTimeField(auto_now_add=True)
    date_of_resend = models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import Group


class TistoryModel(models.Model):
    class Meta:
        db_table = "tistory_subscribe"

    reference_id = models.AutoField(
        primary_key=True
    )
    author = models.CharField(
        verbose_name="author",
        max_length=120
    )
    url = models.URLField(verbose_name="link")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='group')
    date_of_create = models.DateTimeField(auto_now=True)

    objects = models.Manager()

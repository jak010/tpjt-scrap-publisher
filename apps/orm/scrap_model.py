from django.db import models


class TistoryModel(models.Model):
    class Meta:
        db_table = "tistory_post"

    reference_id = models.AutoField(
        primary_key=True
    )

    author = models.CharField(
        verbose_name="author",
        max_length=120
    )
    title = models.CharField(
        verbose_name="title",
        max_length=120
    )
    content = models.TextField(
        verbose_name="content"
    )

    objects = models.Manager()

    date_of_create = models.DateTimeField(auto_now=True)

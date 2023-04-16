from django.db import models
from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model

Member = get_user_model()


class RecommandLink(models.Model):
    class Meta:
        db_table = "recommand_link"
        verbose_name = '추천 링크 목록'
        verbose_name_plural = '추천 링크 목록'

    reference_id = models.AutoField(
        primary_key=True
    )
    register = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)

    sub_domain = models.CharField(verbose_name='sub domain', max_length=36)
    domain = models.CharField(verbose_name='domain', max_length=36)
    top_level_domain = models.CharField(verbose_name='top level domain', max_length=36)

    rate = models.IntegerField(verbose_name="rate")
    like = models.IntegerField(verbose_name="like")
    hit = models.IntegerField(verbose_name="hit")

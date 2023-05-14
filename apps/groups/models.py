from django.contrib.auth import get_user_model
from django.db import models

Member = get_user_model()


class Group(models.Model):
    class Meta:
        db_table = "group"
        verbose_name = '그룹'

    name = models.CharField(
        max_length=36,
        unique=True,
        verbose_name="email"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="설명"
    )
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)

    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)


class GroupMember(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_of_join = models.DateTimeField(auto_now_add=True)


class GroupLink(models.Model):
    class Meta:
        db_table = "group_link"
        verbose_name = '그룹에서 공유되는 링크들'

    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    link = models.TextField()

    register = models.CharField(
        max_length=255,
        verbose_name="등록한 사람"
    )

    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

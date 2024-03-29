from django.db import models
from django.contrib.auth.models import Group


class GroupSubScribe(models.Model):
    class Meta:
        db_table = "group_subscribe"
        verbose_name = '그룹 구독'
        verbose_name_plural = '그룹 구독'

    reference_id = models.AutoField(
        primary_key=True
    )
    author = models.CharField(
        verbose_name="author",
        max_length=36
    )

    sub_domain = models.CharField(verbose_name='sub_domain', max_length=36)
    domain = models.CharField(verbose_name='domain', max_length=36)
    top_level_domain = models.CharField(verbose_name='top_level_domain', max_length=36)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='group')
    date_of_create = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    @property
    def url(self):
        return "https://" + \
               str(self.sub_domain) + "." + \
               str(self.domain) + "." + \
               str(self.top_level_domain)


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

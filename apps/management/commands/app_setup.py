from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group

from ...orm import Member, GroupSubScribe


class Command(BaseCommand):
    help = "초기 데이터 생성"

    COMMON_EMAILS = ["test01@test.com", "test02@test.com", "test03@test.com"]
    COMMON_PASSWORD = "1234"

    GROUP_NAME = "test"

    def add_arguments(self, parser):
        parser.add_argument("init", type=str)

    def handle(self, *args, **options):
        flag = options['init']

        if flag == 'all':
            self.make_member()
            self.make_group()
            self.make_group_member()
            self.make_group_subscribe()

    def make_member(self):
        for email in self.COMMON_EMAILS:
            new_member01 = Member(email=email)
            new_member01.set_password(self.COMMON_PASSWORD)
            new_member01.save()

    def make_group(self):
        g = Group(name=self.GROUP_NAME)
        g.save()

    def make_group_member(self):
        g = Group.objects.get(name=self.GROUP_NAME)

        for email in self.COMMON_EMAILS:
            m = Member.objects.get(email=email)
            m.groups.add(g)

    def make_group_subscribe(self):
        g = Group.objects.get(name=self.GROUP_NAME)

        group_subscribe = GroupSubScribe.objects.create(
            author="jakpentest",
            sub_domain="jakpentest",
            domain="tistory",
            top_level_domain="com",
            group=g
        )
        group_subscribe.save()

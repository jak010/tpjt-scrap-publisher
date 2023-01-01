from __future__ import annotations

import pickle

from django.core.mail import EmailMessage

from apps.models import PublishMemberHistory
from libs.redis_container import RedisList
from libs.constant import CacheKey


class EmailSender:

    def __init__(self,
                 *,
                 rss,
                 subject,  # 이메일 제목
                 sender,
                 receviers: list[str],
                 content_type="html",
                 ):

        self.rss = rss
        self.subject = subject
        self.sender = sender
        self.receviers = receviers
        self.content_type = content_type

    def publish(self):
        """ Email 보내기 """
        email_message = self._get_email_message_instance()

        result = email_message.send()

        if result != 0:
            self._history_save()
        else:
            # TODO:  Email 전송에 실패한 경우 뭘 할까?
            raise RuntimeError()

        return email_message

    def publish_with_scheduled(self):
        """ Email 스케쥴링 하기 """
        email_message = self._get_email_message_instance()
        serialized = pickle.dumps(email_message)

        redis_list = RedisList(cache_key=CacheKey.EMAIL_CACHE_KEY)
        redis_list.lpush(serialized)

        return redis_list

    def _get_email_message_instance(self) -> EmailMessage:
        email_message = EmailMessage(
            subject=self.subject,
            body="<h1>" + self.rss.get_title + "</h1>" + "\n" + self.rss.get_summary,
            to=self.receviers,
        )
        email_message.content_subtype = "html"

        return email_message

    def _history_save(self):
        for receiver in self.receviers:
            publish_history = PublishMemberHistory(
                sender=self.sender,
                receiver=receiver,
                title=self.rss.get_title,
                content=self.rss.get_summary,
                description=self.rss.get_summary_detail
            )
            publish_history.save()

from __future__ import annotations

import pickle
import time
from datetime import datetime
from typing import TYPE_CHECKING

from apps.models import PublishMemberHistory
from libs.constant import CacheKey
from libs.wrapper.redis.redis_list import RedisList

if TYPE_CHECKING:
    from .message import EmailMessage


class EmailSender:

    def __init__(self,
                 *,
                 email_message: EmailMessage,
                 sender,
                 receviers
                 ):

        self.email_message: EmailMessage = email_message
        self.sender: str = sender
        self.receviers: list[str] = receviers

    def publish(self):
        """ Email 보내기 """
        if self.email_message.send() != 0:
            self._history_save()
            return datetime.now()

        raise RuntimeError()  # TODO:  Email 전송에 실패한 경우 뭘 할까?

    def publish_with_scheduled(self) -> int:
        """ Email 스케쥴링 하기 """
        redis_list = RedisList(
            cache_key=CacheKey.EMAIL_CACHE_KEY
        )
        redis_list.lpush(self._serialized)

        return redis_list.size()

    def _history_save(self):
        for receiver in self.receviers:
            publish_history = PublishMemberHistory(
                sender=self.sender,
                receiver=receiver,
                title=self.email_message.content_title,
                content=self.email_message.content_body,
                description="COMPLETE::" + str(time.time())
            )
            publish_history.save()

    @property
    def _serialized(self):
        return pickle.dumps(self.email_message)

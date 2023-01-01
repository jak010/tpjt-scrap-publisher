from __future__ import annotations

from django_redis import get_redis_connection
from functools import cached_property

from libs.constant import CacheKey


class RedisContext:
    """ Redis Container """

    def __init__(self, cache_key: CacheKey):
        self.cache_key = cache_key.value

    @cached_property
    def rcon(self):
        return get_redis_connection("default")

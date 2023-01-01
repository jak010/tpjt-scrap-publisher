from __future__ import annotations

from functools import cached_property

from django_redis import get_redis_connection
from django_redis.client import DefaultClient
from libs.constant import CacheKey

from django.core.cache import cache


class RedisContainer:
    """ Redis Container """

    def __init__(self, cache_key: CacheKey):
        self.cache_key = cache_key.value

    @property
    def rcon(self):
        return get_redis_connection("default")


class RedisList(RedisContainer):
    """ Redis List Data Structure """

    def __init__(self, cache_key: CacheKey):
        super(RedisList, self).__init__(
            cache_key=cache_key,
        )

    def lpush(self, value):
        return self.rcon.lpush(self.cache_key, value)

    def lpop(self):
        return self.rcon.lpop(self.cache_key)

    def lrange(self):
        return self.rcon.lrange(self.cache_key, 0, -1)

    def size(self):
        return len(self.lrange())

    def __str__(self):
        return self.rcon.get(self.cache_key)

    def __getitem__(self, _slice_type: slice):
        return self.rcon.lrange(self.cache_key, _slice_type.start, _slice_type.stop)

    def __iter__(self):
        for item in self.rcon.get(self.cache_key):
            yield item

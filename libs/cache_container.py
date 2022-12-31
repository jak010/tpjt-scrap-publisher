from __future__ import annotations

from functools import cached_property

from django_redis import get_redis_connection

from libs.constant import CacheKey


class RedisContainer:
    """ Redis Container """

    def __init__(self, cache_key: CacheKey, name="default"):
        self.cache_key = cache_key.value
        self.name = name

    @cached_property
    def rcon(self):
        return get_redis_connection(self.name)


class RedisList(RedisContainer):
    """ Redis List Data Structure """

    def __init__(self, cache_key: CacheKey, name="default"):
        super(RedisList, self).__init__(
            cache_key=cache_key,
            name=name
        )

    def append(self, value):
        self.rcon.lpush(self.cache_key, value)

    def pop(self):
        return self.rcon.lpop(self.cache_key)

    def get_all(self):
        return self.rcon.lrange(self.cache_key, 0, -1)

    def size(self):
        return len(self.get_all())

    def __str__(self):
        return self.rcon.get(self.cache_key)

    def __getitem__(self, _slice_type: slice):
        return self.rcon.lrange(self.cache_key, _slice_type.start, _slice_type.stop)

    def __iter__(self):
        for item in self.rcon.get(self.cache_key):
            yield item

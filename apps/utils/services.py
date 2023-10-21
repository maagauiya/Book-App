import redis
from django.conf import settings


class RedisManager:
    def __init__(self):
        self.redis_instance = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True
        )

    def validate_in_redis(self, key, value):
        r_value = self.redis_instance.get(key)
        return r_value == value

    def check_in_redis(self, key):
        return self.redis_instance.get(key)

    def delete_from_redis(self, key):
        self.redis_instance.delete(key)
        return True

    def scan_key_in_redis(self, value, prefix):
        for key in self.redis_instance.scan_iter():
            if key.startswith(prefix):
                if self.redis_instance.get(key) == str(value):
                    return key
        return None

    def add_to_redis(self, key, value, ex):
        self.redis_instance.set(key, value, ex=ex)
        return True

    def get_key_ttl(self, key):
        return self.redis_instance.ttl(key)

    def incr_key(self, key):
        return self.redis_instance.incr(key)

    def key_exists(self, key):
        return self.redis_instance.exists(key)
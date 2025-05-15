from typing import Callable, Any

from redis.asyncio import Redis

from src.config import config


def initialize(func: Callable[..., Any]):
    initialized = None

    def wrapper(*args, **kwargs):
        nonlocal initialized
        if initialized is None:
            initialized = func(*args, **kwargs)
        return initialized

    return wrapper


@initialize
def get_redis_client():
    return Redis.from_url(config.redis.redis_url)

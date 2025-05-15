import json
from datetime import datetime, timedelta
from functools import wraps
from hashlib import md5
from typing import Any, Callable

from src.cache.redis import get_redis_client

type CacheKey = str
type ExpireTime = timedelta


def cache(func: Callable[..., Any]):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        cache_key = _get_cache_key(func, *args, **kwargs)

        redis_client = get_redis_client()

        data = await redis_client.get(cache_key)
        if data is not None:
            return json.loads(data)

        result = await func(*args, **kwargs)
        expire_time = _get_expire_time()
        await redis_client.set(cache_key, json.dumps(result), ex=expire_time)
        return result

    return wrapper


def _get_cache_key(func: Callable[..., Any], *args, **kwargs) -> CacheKey:
    func_w_params_str = f"{func.__name__}"
    for arg in args:
        func_w_params_str += f":{arg}"
    for key, value in kwargs.items():
        func_w_params_str += f":{key}={value}"
    return md5(func_w_params_str.encode()).hexdigest()


def _get_expire_time() -> ExpireTime:
    now = datetime.now()
    target_date = now.replace(hour=14, minute=11, second=0, microsecond=0)

    if now >= target_date:
        target_date += timedelta(days=1)

    return target_date - now

from redis.asyncio import Redis

from src.ioc import container


async def get_redis_client() -> Redis:
    async with container() as di_container:
        return await di_container.get(Redis)

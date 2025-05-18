from datetime import date
from typing import AsyncGenerator, Any

import pytest
from sqlalchemy import NullPool, insert
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession
from redis.asyncio import Redis

from src.base.model import Base
from src.config import config
from src.trading.models import TradingResult

type ListTradingData = list[dict[str, Any]]


@pytest.fixture(scope='session')
def async_engine() -> AsyncEngine:
    return create_async_engine(config.postgres.db_url, echo=False, poolclass=NullPool)


@pytest.fixture(scope="session")
def async_session_maker(async_engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(async_engine, expire_on_commit=False)


@pytest.fixture
async def async_session(async_session_maker: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
async def prepare_database(async_engine: AsyncEngine, trading_data: ListTradingData) -> AsyncGenerator[None, None]:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(insert(TradingResult).values(trading_data))
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session", autouse=True)
async def prepare_redis() -> AsyncGenerator[Redis, None]:
    redis = Redis.from_url(config.redis.redis_url)
    yield redis
    await redis.flushdb()


@pytest.fixture(scope="session")
def trading_data() -> ListTradingData:
    return [
        {
            "exchange_product_id": "A100NVY060F",
            "exchange_product_name": "Бензин (АИ-100-К5), ст. Новоярославская (ст. отправления)",
            "oil_id": "A100",
            "delivery_basis_id": "NVY",
            "delivery_basis_name": "ст. Новоярославская",
            "delivery_type_id": "F",
            "volume": 60,
            "total": 5997120.00,
            "count": 1,
            "date": date(2024, 8, 7),
        },
        {
            "exchange_product_id": "A592ACH005A",
            "exchange_product_name": "Бензин (АИ-100-К5), ст. Стенькино II (ст. отправления)",
            "oil_id": "A592",
            "delivery_basis_id": "ACH",
            "delivery_basis_name": "Ачинский НПЗ",
            "delivery_type_id": "A",
            "volume": 100,
            "total": 6042000.00,
            "count": 1,
            "date": date(2024, 8, 8),
        },
        {
            "exchange_product_id": "A10KZLY060W",
            "exchange_product_name": "Бензин (АИ-100-К5)-Евро, ст. Злынка-Экспорт (промежуточная станция)",
            "oil_id": "A10K",
            "delivery_basis_id": "ZLY",
            "delivery_basis_name": "ст. Злынка-Экспорт",
            "delivery_type_id": "W",
            "volume": 120,
            "total": 10656000.00,
            "count": 2,
            "date": date(2024, 8, 9),
        },
    ]

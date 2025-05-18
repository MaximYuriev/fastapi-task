import datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.trading.interfaces import TradingResultRepository
from src.trading.repository import SQLAlchemyTradingResultRepository
from src.trading.service import TradingResultService

type StartPeriodDate = datetime.date
type EndPeriodDate = datetime.date


@pytest.fixture
def trading_repository(async_session: AsyncSession) -> TradingResultRepository:
    return SQLAlchemyTradingResultRepository(async_session)


@pytest.fixture(scope="session")
def period() -> tuple[StartPeriodDate, EndPeriodDate]:
    return datetime.date(2024, 8, 7), datetime.date(2024, 8, 9)


@pytest.fixture
def trading_service(trading_repository: TradingResultRepository) -> TradingResultService:
    return TradingResultService(trading_repository)

import datetime
from typing import Iterable

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.trading.interfaces import TradingResultRepository
from src.trading.models import TradingResult


class SQLAlchemyTradingResultRepository(TradingResultRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_trading_date_count(self) -> int:
        query = select(
            func.count(
                func.distinct(TradingResult.date)
            )
        )
        query_result = await self._session.execute(query)
        return query_result.scalar()

    async def get_last_trading_date(self, limit: int, offset: int) -> Iterable[datetime.date]:
        query = (
            select(TradingResult.date)
            .distinct()
            .order_by(TradingResult.date.desc())
            .limit(limit)
            .offset(offset)
        )
        result = await self._session.scalars(query)
        return result.all()

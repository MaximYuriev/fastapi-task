import datetime
from typing import Any

from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.trading.interfaces import TradingResultRepository
from src.trading.models import TradingResult as TradingResultModel
from src.trading.schemas.responses import TradingResult, TradingDay


class SQLAlchemyTradingResultRepository(TradingResultRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_trading_date_count(self) -> int:
        query = select(
            func.count(
                func.distinct(TradingResultModel.date)
            )
        )
        query_result = await self._session.execute(query)
        return query_result.scalar()

    async def get_last_trading_date(self, limit: int, offset: int) -> list[TradingDay]:
        query = (
            select(TradingResultModel.date)
            .distinct()
            .order_by(TradingResultModel.date.desc())
            .limit(limit)
            .offset(offset)
        )
        days = await self._session.scalars(query)

        return [TradingDay(day=day) for day in days.all()]

    async def get_trading_result_count_for_period(
            self,
            filters: dict[str, Any],
            start_period_date: datetime.date,
            end_period_date: datetime.date,
    ) -> int:
        query = (
            select(func.count(TradingResultModel.id))
            .filter_by(**filters)
            .where(
                and_(
                    TradingResultModel.date >= start_period_date,
                    TradingResultModel.date <= end_period_date,
                )
            )
        )
        query_result = await self._session.execute(query)
        return query_result.scalar()

    async def get_trading_result_for_period(
            self,
            filters: dict[str, Any],
            start_period_date: datetime.date,
            end_period_date: datetime.date,
            limit: int,
            offset: int
    ) -> list[TradingResult]:
        query = (
            select(TradingResultModel)
            .filter_by(**filters)
            .where(
                and_(
                    TradingResultModel.date >= start_period_date,
                    TradingResultModel.date <= end_period_date,
                )
            )
            .order_by(TradingResultModel.date.desc())
            .limit(limit)
            .offset(offset)
        )
        model_list = await self._session.scalars(query)
        return [TradingResult.model_validate(model, from_attributes=True) for model in model_list.all()]

    async def get_trading_result_count(self, filters: dict[str, Any]) -> int:
        query = (
            select(func.count(TradingResultModel.id))
            .filter_by(**filters)
        )
        query_result = await self._session.execute(query)
        return query_result.scalar()

    async def get_trading_result(self, filters: dict[str, Any], limit: int, offset: int) -> list[TradingResult]:
        query = (
            select(TradingResultModel)
            .filter_by(**filters)
            .order_by(TradingResultModel.date.desc())
            .limit(limit)
            .offset(offset)
        )
        model_list = await self._session.scalars(query)
        return [TradingResult.model_validate(model, from_attributes=True) for model in model_list.all()]

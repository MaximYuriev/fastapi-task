import datetime
from abc import ABC, abstractmethod
from typing import Iterable, Any

from src.trading.schemas.responses import TradingResult


class TradingResultRepository(ABC):
    @abstractmethod
    async def get_trading_date_count(self) -> int:
        pass

    @abstractmethod
    async def get_last_trading_date(self, limit: int, offset: int) -> Iterable[datetime.date]:
        pass

    @abstractmethod
    async def get_trading_result_count_for_period(
            self,
            filters: dict[str, Any],
            start_period_date: datetime.date,
            end_period_date: datetime.date,
    ) -> int:
        pass

    @abstractmethod
    async def get_trading_result_for_period(
            self,
            filters: dict[str, Any],
            start_period_date: datetime.date,
            end_period_date: datetime.date,
            limit: int,
            offset: int,
    ) -> list[TradingResult]:
        pass

    @abstractmethod
    async def get_trading_result_count(
            self,
            filters: dict[str, Any],
    ) -> int:
        pass

    @abstractmethod
    async def get_trading_result(
            self,
            filters: dict[str, Any],
            limit: int,
            offset: int,
    ) -> list[TradingResult]:
        pass

import datetime
from abc import ABC, abstractmethod
from typing import Iterable


class TradingResultRepository(ABC):
    @abstractmethod
    async def get_trading_date_count(self) -> int:
        pass

    @abstractmethod
    async def get_last_trading_date(self, limit: int, offset: int) -> Iterable[datetime.date]:
        pass

from src.trading.interfaces import TradingResultRepository
from src.trading.schemas.queries import GetLastTradingDatesQuery
from src.trading.schemas.responses import TradingLastDaysResponse


class TradingResultService:
    def __init__(self, repository: TradingResultRepository):
        self._repository = repository

    async def get_last_trading_dates(self, query: GetLastTradingDatesQuery) -> TradingLastDaysResponse:
        total_date_count = await self._repository.get_trading_date_count()
        last_days = await self._repository.get_last_trading_date(
            limit=query.limit,
            offset=query.offset,
        )
        return TradingLastDaysResponse(
            total=total_date_count,
            limit=query.limit,
            offset=query.offset,
            days=last_days,
        )

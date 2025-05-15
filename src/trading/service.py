from src.trading.interfaces import TradingResultRepository
from src.trading.schemas.queries import GetLastTradingDatesQuery, GetDynamicsQuery, GetTradingResultQuery
from src.trading.schemas.responses import TradingLastDaysResponse, TradingResultResponse


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

    async def get_dynamics(self, query: GetDynamicsQuery) -> TradingResultResponse:
        query_filter = query.model_dump(exclude_none=True)
        total_trading_result_count = await self._repository.get_trading_result_count_for_period(
            filters=query_filter,
            start_period_date=query.start_date,
            end_period_date=query.end_date,
        )
        trading_result_list = await self._repository.get_trading_result_for_period(
            filters=query_filter,
            start_period_date=query.start_date,
            end_period_date=query.end_date,
            limit=query.limit,
            offset=query.offset,
        )
        return TradingResultResponse(
            total=total_trading_result_count,
            limit=query.limit,
            offset=query.offset,
            trading_results=trading_result_list,
        )

    async def get_trading_results(self, query: GetTradingResultQuery) -> TradingResultResponse:
        query_filter = query.model_dump(exclude_none=True)
        total_trading_result_count = await self._repository.get_trading_result_count(
            filters=query_filter,
        )
        trading_result_list = await self._repository.get_trading_result(
            filters=query_filter,
            limit=query.limit,
            offset=query.offset,
        )
        return TradingResultResponse(
            total=total_trading_result_count,
            limit=query.limit,
            offset=query.offset,
            trading_results=trading_result_list,
        )

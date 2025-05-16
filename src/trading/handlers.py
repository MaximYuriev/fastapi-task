from typing import Annotated

from fastapi import APIRouter, Query

from src.cache.decorator import cache
from src.ioc import container
from src.trading.schemas.queries import GetLastTradingDatesQuery, GetDynamicsQuery, GetTradingResultQuery
from src.trading.schemas.responses import TradingLastDaysResponse, TradingResultResponse
from src.trading.service import TradingResultService

router = APIRouter(prefix="/tradings", tags=["Tradings"])


@router.get("/dates/", summary="Список дат последних торговых дней.")
@cache
async def get_last_trading_dates_handler(
        query: Annotated[GetLastTradingDatesQuery, Query()],
) -> TradingLastDaysResponse:
    async with container() as di_container:
        service = await di_container.get(TradingResultService)
        return await service.get_last_trading_dates(query)


@router.get("/dynamics/", summary="Список торгов за заданный период.")
@cache
async def get_dynamics_handler(
        query: Annotated[GetDynamicsQuery, Query()],
) -> TradingResultResponse:
    async with container() as di_container:
        service = await di_container.get(TradingResultService)
        return await service.get_dynamics(query)


@router.get("/", summary="Список последних торгов.")
@cache
async def get_trading_results_handler(
        query: Annotated[GetTradingResultQuery, Query()],
) -> TradingResultResponse:
    async with container() as di_container:
        service = await di_container.get(TradingResultService)
        return await service.get_trading_results(query)

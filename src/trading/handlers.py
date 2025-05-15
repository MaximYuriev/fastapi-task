from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Query

from src.trading.schemas.queries import GetLastTradingDatesQuery, GetDynamicsQuery, GetTradingResultQuery
from src.trading.schemas.responses import TradingLastDaysResponse, TradingResultResponse
from src.trading.service import TradingResultService

router = APIRouter(prefix="/tradings", tags=["Tradings"])


@router.get("/dates/", summary="Список дат последних торговых дней.")
@inject
async def get_last_trading_dates_handler(
        query: Annotated[GetLastTradingDatesQuery, Query()],
        service: FromDishka[TradingResultService],
) -> TradingLastDaysResponse:
    return await service.get_last_trading_dates(query)


@router.get("/dynamics/", summary="Список торгов за заданный период.")
@inject
async def get_dynamics_handler(
        query: Annotated[GetDynamicsQuery, Query()],
        service: FromDishka[TradingResultService],
) -> TradingResultResponse:
    return await service.get_dynamics(query)


@router.get("/", summary="Список последних торгов.")
@inject
async def get_trading_results_handler(
        query: Annotated[GetTradingResultQuery, Query()],
        service: FromDishka[TradingResultService],
) -> TradingResultResponse:
    return await service.get_trading_results(query)

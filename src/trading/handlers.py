from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Query

from src.trading.schemas.queries import GetLastTradingDatesQuery
from src.trading.schemas.responses import TradingLastDaysResponse
from src.trading.service import TradingResultService

router = APIRouter(prefix="/tradings", tags=["Tradings"])


@router.get("/dates/", summary="Список дат последних торговых дней.")
@inject
async def get_last_trading_dates_handler(
        query: Annotated[GetLastTradingDatesQuery, Query()],
        service: FromDishka[TradingResultService],
) -> TradingLastDaysResponse:
    return await service.get_last_trading_dates(query)

import datetime
from typing import Iterable

from pydantic import BaseModel


class PaginationResponse(BaseModel):
    total: int
    limit: int
    offset: int


class TradingLastDaysResponse(PaginationResponse):
    days: Iterable[datetime.date]


class TradingResult(BaseModel):
    id: int
    exchange_product_id: str
    exchange_product_name: str
    oil_id: str
    delivery_basis_id: str
    delivery_basis_name: str
    delivery_type_id: str
    volume: int
    total: int
    count: int
    date: datetime.date


class TradingResultResponse(PaginationResponse):
    trading_results: list[TradingResult]

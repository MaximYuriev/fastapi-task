import datetime
from abc import ABC
from typing import Iterable

from pydantic import BaseModel


class BaseResponse(BaseModel, ABC):
    pass


class PaginationResponse(BaseResponse):
    total: int
    limit: int
    offset: int


class TradingDay(BaseResponse):
    day: datetime.date


class TradingLastDaysResponse(PaginationResponse):
    days: list[TradingDay]


class TradingResult(BaseResponse):
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

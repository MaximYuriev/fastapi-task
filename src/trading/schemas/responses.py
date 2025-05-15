import datetime
from typing import Iterable

from pydantic import BaseModel


class PaginationResponse(BaseModel):
    total: int
    limit: int
    offset: int


class TradingLastDaysResponse(PaginationResponse):
    days: Iterable[datetime.date]

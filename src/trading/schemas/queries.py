import datetime
from typing import Self

from pydantic import BaseModel, Field, model_validator


class PaginationQuery(BaseModel):
    limit: int = Field(default=20, ge=1, exclude=True)
    offset: int = Field(default=0, ge=0, exclude=True)


class GetLastTradingDatesQuery(PaginationQuery):
    pass


class GetDynamicsQuery(PaginationQuery):
    oil_id: str | None = None
    delivery_type_id: str | None = None
    delivery_basis_id: str | None = None
    start_date: datetime.date = Field(exclude=True)
    end_date: datetime.date = Field(exclude=True)

    @model_validator(mode="after")
    def validate_dates(self) -> Self:
        if self.end_date < self.start_date:
            raise ValueError("end_date must be grater or equal then start_date")
        return self

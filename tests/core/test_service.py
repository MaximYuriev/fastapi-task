import datetime

import pytest

from src.trading.schemas.queries import GetLastTradingDatesQuery, GetDynamicsQuery, GetTradingResultQuery
from src.trading.service import TradingResultService

type StartPeriodDate = datetime.date
type EndPeriodDate = datetime.date


@pytest.mark.parametrize(
    "query, total, length", [
        (GetLastTradingDatesQuery(), 3, 3),
        (GetLastTradingDatesQuery(offset=2), 3, 1),
    ]
)
async def test_get_last_trading_dates(
        trading_service: TradingResultService,
        query: GetLastTradingDatesQuery,
        total: int,
        length: int,
):
    last_trading_dates = await trading_service.get_last_trading_dates(query)

    assert last_trading_dates.total == total
    assert last_trading_dates.offset == query.offset
    assert len(last_trading_dates.days) == length


@pytest.mark.parametrize(
    "offset, total, length, oil_id", [
        (0, 3, 3, None),
        (2, 3, 1, None),
        (0, 1, 1, "A10K"),
    ]
)
async def test_get_dynamics(
        trading_service: TradingResultService,
        period: tuple[StartPeriodDate, EndPeriodDate],
        offset: int,
        total: int,
        length: int,
        oil_id: str | None,
):
    start, end = period
    query = GetDynamicsQuery(
        oil_id=oil_id,
        offset=offset,
        start_date=start,
        end_date=end,
    )
    trading_result_for_period = await trading_service.get_dynamics(query)

    assert trading_result_for_period.total == total
    assert trading_result_for_period.offset == offset
    assert len(trading_result_for_period.trading_results) == length


async def test_get_dynamics_w_validation_error(
        trading_service: TradingResultService,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    with pytest.raises(ValueError):
        query = GetDynamicsQuery(
            start_date=end,
            end_date=start,
        )
        await trading_service.get_dynamics(query)


@pytest.mark.parametrize(
    "query, total, length", [
        (GetTradingResultQuery(), 3, 3),
        (GetTradingResultQuery(offset=2), 3, 1),
        (GetTradingResultQuery(oil_id="A10K"), 1, 1),
    ]
)
async def test_get_trading_results(
        trading_service: TradingResultService,
        query: GetTradingResultQuery,
        total: int,
        length: int,
):
    trading_result_response = await trading_service.get_trading_results(query)

    assert trading_result_response.total == total
    assert trading_result_response.offset == query.offset
    assert len(trading_result_response.trading_results) == length

import datetime

import pytest

from src.trading.interfaces import TradingResultRepository

type StartPeriodDate = datetime.date
type EndPeriodDate = datetime.date


async def test_get_trading_date_count(trading_repository: TradingResultRepository):
    count = await trading_repository.get_trading_date_count()
    assert count == 3


@pytest.mark.parametrize(
    "limit, offset, length", [
        (20, 0, 3),
        (20, 2, 1),
    ]
)
async def test_get_last_trading_date(
        trading_repository: TradingResultRepository,
        limit: int,
        offset: int,
        length: int,
):
    trading_date_list = await trading_repository.get_last_trading_date(limit=limit, offset=offset)
    assert len(trading_date_list) == length


@pytest.mark.parametrize(
    "filters, count", [
        ({}, 3),
        ({"oil_id": "A10K"}, 1),
    ]
)
async def test_get_trading_result_count_for_period(
        trading_repository: TradingResultRepository,
        period: tuple[StartPeriodDate, EndPeriodDate],
        filters: dict[str, str],
        count: int,
):
    start, end = period
    trading_result_count = await trading_repository.get_trading_result_count_for_period(
        filters=filters,
        start_period_date=start,
        end_period_date=end
    )
    assert trading_result_count == count


@pytest.mark.parametrize(
    "filters, limit, offset, length", [
        ({}, 20, 0, 3),
        ({}, 20, 2, 1),
        ({"oil_id": "A10K"}, 20, 0, 1),
    ]
)
async def test_get_trading_result_for_period(
        trading_repository: TradingResultRepository,
        period: tuple[StartPeriodDate, EndPeriodDate],
        filters: dict[str, str],
        limit: int,
        offset: int,
        length: int
):
    start, end = period
    trading_result_list = await trading_repository.get_trading_result_for_period(
        filters=filters,
        start_period_date=start,
        end_period_date=end,
        limit=limit,
        offset=offset,
    )
    assert len(trading_result_list) == length


@pytest.mark.parametrize(
    "filters, count", [
        ({}, 3),
        ({"oil_id": "A10K"}, 1),
    ]
)
async def test_get_trading_result_count(
        trading_repository: TradingResultRepository,
        filters: dict[str, str],
        count: int,
):
    trading_result_count = await trading_repository.get_trading_result_count(filters=filters)
    assert trading_result_count == count


@pytest.mark.parametrize(
    "filters, limit, offset, length", [
        ({}, 20, 0, 3),
        ({}, 20, 2, 1),
        ({"oil_id": "A10K"}, 20, 0, 1),
    ]
)
async def test_get_trading_result(
        trading_repository: TradingResultRepository,
        filters: dict[str, str],
        limit: int,
        offset: int,
        length: int,
):
    trading_result_list = await trading_repository.get_trading_result(
        filters=filters,
        limit=limit,
        offset=offset,
    )
    assert len(trading_result_list) == length

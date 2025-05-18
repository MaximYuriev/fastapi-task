import datetime

import pytest

from src.trading.schemas.queries import GetLastTradingDatesQuery, GetDynamicsQuery, GetTradingResultQuery
from src.trading.service import TradingResultService

type StartPeriodDate = datetime.date
type EndPeriodDate = datetime.date


async def test_get_last_trading_dates(trading_service: TradingResultService):
    last_trading_dates = await trading_service.get_last_trading_dates(
        query=GetLastTradingDatesQuery(),
    )

    assert last_trading_dates.total == 3
    assert len(last_trading_dates.days) == 3


async def test_get_last_trading_dates_w_pagination(trading_service: TradingResultService):
    query = GetLastTradingDatesQuery(
        offset=2,
    )

    last_trading_dates = await trading_service.get_last_trading_dates(query=query)

    assert last_trading_dates.total == 3
    assert last_trading_dates.offset == 2
    assert len(last_trading_dates.days) == 1


async def test_get_dynamics(
        trading_service: TradingResultService,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    query = GetDynamicsQuery(
        start_date=start,
        end_date=end,
    )
    trading_result_for_period = await trading_service.get_dynamics(query)

    assert trading_result_for_period.total == 3
    assert len(trading_result_for_period.trading_results) == 3


async def test_get_dynamics_w_pagination(
        trading_service: TradingResultService,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    query = GetDynamicsQuery(
        offset=2,
        start_date=start,
        end_date=end,
    )
    trading_result_for_period = await trading_service.get_dynamics(query)

    assert trading_result_for_period.total == 3
    assert trading_result_for_period.offset == 2
    assert len(trading_result_for_period.trading_results) == 1


async def test_get_dynamics_w_filters(
        trading_service: TradingResultService,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    query = GetDynamicsQuery(
        oil_id="A10K",
        start_date=start,
        end_date=end,
    )
    trading_result_for_period = await trading_service.get_dynamics(query)

    assert trading_result_for_period.total == 1
    assert len(trading_result_for_period.trading_results) == 1


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


async def test_get_trading_results(trading_service: TradingResultService):
    trading_result_response = await trading_service.get_trading_results(GetTradingResultQuery())

    assert trading_result_response.total == 3
    assert len(trading_result_response.trading_results) == 3


async def test_get_trading_results_w_pagination(trading_service: TradingResultService):
    query = GetTradingResultQuery(
        offset=2,
    )

    trading_result_response = await trading_service.get_trading_results(query)

    assert trading_result_response.total == 3
    assert trading_result_response.offset == 2
    assert len(trading_result_response.trading_results) == 1


async def test_get_trading_result_w_filters(trading_service: TradingResultService):
    query = GetTradingResultQuery(
        oil_id="A10K",
    )

    trading_result_response = await trading_service.get_trading_results(query)

    assert trading_result_response.total == 1
    assert len(trading_result_response.trading_results) == 1

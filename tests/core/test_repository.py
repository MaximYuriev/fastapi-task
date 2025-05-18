import datetime

from src.trading.interfaces import TradingResultRepository

type StartPeriodDate = datetime.date
type EndPeriodDate = datetime.date


async def test_get_trading_date_count(trading_repository: TradingResultRepository):
    count = await trading_repository.get_trading_date_count()
    assert count == 3


async def test_get_last_trading_date(trading_repository: TradingResultRepository):
    trading_date_list = await trading_repository.get_last_trading_date(limit=20, offset=0)
    assert len(trading_date_list) == 3


async def test_get_last_trading_date_w_pagination(trading_repository: TradingResultRepository):
    trading_date_list = await trading_repository.get_last_trading_date(limit=20, offset=2)
    assert len(trading_date_list) == 1


async def get_trading_result_count_for_period(
        trading_repository: TradingResultRepository,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    trading_result_count = await trading_repository.get_trading_result_count_for_period(
        filters={},
        start_period_date=start,
        end_period_date=end
    )
    assert trading_result_count == 3


async def test_get_trading_result_count_for_period_w_filters(
        trading_repository: TradingResultRepository,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    trading_result_count = await trading_repository.get_trading_result_count_for_period(
        filters={"oil_id": "A10K"},
        start_period_date=start,
        end_period_date=end
    )
    assert trading_result_count == 1


async def test_get_trading_result_for_period(
        trading_repository: TradingResultRepository,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    trading_result_list = await trading_repository.get_trading_result_for_period(
        filters={},
        start_period_date=start,
        end_period_date=end,
        limit=20,
        offset=0,
    )
    assert len(trading_result_list) == 3


async def test_get_trading_result_for_period_w_pagination(
        trading_repository: TradingResultRepository,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    trading_result_list = await trading_repository.get_trading_result_for_period(
        filters={},
        start_period_date=start,
        end_period_date=end,
        limit=20,
        offset=2,
    )
    assert len(trading_result_list) == 1


async def test_get_trading_result_for_period_w_filters(
        trading_repository: TradingResultRepository,
        period: tuple[StartPeriodDate, EndPeriodDate],
):
    start, end = period
    trading_result_list = await trading_repository.get_trading_result_for_period(
        filters={"oil_id": "A10K"},
        start_period_date=start,
        end_period_date=end,
        limit=20,
        offset=0,
    )
    assert len(trading_result_list) == 1


async def test_get_trading_result_count(trading_repository: TradingResultRepository):
    trading_result_count = await trading_repository.get_trading_result_count(filters={})
    assert trading_result_count == 3


async def test_get_trading_result_count_w_filters(trading_repository: TradingResultRepository):
    trading_result_count = await trading_repository.get_trading_result_count(filters={"oil_id": "A10K"})
    assert trading_result_count == 1


async def test_get_trading_result(trading_repository: TradingResultRepository):
    trading_result_list = await trading_repository.get_trading_result(
        filters={},
        limit=20,
        offset=0,
    )
    assert len(trading_result_list) == 3


async def test_get_trading_result_w_filters(trading_repository: TradingResultRepository):
    trading_result_list = await trading_repository.get_trading_result(
        filters={"oil_id": "A10K"},
        limit=20,
        offset=0,
    )
    assert len(trading_result_list) == 1


async def test_get_trading_result_w_pagination(trading_repository: TradingResultRepository):
    trading_result_list = await trading_repository.get_trading_result(
        filters={},
        limit=20,
        offset=2,
    )
    assert len(trading_result_list) == 1

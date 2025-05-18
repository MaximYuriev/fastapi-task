import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "params, status_code, length", [
        ({}, 200, 3),
        ({"limit": 2, "offset": 1}, 200, 2),
        ({"limit": -10}, 422, None),
    ]
)
async def test_get_trading_dates(
        api_client: AsyncClient,
        params: dict[str, int],
        status_code: int,
        length: int,
):
    response = await api_client.get("tradings/dates/", params=params)
    assert response.status_code == status_code

    if status_code == 200:
        body = response.json()
        assert len(body["days"]) == length


@pytest.mark.parametrize(
    "params, status_code, length", [
        ({}, 200, 3),
        ({"oil_id": "A100"}, 200, 1),
    ]
)
async def test_get_trading_result(
        api_client: AsyncClient,
        params: dict[str, str],
        status_code: int,
        length: int
):
    response = await api_client.get("tradings/", params=params)
    body = response.json()
    assert response.status_code == status_code
    assert len(body["trading_results"]) == length


@pytest.mark.parametrize(
    "params, status_code, length", [
        ({"start_date": "2024-08-07", "end_date": "2024-08-10"}, 200, 3),
        ({"start_date": "2024-08-07", "end_date": "2024-08-08"}, 200, 2),
        ({}, 422, None),
    ]
)
async def test_get_trading_dynamics_success(
        api_client: AsyncClient,
        params: dict[str, str],
        status_code: int,
        length: int | None,
):
    response = await api_client.get("tradings/dynamics/", params=params)
    assert response.status_code == status_code

    if status_code == 200:
        body = response.json()
        assert len(body["trading_results"]) == length



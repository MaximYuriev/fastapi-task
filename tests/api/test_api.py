from httpx import AsyncClient


async def test_get_trading_dates_success(api_client: AsyncClient):
    response = await api_client.get("tradings/dates/")
    body = response.json()
    assert response.status_code == 200
    assert len(body["days"]) == 3


async def test_get_trading_dates_w_limit_and_offset(api_client: AsyncClient):
    response = await api_client.get("tradings/dates/", params={"limit": 2, "offset": 1})
    body = response.json()
    assert response.status_code == 200
    assert len(body["days"]) == 2


async def test_get_trading_dates_w_validation_error(api_client: AsyncClient):
    response = await api_client.get("tradings/dates/", params={"limit": -10})
    assert response.status_code == 422


async def test_get_trading_result_success(api_client: AsyncClient):
    response = await api_client.get("tradings/")
    body = response.json()
    assert response.status_code == 200
    assert len(body["trading_results"]) == 3


async def test_get_trading_result_w_filter(api_client: AsyncClient):
    response = await api_client.get("tradings/", params={"oil_id": "A100"})
    body = response.json()
    assert response.status_code == 200
    assert len(body["trading_results"]) == 1


async def test_get_trading_dynamics_success(api_client: AsyncClient):
    response = await api_client.get(
        "tradings/dynamics/",
        params={
            "start_date": "2024-08-07",
            "end_date": "2024-08-10",
        }
    )
    body = response.json()
    assert response.status_code == 200
    assert len(body["trading_results"]) == 3


async def test_get_trading_dynamics_w_data_filter(api_client: AsyncClient):
    response = await api_client.get(
        "tradings/dynamics/",
        params={
            "start_date": "2024-08-07",
            "end_date": "2024-08-08",
        }
    )
    body = response.json()
    assert response.status_code == 200
    assert len(body["trading_results"]) == 2


async def test_get_trading_dynamics_w_validation_error(api_client: AsyncClient):
    response = await api_client.get("tradings/dynamics/")
    assert response.status_code == 422

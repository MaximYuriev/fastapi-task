from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport

from src.main import create_app

@pytest.fixture
async def api_client() -> AsyncGenerator[AsyncClient, None]:
    app = create_app()
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as async_client:
        yield async_client

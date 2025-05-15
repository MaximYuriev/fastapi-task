from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.ioc import container
from src.trading.handlers import router as trading_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="TradingResultAPI",
        debug=True,
    )
    app.include_router(trading_router)

    setup_dishka(container, app)

    return app

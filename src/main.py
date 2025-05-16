from fastapi import FastAPI

from src.trading.handlers import router as trading_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="TradingResultAPI",
        debug=True,
    )
    app.include_router(trading_router)

    return app

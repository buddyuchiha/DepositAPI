from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from api.endpoints.users import users_router
from api.endpoints.deposits import deposits_router
from api.endpoints.utils import utils_router
from core.config import settings 
from core.logging import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("DepositAPI turned on")
    yield 
    logger.info("DepositAPI turned down")


deposit_app = FastAPI(lifespan=lifespan)

deposit_app.include_router(users_router)
deposit_app.include_router(deposits_router)
deposit_app.include_router(utils_router)

@deposit_app.get("/")
def root():
    return {"msg" : "Welcome to DepositAPI"}

if __name__ == "__main__":
    uvicorn.run(
        "main:deposit_app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
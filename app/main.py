from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from core.config import settings 
from core.logging import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("DepositAPI turned on")
    yield 
    logger.info("DepositAPI turned down")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"msg" : "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
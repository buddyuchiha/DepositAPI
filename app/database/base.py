from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, registry

from app.core.config import settings


engine = create_async_engine(settings.DB_URL)
session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
        }
    )
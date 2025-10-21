from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db
from repositories.deposit_repository import DepositsRepository
from repositories.user_repository import UserRepository


async def get_user_repository(
    session: AsyncSession = Depends(get_db)
    ) -> AsyncSession:
    return UserRepository(session)


async def get_deposits_repository(
    session: AsyncSession = Depends(get_db)
    ) -> AsyncSession:
    return DepositsRepository(session)
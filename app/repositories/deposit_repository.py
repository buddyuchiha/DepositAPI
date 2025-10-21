from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from models.models import DepositsORM
from repositories.base_repository import BaseRepository
from schemas.deposits import DefaultDepositScheme


class DepositsRepository(BaseRepository):
    def __init__(self, session) -> None:
        self.session = session
        
    async def get(self) -> list[DepositsORM]:
        async with self.session as session:
            query = select(DepositsORM)
            result = await session.execute(query)
            
            return result.scalars().all()
        
    async def get_single(self, deposit_id: int) -> DepositsORM | None:
        async with self.session as session:
            query = (select(
                DepositsORM
                )
                .where(DepositsORM.id == deposit_id)    
            )
            
            result = await session.execute(query)
            
            return result.scalars().all()
        
    async def create(self, data: DefaultDepositScheme) -> DepositsORM:
        async with self.session as session:
            deposit = DepositsORM(**data.model_dump())
            session.add(deposit)
            
            await session.commit()
            await session.refresh(deposit)
            
            return deposit
        
    async def update(self, deposit_id: int, data: DefaultDepositScheme) -> bool:
        async with self.session as session:
            query = (update(
                DepositsORM
                )
                .where(DepositsORM.id == deposit_id)
                .values(
                    date = data.date,
                    periods = data.periods,
                    amount = data.amount, 
                    rate = data.amount
                )
            )
            
            await session.execute(query)
            await session.commit()
            
            return True
            
    async def delete(self, deposit_id: int) -> bool:
        async with self.session as session: 
            query = (delete(   
                DepositsORM             
                )
                .where(DepositsORM.id == deposit_id)
            )
            
            await session.execute(query)
            await session.commit()
            
            return True 
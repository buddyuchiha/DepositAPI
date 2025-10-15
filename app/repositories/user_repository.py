from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import UsersORM 
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session: Session) -> None:
        self.session = session
        
    async def get(self) -> list[UsersORM]:
        async with self.session() as session:
            query = select(UsersORM)
            result = await session.execute(query)
            return result.scalars().all()
    
    def get_single(self, **kwargs):
        return super().get_single(**kwargs)
    
    async def create(self, data) -> dict:
        async with self.session() as session:
            user = UsersORM(data)
            await session.add(user)
            await session.commit()
            await session.refresh(user)
            return {"msg" : "all okay"}
        
    def update(self, **kwargs):
        return super().update(**kwargs)
    
    def delete(self, **kwargs):
        return super().delete(**kwargs) 
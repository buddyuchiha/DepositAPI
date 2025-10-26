from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from models.models import UsersORM 
from repositories.base_repository import BaseRepository
from schemas.users import DefaultUserScheme


class UserRepository(BaseRepository):
    def __init__(self, session: Session) -> None:
        self.session = session
        
    async def get(self) -> list[UsersORM]:
        async with self.session as session:
            query = select(UsersORM)
            result = await session.execute(query)
            
            return result.scalars().all()
    
    async def get_single(self, user_id: int) -> UsersORM | None:
        async with self.session as session: 
            query = (select(
                UsersORM
                ).
                where(UsersORM.id == user_id)
            )
            
            result = await session.execute(query)
            
            return result.scalars().all()
    
    async def create(self, data: DefaultUserScheme) -> UsersORM:
        async with self.session as session:
            user = UsersORM(**data.model_dump())
            session.add(user)
            
            await session.commit()
            await session.refresh(user)
            
            return user
        
    async def update(self, user_id: int, data: DefaultUserScheme) -> bool:
        async with self.session as session:
            query = (update(
                UsersORM
                )
                .where(UsersORM.id == user_id)
                .values(
                    name = data.name, 
                    email = data.email
                )
            )
            
            await session.execute(query)
            await session.commit()
            
            return True 
                
    async def delete(self, user_id: int) -> bool:
        async with self.session as session:
            query = (delete(
                UsersORM
                )
                .where(UsersORM.id == user_id)   
            )
            
            await session.execute(query)
            await session.commit()
            
            return True
        
    async def clean(self) -> bool:
        async with self.session as session: 
            query = (delete(   
                UsersORM            
                )
                .where(UsersORM.id > 0)
            )
            
            await session.execute(query)
            await session.commit()
            
            return True 
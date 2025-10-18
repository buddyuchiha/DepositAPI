from fastapi import Depends
from sqlalchemy.orm import Session

from database.session import get_db
from repositories.user_repository import UserRepository


def get_user_repository(session: Session = Depends(get_db)) -> Session:
    return UserRepository(session)
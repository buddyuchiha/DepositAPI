import datetime
from decimal import Decimal
from sqlalchemy import ForeignKey, text, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

from app.database.base import Base


created_at = Annotated[datetime.datetime, 
                       mapped_column(
                           server_default=text("TIMEZONE('utc', now())")
                           )]


class UsersORM(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[created_at]
    

class DepositsORM(Base):
    __tablename__ = "deposits"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"))
    date: Mapped[datetime.date]
    periods: Mapped[int]
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    rate: Mapped[float]
    created_at: Mapped[created_at]
    
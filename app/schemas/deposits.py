from datetime import date

from pydantic import BaseModel, RootModel, Field


class DefaultDepositScheme(BaseModel):
    user_id: int 
    date: date 
    periods: int 
    amount: float 
    rate: float 
    

class InputCalculateDepositScheme(BaseModel):
    date: str 
    periods: int = Field(ge=1, le=60)
    amount: int = Field(ge=10000, le=3000000)
    rate: float = Field(ge=1, le=8)
    
    
class OutputCalculateDepositScheme(RootModel):
    root: dict[str, float]
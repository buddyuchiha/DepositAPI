from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DefaultUserScheme(BaseModel):
    name: str
    email: str 
    
    
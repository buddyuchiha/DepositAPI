from pydantic import BaseModel


class DefaultUserScheme(BaseModel):
    name: str
    email: str 
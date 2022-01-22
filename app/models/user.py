from sqlmodel import SQLModel
from sqlmodel import Field
from datetime import datetime

class User(SQLModel):
    id: int = Field(primary_key = True)
    access: str = Field(default = "User")
    email: str

class Log(SQLModel):
    id: int = Field(primary_key = True)
    timestamp: datetime
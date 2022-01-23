from sqlmodel import SQLModel
from sqlmodel import Field
from datetime import datetime


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    access: str = Field(default="User")
    email: str


class Log(SQLModel, table=True):
    id: int = Field(primary_key=True)
    timestamp: datetime
    level: str
    request: str

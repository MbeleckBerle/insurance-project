from typing import Annotated
from sqlmodel import Field,  SQLModel
from pydantic import EmailStr
from datetime import datetime


class UserBase(SQLModel):
    # id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    email: EmailStr | None = Field(...)


class User(UserBase, table=True):
    __tablename__ = "Users"

    id: int | None = Field(default=None, primary_key=True)
    role: str | None
    password_hash: str

    # is_active: bool | None = Field(default=True) - for provider and clinic table

    created_at: datetime | None = Field(default=datetime.now())
    updated_at: datetime | None = Field(default=datetime.now())

    # age: int | None = Field(default=None, index=True)

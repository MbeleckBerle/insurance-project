from sqlmodel import Field,  SQLModel
from pydantic import EmailStr
from datetime import datetime
from ..models import users


class UserBase(SQLModel):
    # id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)


class UserCreate(UserBase):
    email: EmailStr | None = Field(...)
    password_hash: str


class UserUpdate(UserBase):
    email: EmailStr | None = Field(...)
    password_hash: str
    role: str | None
    updated_at: datetime = Field(default=datetime.now())


class UserPublic(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

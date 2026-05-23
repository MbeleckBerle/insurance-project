from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field,  SQLModel
from pydantic import EmailStr
from datetime import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr | None = Field(...)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    password_hash: str
    created_at: datetime
    # hash password
    # is_active: 
    

    # age: int | None = Field(default=None, index=True)
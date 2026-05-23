from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..db import db_connect

from ..models import users
from ..db import db_connect


router = APIRouter(prefix='/users',
                   tags=['users'],
                   responses={404: {"description": "Not found"}})


@router.post("/")
def create_user(user: users.User , session: db_connect.SessionDep) -> users.User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
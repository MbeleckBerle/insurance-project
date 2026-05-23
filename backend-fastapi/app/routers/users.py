from fastapi import APIRouter, Form
from typing import Annotated


from ..models import users
from ..db import db_connect


router = APIRouter(prefix='/users',
                   tags=['users'],
                   responses={404: {"description": "Not found"}})


@router.post("/")
def create_user(data: Annotated[users.User, Form()], session: db_connect.SessionDep) -> users.User:
    session.add(data)
    session.commit()
    session.refresh(data)
    return data
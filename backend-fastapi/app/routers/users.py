from fastapi import APIRouter, Query

from ..schemas.users import UserCreate
from ..db.db_connect import SessionDep
from ..crud.users import create_user as create, get_users
from ..schemas.users import UserPublic


router = APIRouter(prefix='/users',
                   tags=['users'],
                   responses={404: {"description": "Not found"}})


# create user
@router.post("/", response_model=UserPublic)
async def create_user(request: UserCreate, session: SessionDep):
    return create(request, session)


# get all users
@router.get('/users', response_model=list[UserPublic])
async def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    return get_users(session, offset, limit)


# Get user by ID
@router.get("/{user_id}")
async def get_user_by_id():
    pass


# Delete user


# use for for authentication

# from fastapi import APIRouter, Form
# from typing import Annotated

# @router.post("/")
# def create_user(data: Annotated[users.User, Form()], session: db_connect.SessionDep) -> users.User:
#     session.add(data)
#     session.commit()
#     session.refresh(data)
#     return data

from fastapi import APIRouter, Query

from ..schemas.users import UserCreate
from ..db.db_connect import SessionDep
from ..crud.users import create_user as create, get_users, user_delete, user_update
from ..schemas.users import UserPublic, UserUpdate


router = APIRouter(prefix='/users',
                   tags=['users'],
                   responses={404: {"description": "Not found"}})


"""
FastAPI router for User endpoints.
Defines API routes for CRUD operations on users.
"""


# Create users
@router.post("/", response_model=UserPublic, description="Create user endpoint")
async def create_user(request: UserCreate, session: SessionDep):
    return create(request, session)


# get all users
@router.get('/', response_model=list[UserPublic], description="Get all users")
async def get_all_users(
    session: SessionDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):

    return get_users(session, offset, limit)


# Delete user by user id
@router.delete("/{user_id}", description="Delete User")
async def delete_single_user(user_id: int, session: SessionDep):
    return user_delete(user_id, session)


# update user
@router.patch("/{user_id}", response_model=UserPublic, description="Update User")
def update_user(user_id: int, user: UserUpdate, session: SessionDep):
    return user_update(user_id, user, session)


# Get user by ID
@router.get("/{user_id}")
async def get_user_by_id():
    pass

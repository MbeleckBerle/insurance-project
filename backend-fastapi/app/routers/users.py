from fastapi import APIRouter, Query

from ..schemas.users import UserCreate
from ..db.db_connect import SessionDep
from ..crud.users import create_user as create, get_users
from ..schemas.users import UserPublic


router = APIRouter(prefix='/users',
                   tags=['users'],
                   responses={404: {"description": "Not found"}})


"""
FastAPI router for User endpoints.
Defines API routes for CRUD operations on users.
"""

# get all users


@router.get('/', response_model=list[UserPublic], description="Get all users")
async def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):

    return get_users(session, offset, limit)


# Create users
@router.post("/", response_model=UserPublic, description="Create user endpoint")
async def create_user(request: UserCreate, session: SessionDep):
    return create(request, session)


# Get user by ID
@router.get("/{user_id}")
async def get_user_by_id():
    pass


# Delete user

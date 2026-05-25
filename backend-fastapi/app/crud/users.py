from sqlmodel import Session, select
from fastapi import HTTPException

from ..schemas.users import UserCreate
from ..models.users import User


# Create user
def create_user(data: UserCreate, session: Session):

    user = User(**data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# Get all users
def get_users(
    session: Session,
    offset: int = 0,
    limit: int = 100
):
    users = session.exec(
        select(User).offset(offset).limit(limit)
    ).all()

    return users


# Get user by ID
def get_user_by_id(user_id: int, session: Session):
    pass


# Delete a user
def delete_user(user_id: int, session: Session):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True,
            "message": f"user_id {user_id} deleted"}

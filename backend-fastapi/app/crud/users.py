from ..schemas.users import UserCreate
from sqlmodel import Session, select
from ..models.users import User


# Create user
def create_user(data: UserCreate, session: Session):
    user = User(**data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


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
def get_user_by_id():
    pass


# Delete a user
def delete_user():
    pass

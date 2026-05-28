from sqlmodel import Session, select
from fastapi import HTTPException


# Create provider
def create_provider():
    pass


# Get all providers
def get_providers(
    session: Session,
    offset: int = 0,
    limit: int = 100
):
    pass


# Get provider by ID
def get_provider_by_id(provider_id: int, session: Session):
    pass


# Delete a provider
def delete_provider(provider_id: int, session: Session):
    pass

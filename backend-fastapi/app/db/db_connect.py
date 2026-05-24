import os
from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends



load_dotenv()

DB_PASSWORD = os.getenv("SUPABASE_PASSWORD")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# SUPABASE_URL=f"postgresql://postgres:{DB_PASSWORD}@db.{SUPABASE_KEY}.supabase.co:5432/postgres"
SUPABASE_URL=f"postgresql://postgres.{SUPABASE_KEY}:{DB_PASSWORD}@aws-1-us-west-2.pooler.supabase.com:6543/postgres"

engine = create_engine(SUPABASE_URL)


def create_db_and_tables():
    if not SQLModel.metadata.create_all(engine):
        SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

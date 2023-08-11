from sqlalchemy import Column, Integer, String, DateTime, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import uvicorn

from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
    company = Column(String)
    location = Column(String)

class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    phone = Column(String)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    linkedin = Column(String, index=True)
    age = Column(Integer)
    country = Column(String)
    formal_education = Column(String)
    skills = Column(String)
    work_experience = Column(String)
    role = Column(String)
    english_level = Column(String)
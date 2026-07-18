from sqlalchemy import Column, Integer, String, JSON, Boolean, DateTime
from sqlalchemy.sql import func
from db import Base

class Household(Base):
    __tablename__ = "households"

    #fields
    id = Column(Integer, primary_key=True, index=True)
    userkey = Column(String, nullable=False)
    household_name = Column(String, nullable=False)
    email = Column(String)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    settings = Column(JSON, default=lambda: {})
    members = Column(JSON, nullable=False, default=dict)
    encrypted = Column(Boolean, nullable=False)

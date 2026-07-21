from sqlalchemy import Column, Integer, String, JSON

from db import Base

class Category(Base):
    __tablename__ = "categories"

    #fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    style = Column(JSON)
    icon = Column(String)
    description = Column(String)
    metadata_keys = Column(JSON, default=list)
    
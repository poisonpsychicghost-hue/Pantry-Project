from sqlalchemy import Column, Integer, String
from db import Base

class InventoryLocation(Base):
    __tablename__ = "inventory_locations"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class InventoryLocation(Base):
    __tablename__ = "inventory_locations"
    
    #fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    emoji = Column(String, nullable=False)
    description = Column(String, nullable=False)

    ALLOWED_UPDATED_FIELDS = [
        "name", "type", "emoji", "description"
    ]

    #relationships
    category = relationship("Category")
    fooditem = relationship("FoodItem")


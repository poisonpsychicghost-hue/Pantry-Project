from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class ShoppingItem(Base):
    __tablename__ = "shopping_items"

    #fields

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    fooditem_id = Column(Integer, ForeignKey("food_items.id"))
    requested_by = Column(String)
    date_added = Column(Date, nullable=False)
    date_needed = Column(Date)
    completed_at = Column(Date)
    notes = Column(String)

    ALLOWED_UPDATED_FIELDS = [
        "name", "requested_by", "date_needed", "notes"
    ]
    REQUIRED_CREATE_FIELDS = [
        "name", "date_added"
    ]

    #relationships
    fooditem = relationship("FoodItem")
    
"""
Shopping Item Entity Model - Defines Shopping List Item Entities
Structures Shopping Items and Their Attributes
Example Items: Milk, Cabbage, Bacon
Mutable - Use Can Edit Whitelist Fields
"""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class ShoppingItem(Base):
    """
    Shopping Item Class:
        Attributes:
            id: Unique Numeric Identifier For Indexing 
            name: Display Name
            fooditem_id: Link To Food Item In Pantry
            requested_by: Optional Display Detail
            date_added: Date Added to List
            date_needed: Optional Date Needed to Purchase By
            completed_at: Date Marked Off List
            notes: Optional Additional User Notes
        Required:
            ["name", "date_added"]
        Whitelist:
            ["name", "requested_by", "date_needed", "notes"]
    """
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
    
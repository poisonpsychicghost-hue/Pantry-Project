from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from db import Base


class FoodItem(Base):
    __tablename__ = "food_items"

    #Fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("inventory_locations.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    expiration_date = Column(Date, nullable=False)
    status = Column(String, nullable=False, default='in_stock')
    notes = Column(String)
    item_metadata = Column(JSON, nullable=False, default=dict)
    added_on = Column(Date)
    purchased_at = Column(Date)

    ALLOWED_UPDATE_FIELDS = [
        "location_id", "quantity", "unit", "status", "notes", "item_metadata"
    ]

    #Relationships
    category = relationship("Category")
    location = relationship("InventoryLocation")
    
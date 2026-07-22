"""
Food Item Entity Model - Defines Pantry Inventory Item Entities
Structures Food Items and their Attributes
Example Items: Milk, Cabbage, Bacon
Mutable - User Can Edit Whitelist Fields
"""

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from db import Base


class FoodItem(Base):
    """
    FoodItem Class:
    Attributes:
        id: Unique Numeric Indetifier For Indexing
        name: Display Name (Also Used In Search)
        category_id: Numeric Link To Category for Metadata Allowances
        location_id: Numeric Link To Location for Display + Search
        quantity: Numeric Value - Float Allowed For Partials
        unit: Quantity Unit Identifier
        expiration_date: Date Expires (Calculated Internally)
        status: Item Condition Tag (Expired, New, Warning, Etc)
        notes: User Written Notes For Non-Field Data
        item_metadata: Category Specific Fields
        added_on: Date Added To Inventory
        purchased_on: Date Most Recently Purchased
    Required:
        Minimum Needed Fields For Item Creation
        ["name", "category_id", "location_id", "quantity", "unit", "expiration_date"]
    Whitelist:
        Allowed User-Editable Fields
        ["location_id", "quantity", "unit", "status", "notes", "item_metadata"]
    """
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

    REQUIRED_CREATE_FIELDS = [
        "name", "category_id", "location_id", "quantity", "unit", "expiration_date"
    ]

    #Relationships
    category = relationship("Category")
    location = relationship("InventoryLocation")

    from models.category import Category
    from models.inventorylocation import InventoryLocation
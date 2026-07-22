"""
Location Entity Model - Defines Inventory Locations
Structures Inventory Locations And Their Attributes
Example Locations: Refrigerator, Pantry, Freezer
Mutable - User Can Edit Whitelist Fields
"""
from sqlalchemy import Column, Integer, String
from db import Base

class InventoryLocation(Base):
    """
    Inventory Location Class:
        Attributes:
            id: Unique Numeric Identifier For Indexing
            name: Display Name
            type: Cateogoric Attribute For Filtering
            emoji: Display Image
            description: Short Description Of Location
        Required:
            ["name", "type", "emoji"]
        Whitelist:
            ["name", "type", "emoji", "description"]
    """
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
    REQUIRED_CREATE_FIELDS = [
        "name", "type", "emoji"
    ]

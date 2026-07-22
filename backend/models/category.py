"""
Category Entity Model - Defines Category Enitities
Defines Food Types for FoodItems
Food Type Examples: Fresh Produce, Meat, Dairy
Static - User Cannot Edit
"""
from sqlalchemy import Column, Integer, String, JSON
from db import Base

class Category(Base):
    """
    Category Class:
    attributes: 
        id: Unique Numeric Identifier For Indexing
        name: Display Name 
        style: Color-Coding Selection
        icon: Emoji or SVG Display Image
        description: Short Explanation Of Category
        metadata_keys: Unique Attributes Per Category
    """
    __tablename__ = "categories"

    #fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    style = Column(JSON)
    icon = Column(String)
    description = Column(String)
    metadata_keys = Column(JSON, default=list)
    
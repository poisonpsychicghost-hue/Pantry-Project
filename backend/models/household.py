"""
Household Entity Model - Defines Household Entities
Structures Households and Their Attributes
Example: Main_Household, Moms_House, Restaurant_Inventory
Mutable - User Can Edit Whitelist Fields
"""

from sqlalchemy import Column, Integer, String, JSON, Boolean, DateTime
from sqlalchemy.sql import func
from db import Base

class Household(Base):
    """
    Household Class:
        Attributes:
            id: Unique Numeric Identifier For Indexing
            userkey: Unique Login Key
            household_name: Display Name
            email: Optional Recovery Email
            created_at: Date Household Created
            settings: User-Saved Household App Settings
            members: User-Created Household Members
            encrypted: Boolean Encryption Toggle (MVP Always True)
        Required:
            ["userkey", "household_name", "created_at", "members", "encrypted"]
        Whitelist:
            ["household_name", "email", "settings", "members", "encrypted"]
    """
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

    ALLOWED_UPDATED_FIELDS = [
        "household_name", "email", "settings", "members", "encrypted"
    ]
    
    REQUIRED_CREATE_FIELDS = [
        "userkey", "household_name", "created_at", "members", "encrypted"
    ]

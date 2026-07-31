"""
- Shooping Item Service Layer - 
Provides Validation For Shopping Item Entities

"""

from repositories.shoppingitem_repository import (
    get_shoppingitem,
    get_shoppingitem_by_name,
    list_shoppingitems,
    add_shoppingitem,
    update_shoppingitem,
    delete_shoppingitem
)
from models.shoppingitem import ShoppingItem

ALLOWED_UPDATE_FIELDS = ShoppingItem.ALLOWED_UPDATED_FIELDS
REQUIRED_CREATE_FIELDS = ShoppingItem.REQUIRED_CREATE_FIELDS

def create_shoppingitem_service(db, shoppingitem_data):
    """
    Checks Fields In Input shoppingitem_data
    If Missing Required Field > Raises Error
    Else > Loads add_shoppingitem() 

    Args:
        db: Database To Be Passed
        shoppingitem_data: Data For Validation + Passing

    Return:
        add_shoppingitem(db, shoppingitem_data)
    """
    missing = [field for field in REQUIRED_CREATE_FIELDS if field not in shoppingitem_data or not shoppingitem_data[field]]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    return add_shoppingitem(db, shoppingitem_data)

def update_shoppingitem_service(db, shoppingitem_id, update_data):
    """
    Checks Fields In Input update_data
    If Disallowed Field > Raises Error
    Else > Loads update_shoppingitem()

    Args:
        db: Database To Be Passed
        shoppingitem_id: Shooping Item Index To Be Passed
        update_data: Data For Validation = Passing

    Return:
        update_shoppingitem(d, shoppingitem_id, update_data)
    """
    for field in update_data.keys():
        if field not in ALLOWED_UPDATE_FIELDS:
            raise ValueError(f"Field '{field}' not allowed to be updated.")
    return update_shoppingitem(db, shoppingitem_id, update_data)
    
def get_shoppingitem_service(db, shoppingitem_id):
    """
    Loads get_shoppingitem()

    Args:
        db: Database To Be Passed
        shoppingitem_id: Shopping Item Index To Be Passed

    Return:
        get_shoppingitem(db, shoppingitem_id)
    """
    return get_shoppingitem(db, shoppingitem_id)

def get_shoppingitem_by_name_service(db, shoppingitem_name):
    """
    Loads get_shoppingitem_by_name()

    Args:
        db: Database To Be Passed
        shoppingitem_name: Shopping Item Name To Be Passed

    Return:
        get_shoppingitem_by_name(db, shoppingitem_name)
    """
    return get_shoppingitem_by_name(db, shoppingitem_name)

def list_shoppingitem_service(db):
    """
    Loads list_shoppingitems()

    Args:
        db: Database To Be Passed

    Return:
        list_shoppingitems(db)
    """
    return list_shoppingitems(db)

def delete_shoppingitem_service(db, shoppingitem_id):
    """
    Loads delete_shoppingitem()

    Args:
        db: Database To Be Passed
        shoppingitem_id: Shopping Item Index To Be Passed

    Return:
        delete_shoppingitem(db, shoppingitem_id)
    """
    return delete_shoppingitem(db, shoppingitem_id)

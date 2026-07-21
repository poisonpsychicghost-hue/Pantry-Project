from repositories.shoppingitem_repository import (
    get_shoppingitem,
    get_shoppingitem_by_name,
    list_shoppingitems,
    add_shoppingitem,
    update_shoppingitem,
    delete_shoppingitem
)
from models.shoppngitem import ShoppingItem

ALLOWED_UPDATE_FIELDS = ShoppingItem.ALLOWED_UPDATED_FIELDS
REQUIRED_CREATE_FIELDS = ShoppingItem.REQUIRED_CREATE_FIELDS

def create_shoppingitem_service(db, shoppingitem_data):
    missing = [field for field in REQUIRED_CREATE_FIELDS if field not in shoppingitem_data or not shoppingitem_data[field]]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    return add_shoppingitem(db, shoppingitem_data)

def update_shoppingitem_service(db, shoppingitem_id, update_data):
    for field in update_data.keys():
        if field not in ALLOWED_UPDATE_FIELDS:
            raise ValueError(f"Field '{field}' not allowed to be updated.")
    return update_shoppingitem(db, shoppingitem_id, update_data)
    
def get_shoppingitem_service(db, shoppingitem_id):
    return get_shoppingitem(db, shoppingitem_id)

def get_shoppingitem_by_name_service(db, shoppingitem_name):
    return get_shoppingitem_by_name(db, shoppingitem_name)

def list_shoppingitem_service(db):
    return list_shoppingitems(db)

def delete_shoppingitem_service(db, shoppingitem_id):
    return delete_shoppingitem(db, shoppingitem_id)

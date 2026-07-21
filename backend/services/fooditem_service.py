from repositories.fooditem_repository import (
    get_fooditem,
    get_fooditem_by_name,
    get_fooditem_by_status,
    list_fooditems,
    add_fooditem,
    update_fooditem,
    delete_fooditem
)
from models.category import Category
from models.fooditem import FoodItem

ALLOWED_UPDATE_FIELDS = FoodItem.ALLOWED_UPDATE_FIELDS
REQUIRED_CREATE_FIELDS = FoodItem.REQUIRED_CREATE_FIELDS

def create_fooditem_service(db, fooditem_data):
    missing = [field for field in REQUIRED_CREATE_FIELDS if field not in fooditem_data or not fooditem_data[field]]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    category = db.query(Category).filter(Category.id == fooditem_data['category_id']).first()
    allowed_keys = category.metadata_keys if category else []
    if 'item_metadata' in fooditem_data:
        for key in fooditem_data:
            if key not in allowed_keys:
                raise ValueError(f"'{key}' not allowed for category: {category.name}")
            return add_fooditem(db, fooditem_data)
        
def update_fooditem_service(db, fooditem_id, update_data):
    for field in update_data.keys():
        if field not in ALLOWED_UPDATE_FIELDS:
            raise ValueError(f"Field '{field}' is not allwowed to be updated")
    if "item_metadata" in update_data:
        item = get_fooditem(db, fooditem_id)
        category = db.query(Category).filter(Category.id == item.category_id).first()
        allowed_keys = category.metadata_keys if category else []
        for key in update_data["item_metadata"]:
            if key not in allowed_keys:
                raise ValueError(f"'{key}' not allowed for category {category.name}")
    return update_fooditem(db, fooditem_id, update_data)

def get_fooditem_service(db, fooditem_id):
    return get_fooditem(db, fooditem_id)

def get_fooditem_by_name_service(db, fooditem_name):
    return get_fooditem_by_name(db, fooditem_name)

def get_fooditem_by_status_service(db, fooditem_status):
    #need to work out logics after approved status codes locked.
    return get_fooditem_by_status(db, fooditem_status)

def list_fooditems_service(db):
    return list_fooditems(db)

def delete_fooditem_service(db, fooditem_id):
    return delete_fooditem(db, fooditem_id)

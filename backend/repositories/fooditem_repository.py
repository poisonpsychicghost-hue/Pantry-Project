"""
- Food Item Repository - 
CRUD Methods For Food Item Entities

"""
from models.fooditem import FoodItem

def get_fooditem(db, fooditem_id):
    """
    Queries Database For Individual Food Item By ID

    Args:
        db: Database To Be Queried
        fooditem_id: Food Item Index Number For Filter   

    Return:
        Selected Food Item
    """
    return db.query(FoodItem).filter(FoodItem.id == fooditem_id).first()

def get_fooditem_by_name(db, fooditem_name):
    """
    Queries Database For Individual Food Item By Name

    Args:
        db: Database To Be Queried
        fooditem_name: Food Item Name For Filter

    Return:
        Selected Food Item
    """
    return db.query(FoodItem).filter(FoodItem.name.ilike(f"%{fooditem_name}%")).all()\

def get_fooditem_by_status(db, fooditem_status):
    """
    Queries Database For Indvidual Food Items By Item Status

    Args:
        db: Database To Be Queried
        fooditem_status: Food Item Status For Filter

    Return:
        Selected Food Item
    """
    return db.query(FoodItem).filter(FoodItem.status == fooditem_status).all()

def list_fooditems(db):
    """
    Queries Database For Full List Of Food Items In Inventory

    Args:
        db: Database To Be Queried

    Return:
        List Of All Food Items
    """
    return db.query(FoodItem).all()

def add_fooditem(db, item_data):
    """
    Creates A New Food Item Using Input Data
    Adds New Food Item Into Database Inventory

    Args:
        db: Database To Load Created Item Into
        item_data: Structured Data To Build Food Item Entity From

    Return:
        Created Food Item
    """
    item = FoodItem(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return(item)

def update_fooditem(db, fooditem_id, update_data):
    """
    Selects Food Item From Database With ID
    Updates Selected Food Item With New Data

    Args:
        db: Database To Query And Save To
        fooditem_id: Food Item Index Number For Filter
        update_data: New Data To Update Food Item Entity From

        Return Updated Food Item
    """
    item = db.query(FoodItem).filter(FoodItem.id == fooditem_id).first()
    for k, v in update_data.items():
        setattr(item, k, v)
    db.commit()
    db.refresh(item)
    return(item)

def delete_fooditem(db, fooditem_id):
    """
    Selects A Food Item From Database With ID
    Deletes Selected Food Item From Database

    Args:
        db: Database To Query And Remove Food Item From
        fooditem_id: Food Item Index Number For Filter

    Return:
        Deleted Food Item
    """
    item = db.query(FoodItem).filter(FoodItem.id == fooditem_id).first()
    db.delete(item)
    db.commit()
    return item

"""
- Shopping Item Repository -
CRUD Methods For Shopping Item Entites
"""

from models.shoppingitem import ShoppingItem

def get_shoppingitem(db, shoppingitem_id):
    """
    Queries Database For Individual Shopping Item By ID

    Args:
        db: Database To Be Queried
        shoppingitem_id: Shopping Item Index For Filter

    Return:
        Selected Shopping Item
    """
    return db.query(ShoppingItem).filter(ShoppingItem.id == shoppingitem_id).first()

def get_shoppingitem_by_name(db, shoppingitem_name):
    """
    Queries Database For Indivdual Shopping Item By Name

    Args:
        db: Database To Be Queried
        shoppingitem_name: Shopping Item Name For Filter

    Return:
        Seleceted Shopping Item
    """
    return db.query(ShoppingItem).filter(ShoppingItem.name.ilike(f"%{shoppingitem_name}%")).all()

def list_shoppingitems(db):
    """
    Queries Database For List Of All Shopping Items

    Args:
        db: Database To Be Queried

    Return:
        List Of All Shopping Items
    """
    return db.query(ShoppingItem).all()

def add_shoppingitem(db, item_data):
    """
    Creates A New Shopping Item From Input Data
    Adds it To Shopping List Inventory
    
    Args:
        db: Database To Save To
        item_data: Structured Data To Build New Shopping Item From

    Return:
        Created Item
    """
    item = ShoppingItem(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_shoppingitem(db, shoppingitem_id, update_data):
    """
    Selects Individual Shopping Item From Database By ID
    Updates Selected Shopping Item With Input Data

    Args:
        db: Database To Be Queried + Updated
        shoppingitem_id: Shopping Item Index For Filter
        update_data: Structured Data To Update Shopping Item From

    Return:
        Updated Shopping Item
    """
    item = db.query(ShoppingItem).filter(ShoppingItem.id == shoppingitem_id).first()
    for k,v in update_data.items():
        setattr(item, k, v)
    db.commit()
    db.refresh(item)
    return item

def delete_shoppingitem(db, shoppingitem_id):
    """
    Selects Individual Shopping Item From Database With ID
    Deletes Selected Shopping Item From Database

    Args:
        db: Database To Be Queried + Updated
        shoppingitem_id: Shopping Item Index For Filter

    Return:
        Deleted Shopping Item
    """
    item = db.query(ShoppingItem).filter(ShoppingItem.id == shoppingitem_id).first()
    db.delete(item)
    db.commit()
    return item

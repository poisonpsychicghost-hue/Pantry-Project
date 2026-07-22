"""
- Inventory Location Repositry -
CRUD Methods For Inventory Locations

"""
from models.inventorylocation import InventoryLocation

def get_inventorylocation(db, inventorylocation_id):
    """
    Queries Database For Individual Location With ID

    Args:
        db: Database To Be Queried
        inventorylocation_id: Location Index For Filter

    Return:
        Selected Location
    """
    return db.query(InventoryLocation).filter(InventoryLocation.id == inventorylocation_id).first()

def list_inventorylocations(db):
    """
    Queries Database For List Of All Inventory Locations

    Args:
        db: Database To Be Queried

    Return:
        List Of All Inventory Locations
    """
    return db.query(InventoryLocation).all()

def add_inventorylocation(db, location_data):
    """
    Creates A New Inventory Location Using Input Data
    Adds New Inventory Location To Database

    Args:
        db: Database To Save To
        location_data: Structured Data To Build New Location From

    Return:
        Created Location
    """
    loc = InventoryLocation(**location_data)
    db.add(loc)
    db.commit()
    db.refresh(loc)
    return loc

def update_inventorylocation(db, inventorylocation_id, update_data):
    """
    Selects An Individual Inventory Location From Database With ID
    Updates Selected Location With Input Data

    Args:
        db: Database To Query + Update
        inventorylocation_id: Location Index For Filter
        update_data: Structured Data To Update Location From
    
    Return:
        Updated Location
    """
    loc = db.query(InventoryLocation).filter(InventoryLocation.id == inventorylocation_id).first()
    for k, v in update_data.items():
        setattr(loc, k, v)
    db.commit()
    db.refresh(loc)
    return loc

def delete_inventorylocation(db, inventorylocation_id):
    """
    Selects Individual Inventory Location From Database With ID
    Deletes Selected Location From Database

    Args:
        db: Database To Be Queried + Updated
        inventorylocation_id: Location Index For Filter

    Return:
        Deleted Location
    """
    loc = db.query(InventoryLocation).filter(InventoryLocation.id == inventorylocation_id).first()
    db.delete(loc)
    db.commit()
    return loc

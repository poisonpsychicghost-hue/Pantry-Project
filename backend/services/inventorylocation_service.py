"""
- Inventory Locations Service Layer -
Provides Data Validation For Location Entites

"""

from repositories.inventorylocation_repository import(
    get_inventorylocation,
    list_inventorylocations,
    add_inventorylocation,
    update_inventorylocation,
    delete_inventorylocation
)
from models.inventorylocation import InventoryLocation

ALLOWED_UPDATED_FIELDS = InventoryLocation.ALLOWED_UPDATED_FIELDS
IMMUTABLE_BASE_LOCATIONS = ['pantry', 'refrigerator', 'freezer']
REQUIRED_CREATE_FIELDS = InventoryLocation.REQUIRED_CREATE_FIELDS

def create_inventorylocation_service(db, inventorylocation_data):
    """
    Checks Fields In Input inventorylocation_data
    If Missing Required Field > Raises Error
    Else > Loads add_inventorylocation()    

    Args:
        db: Database To Be Passed
        inventorylocation_data: Location Data To Be Validated And Passed

    Return:
        add_inventorylocation(db, inventorylocation_data)
    """
    missing = [field for field in REQUIRED_CREATE_FIELDS if field not in inventorylocation_data or not inventorylocation_data[field]]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    return add_inventorylocation(db, inventorylocation_data)

def update_inventorylocation_service(db, inventorylocation_id, update_data):
    """
    Checks Fields In Input update_data
    If Disallowed Location > Raises Error
    If Disallowed Field > Raises Error
    Else > Loads update_inventorylocation()

    Args:
        db: Database To Be Passed
        inventorylocation_id: Locaton Index To Be Passed
        update_data: Location Data For Validation + Passing
    """
    loc = db.query(InventoryLocation).filter(InventoryLocation.id == inventorylocation_id).first()
    if loc.name in IMMUTABLE_BASE_LOCATIONS:
        raise ValueError(f"Location '{loc.name}' is not allowed to be updated.")
    for field in update_data.keys():
        if field not in ALLOWED_UPDATED_FIELDS:
            raise ValueError(f"Field '{field}' is not allowed to be updated.")
        return update_inventorylocation(db, inventorylocation_id, update_data)
    
def get_inventorylocation_service(db, inventorylocation_id):
    """
    Loads get_inventory_location()

    Args:
        db: Database To Be Passed
        inventorylocation_id: Location Index To Be Passed

    Return:
    get_inventorylocation(db, inventorylocation_id)
    """
    return get_inventorylocation(db, inventorylocation_id)

def list_inventorylocation_service(db):
    """
    Loads list_inventorylocations()

    Args:
        db: Database To Be Passed

    Return: 
        list_inventorylocations(db)
    """
    return list_inventorylocations(db)

def delete_inventorylocation_service(db, inventorylocation_id):
    """
    Loads delete_inventorylocation()

    Args:
        db: Database To Be Passed
        inventorylocation_id: Location Index To Be Passed

    Return:
        delete_inventorylocation(db, inventorylocation_id)
    """
    return delete_inventorylocation(db, inventorylocation_id)

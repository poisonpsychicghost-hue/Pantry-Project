from models.inventorylocation import InventoryLocation

def get_inventorylocation(db, inventorylocation_id):
    return db.query(InventoryLocation).filter(InventoryLocation.id == inventorylocation_id).first()

def list_inventorylocations(db):
    return db.query(InventoryLocation).all()

def add_inventorylocation(db, location_data):
    loc = InventoryLocation(**location_data)
    db.add(loc)
    db.commit()
    db.refresh(loc)
    return loc

def update_inventorylocation(db, inventorylocation_id, update_data):
    loc = db.query(InventoryLocation).filter(InventoryLocation.id == inventorylocation_id).first()
    for k, v in update_data.items():
        setattr(loc, k, v)
    db.commit()
    db.refresh(loc)
    return loc

def delete_inventorylocation(db, inventorylocation_id):
    loc = db.query(InventoryLocation).filter(InventoryLocation.id == inventorylocation_id).first()
    db.delete(loc)
    db.commit()
    return loc

from models.shoppngitem import ShoppingItem

def get_shoppingitem(db, shoppingitem_id):
    return db.query(ShoppingItem).filter(ShoppingItem.id == shoppingitem_id).first()

def get_shoppingitem_by_name(db, shoppingitem_name):
    return db.query(ShoppingItem).filter(ShoppingItem.name.ilike(f"%{shoppingitem_name}%")).all()

def list_shoppingitems(db):
    return db.query(ShoppingItem).all()

def add_shoppingitem(db, item_data):
    item = ShoppingItem(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_shoppingitem(db, shoppingitem_id, update_data):
    item = db.query(ShoppingItem).filter(ShoppingItem.id == shoppingitem_id).first()
    for k,v in update_data.items():
        setattr(item, k, v)
    db.commit()
    db.refresh(item)
    return item

def delete_shoppingitem(db, shoppingitem_id):
    item = db.query(ShoppingItem).filter(ShoppingItem.id == shoppingitem_id).first()
    db.delete(item)
    db.commit()
    return item

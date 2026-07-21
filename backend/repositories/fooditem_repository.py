from models.fooditem import FoodItem

def get_fooditem(db, fooditem_id):
    return db.query(FoodItem).filter(FoodItem.id == fooditem_id).first()

def get_fooditem_by_name(db, fooditem_name):
    return db.query(FoodItem).filter(FoodItem.name.ilike(f"%{fooditem_name}%")).all()\

def get_fooditem_by_status(db, fooditem_status):
    return db.query(FoodItem).filter(FoodItem.status == fooditem_status).all()

def list_fooditems(db):
    return db.query(FoodItem).all()

def add_fooditem(db, item_data):
    item = FoodItem(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return(item)

def update_fooditem(db, fooditem_id, update_data):
    item = db.query(FoodItem).filter(FoodItem.id == fooditem_id).first()
    for k, v in update_data.items():
        setattr(item, k, v)
    db.commit()
    db.refresh(item)
    return(item)

def delete_fooditem(db, fooditem_id):
    item = db.query(FoodItem).filter(FoodItem.id == fooditem_id).first()
    db.delete(item)
    db.commit()
    return item
from models.household import Household

def get_household(db, household_id):
    return db.query(Household).filter(Household.id == household_id).first()

def list_households(db):
    return db.query(Household).all()

def add_household(db, household_data):
    house = Household(**household_data)
    db.add(house)
    db.commit()
    db.refresh(house)
    return house

def update_household(db, household_id, update_data):
    house = db.query(Household).filter(Household.id == household_id).first()
    for k, v in update_data.items():
        setattr(house, k, v)
    db.commit()
    db.refresh(house)
    return house

def delete_household(db, household_id):
    house = db.query(Household).filter(Household.id == household_id).first()
    db.delete(house)
    db.commit()
    return house

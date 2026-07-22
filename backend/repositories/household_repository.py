"""
- Household Repository -
CRUD Methods For HouseHold Entities

"""

from models.household import Household

def get_household(db, household_id):
    """
    Queries Database For Household By ID

    Args:
        db: Database To Be Queried
        household_id: Household Index For Filter
    
    Return:
        Selected Household
    """
    return db.query(Household).filter(Household.id == household_id).first()

def list_households(db):
    """
    Queries Database For Full List Of Households

    Args:
        db: Database To Be Queried
    
    Return:
        List Of All Households
    """
    return db.query(Household).all()

def add_household(db, household_data):
    """
    Creates A New Household Entity Using Input Data
    Adds New Household To Database Inventory

    Args:
        db: Database To Be Queried And Saved To
        household_data: Structured Data To Build New Household Entity From
    
    Return:
        Created Household
    """
    house = Household(**household_data)
    db.add(house)
    db.commit()
    db.refresh(house)
    return house

def update_household(db, household_id, update_data):
    """
    Selects Household Entity From Database With ID
    Updates Selected Household With New Data

    Args:
        db: Database To Be Queried And Saved To
        household_id: Household Index For Filter
        update_data: New Data To Update Household Entity From

    Return: 
        Updated Household
    """
    house = db.query(Household).filter(Household.id == household_id).first()
    for k, v in update_data.items():
        setattr(house, k, v)
    db.commit()
    db.refresh(house)
    return house

def delete_household(db, household_id):
    """
    Selects Household Entity From Database With ID
    Deletes Selected Household From Database

    Args:
        db: Database To Be Queried
        household_id: Household Index For Filter

    Return:
        Deleted Household
    """
    house = db.query(Household).filter(Household.id == household_id).first()
    db.delete(house)
    db.commit()
    return house

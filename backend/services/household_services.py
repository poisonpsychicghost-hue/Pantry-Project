"""
- Household Service Layer -
Provides Data Validation For Household Entities

"""
from repositories.household_repository import(
    get_household,
    list_households,
    add_household,
    update_household,
    delete_household
)
from models.household import Household

ALLOWED_UPDATED_FIELDS = Household.ALLOWED_UPDATED_FIELDS
REQUIRED_CREATE_FIELDS = Household.REQUIRED_CREATE_FIELDS

def create_household_service(db, household_data):
    """
    Checks Fields In Input household_data
    If Missing Required Field > Raises Error
    Else > Loads add_household()

    Args:
        db: Database To Be Passed
        household_data: Data For Validation + Passing

    Return:
        add_household(db, household_data)    
    """
    missing = [field for field in REQUIRED_CREATE_FIELDS if field not in household_data or not household_data[field]]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    return add_household(db, household_data)

def update_household_service(db, household_id, update_data):
    """
    Checks Fields In Input update_data 
    If Disallowed Field > Raises Error
    Else > Loads update_household()

    Args:
        db: Database To Be Passed
        household_id: Household Index To Be Passed
        update_data: Data For Validation + Passing

    Return:
        update_household(db, household_id, update_data)
    """
    for field in update_data:
        if field not in ALLOWED_UPDATED_FIELDS:
            raise ValueError(f"Field '{field}' is not allowed to be updated.")
        return update_household(db, household_id, update_data)
    
def get_household_service(db, household_id):
    """
    Loads get_household()

    Args:
        db: Database To Be Passed
        household_id: Household Index To Be Passed

    Return:
        get_household(db, household_id)
    """
    return get_household(db, household_id)

def list_households_service(db):
    """
    Loads list_households()

    Args:
        db: Database To Be Passed

    Return:
        list_household(db)
    """
    return list_households(db)

def delete_household_service(db, household_id):
    """
    Loads delete_household()

    Args: 
        db: Database To Be Passed
        household_id: Household Index To Be Passed

    Return:
        delete_household(db, household_id)
    """
    return delete_household(db, household_id)

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
    missing = [field for field in REQUIRED_CREATE_FIELDS if field not in household_data or not household_data[field]]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    return add_household(db, household_data)

def update_household_service(db, household_id, update_data):
    for field in update_data:
        if field not in ALLOWED_UPDATED_FIELDS:
            raise ValueError(f"Field '{field}' is not allowed to be updated.")
        return update_household(db, household_id, update_data)
    
def get_household_service(db, household_id):
    return get_household(db, household_id)

def list_households_service(db):
    return list_households(db)

def delete_household_service(db, household_id):
    return delete_household(db, household_id)

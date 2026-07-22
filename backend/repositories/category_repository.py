"""
- Category Repository - 
CRUD Methods For Category Entities (MVP READ-ONLY)

"""
from models.category import Category

def get_category(db, category_id):
    """
    Queries Database For Individual Category by ID

    Args:
        db: The Database to be Queried
        category_id: The Category ID to be Filtered For

    Return:
        Selected Category Dict
    """
    return db.query(Category).filter(Category.id == category_id).first()

def list_categories(db):
    """
    Queries Database For Full List Of Categories
    
    Args:
        db: The Database To Be Queried

    Return:
        List Of All Categories
    """
    return db.query(Category).all()

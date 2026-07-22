"""
- Category Service Layer - 
Provides Data Validation For Category CRUD Methods (MVP READ-ONLY)

"""
from repositories.category_repository import(
    get_category,
    list_categories
)
from models.category import Category

def get_category_service(db, category_id):
    """
    Loads get_category()

    Args:
        db: Database To Be Passed
        category_id: Category Index To Be Passed

    Return: 
        get_category(db, category_id)
    """
    return get_category(db, category_id)

def list_categories_service(db):
    """
    Loads list_categories()

    Args:
        db: Database To Be Passed

    Return:
        list_categories(db)
    """
    return list_categories(db)

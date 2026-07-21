from repositories.category_repository import(
    get_category,
    list_categories
)
from models.category import Category

def get_category_service(db, category_id):
    return get_category(db, category_id)

def list_categories_service(db):
    return list_categories(db)

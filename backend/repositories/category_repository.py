from models.category import Category

def get_category(db, category_id):
    return db.query(Category).filter(Category.id == category_id).first()

def list_categories(db):
    return db.query(Category).all()

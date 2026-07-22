"""
- Test Inventory Seeder - 
Seeds Database With Test Inventory Food Items

"""

from sqlalchemy.orm import Session
from db import engine
from models.fooditem import FoodItem

session = Session(bind=engine)

test_inventory_items = [
    FoodItem(name="Bananas", category_id=1, location_id=1, quantity=5, unit="individual", expiration_date="2026-7-30"), #1
    FoodItem(name="Milk", category_id=2, location_id=2, quantity=1, unit="gallon", expiration_date="2026-7-30"), #2
    FoodItem(name="Bacon", category_id=3, location_id=3, quantity=1.5, unit="lbs", expiration_date="2026-7-30"), #3
    FoodItem(name="Wheat Bread", category_id=4, location_id=1, quantity=1.5, unit="loaf", expiration_date="2026-7-30"), #4
    FoodItem(name="BBQ Chips", category_id=5, location_id=1, quantity=5, unit="bags", expiration_date="2026-7-30"), #5
    FoodItem(name="Chocolate Pudding", category_id=2, location_id=2, quantity=6, unit="packs", expiration_date="2026-7-30"), #6
    FoodItem(name="Flour", category_id=6, location_id=1, quantity=1, unit="lbs", expiration_date="2026-7-30"), #7
    FoodItem(name="Cilantro", category_id=7, location_id=1, quantity=3, unit="oz", expiration_date="2026-7-30"), #8
]

for item in test_inventory_items:
    exists = session.query(FoodItem).filter_by(name=item.name).first()
    if not exists:    
        session.add(item)

session.commit()
print("Seeded Test Food Items!")
session.close()

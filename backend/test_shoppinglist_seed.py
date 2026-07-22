"""
- Test Shopping List Seeder -
Seeds Database With Test Shopping Items

"""


from sqlalchemy.orm import Session
from db import engine
from models.shoppingitem import ShoppingItem

session = Session(bind=engine)

test_shopping_items = [
    ShoppingItem(name="Bananas", date_added="2026-7-23"), #1
    ShoppingItem(name="Milk", date_added="2026-7-23"), #2
    ShoppingItem(name="Bacon", date_added="2026-7-23"), #3
    ShoppingItem(name="Wheat Bread", date_added="2026-7-23"), #4
    ShoppingItem(name="BBQ CHips", date_added="2026-7-23"), #5
    ShoppingItem(name="Chocolate Pudding", date_added="2026-7-23"), #6
    ShoppingItem(name="Flour", date_added="2026-7-23"), #7
    ShoppingItem(name="Cilantro", date_added="2026-7-23"), #8
]

for item in test_shopping_items:
    if not session.query(ShoppingItem).filter_by(name=item.name).first():
        session.add(item)

session.commit()
print("Test Shopping Items Seeded!")
session.close()

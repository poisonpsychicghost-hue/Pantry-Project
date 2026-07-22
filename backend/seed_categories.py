"""
- Category Seeder -
Seeds Database With Defaulted Categories

"""

from sqlalchemy.orm import Session
from db import engine
from models.category import Category
import os

print("Using database URL:", os.getenv("DATABASE_URL"))
session = Session(bind=engine)

seed_categories = [
    Category(
        name="fresh_produce",
        metadata_keys=["is_cut", "washed", "ripeness", "is_frozen", "produce_type"]
    ),
    Category(
        name="dairy",
        metadata_keys=["is_open", "opened_date", "is_frozen", "dairy_type"]
    ),
    Category(
        name="meat",
        metadata_keys=["is_frozen", "meat_type"]
    ),
    Category(
        name="baked",
        metadata_keys=["is_open", "opened_date", "is_frozen", "homemade", "baked_type"]
    ),
    Category(
        name="snack",
        metadata_keys=["is_open", "opened_date", "is_frozen", "homemade", "snack_type"]
    ),
    Category(
        name="other",
        metadata_keys=["is_open", "opened_date", "is_frozen", "homemade"]
    ),
    Category(
        name="spice",
        metadata_keys=["is_open", "opened_date", "homemade", "is_dry"]
    ),
    Category(
        name="condiment",
        metadata_keys=["is_open", "opened_date", "homemade"]
    ),
]

for cat in seed_categories:
    exists = session.query(Category).filter_by(name=cat.name).first()
    print(f"Checking category {cat.name}, exists={exists}")
    if not exists:
        session.add(cat)

session.commit()
print("Seeded Categories!")
session.close()

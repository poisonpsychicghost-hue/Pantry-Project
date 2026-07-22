from sqlalchemy.orm import Session
from db import engine
from models.category import Category
import os

print("Using database URL:", os.getenv("DATABASE_URL"))
session = Session(bind=engine)
print("Started!")
for cat in session.query(Category).all():
    print(f"{cat.id}: {cat.name}")
session.close()
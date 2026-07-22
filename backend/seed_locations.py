"""
- Location Seeder - 
Seeds Database With Default Locations

"""

from sqlalchemy.orm import Session
from db import engine
from models.inventorylocation import InventoryLocation

session = Session(bind=engine)

seed_locations = [
    InventoryLocation(name="Pantry", type="pantry", emoji="🥫", description="Home Pantry"),
    InventoryLocation(name="Refrigerator", type="refrigerator", emoji="🥛", description="Main Refrigerator"),
    InventoryLocation(name="Freezer", type="freezer", emoji="🧊", description="Deep Freezer")
]

for loc in seed_locations:
    exists = session.query(InventoryLocation).filter_by(name=loc.name).first()
    print(f"Checking Location {loc.name}, exists={exists}")
    if not exists:
        session.add(loc)

session.commit()
print("Seeded Initial Locations!")
session.close()

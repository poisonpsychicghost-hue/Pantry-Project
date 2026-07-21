from fastapi import FastAPI
from routes.fooditem import router as fooditem_router
from routes.shoppingitem import router as shoppintitem_router
from routes.inventorylocation import router as inventorylocation_router
from routes.category import router as category_router
from routes.household import router as household_router

app = FastAPI(
    title="Pantry Manager Backend",
    description="Core API for Pantry Manager",
    version="0.1.0"
)

app.include_router(fooditem_router)
app.include_router(shoppintitem_router)
app.include_router(inventorylocation_router)
app.include_router(category_router)
app.include_router(household_router)

def root():
    return {"message": "Pantry Manager Backend is running!"}

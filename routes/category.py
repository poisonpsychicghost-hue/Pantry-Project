"""
- Category Router -
Controls CRUD routes for Category Entities

"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.services.category_service import (
    get_category_service,
    list_categories_service
)
from db import SessionLocal

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/category",
    tags=["category"]
)
@router.get("/category_id")
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category_service(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category

@router.get("/")
def list_categories(db: Session = Depends(get_db)):
    return list_categories_service(db)


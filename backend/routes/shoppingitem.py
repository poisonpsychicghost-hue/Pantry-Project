"""
- Shopping Item Routes - 
Controls CRUD Routes For Shopping Item Entities

"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.shoppingitem_service import (
    create_shoppingitem_service,
    update_shoppingitem_service,
    get_shoppingitem_service,
    get_shoppingitem_by_name_service,
    list_shoppingitem_service,
    delete_shoppingitem_service
)
from db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

router = APIRouter(
    prefix="/shoppingitems",
    tags=["shoppingitems"]
)

@router.get("/{item_id}")
def get_shoppingitem(item_id: int, db: Session = Depends(get_db)):
    item = get_shoppingitem_service(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="ShoppingItem not found.")
    return item

@router.get("/")
def list_shoppingitems(db: Session = Depends(get_db)):
    return list_shoppingitem_service(db)

@router.get("/search/")
def get_shoppingitem_by_name(name: str, db: Session = Depends(get_db)):
    return get_shoppingitem_by_name_service(db, name)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_shoppingitem(shoppingitem_data: dict, db: Session = Depends(get_db)):
    try:
        return create_shoppingitem_service(db, shoppingitem_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{item_id}")
def update_shoppingitem(item_id: int, update_data: dict, db: Session = Depends(get_db)):
    try:
        return update_shoppingitem_service(db, item_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch("/{item_id}")
def patch_shoppingitem(item_id: int, patch_data: dict, db: Session = Depends(get_db)):
    try:
        return update_shoppingitem_service(db, item_id, patch_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{item_id}")
def delete_shoppingitem(item_id: int, db: Session = Depends(get_db)):
    item = delete_shoppingitem_service(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="ShoppingItem not found.")
    return {"detail": "deleted"}

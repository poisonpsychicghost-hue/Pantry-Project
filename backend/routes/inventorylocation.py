"""
- Inventory Location Routes - 
Controls CRUD Routes For Inventory Locations

"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.inventorylocation_service import (
    create_inventorylocation_service,
    update_inventorylocation_service,
    get_inventorylocation_service,
    list_inventorylocation_service,
    delete_inventorylocation_service
)
from db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/inventorylocation",
    tags=["inventorylocation"]
)

@router.get("/{location_id}")
def get_inventorylocation(location_id: int, db: Session = Depends(get_db)):
    location = get_inventorylocation_service(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found.")
    return location

@router.get("/")
def list_inventorylocations(db: Session = Depends(get_db)):
    return list_inventorylocation_service(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_inventorylocation(location_data: dict, db: Session = Depends(get_db)):
    try:
        return create_inventorylocation_service(db, location_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{location_id}")
def update_inventorylocations(location_id: int, patch_data: dict, db: Session = Depends(get_db)):
    try:
        return update_inventorylocation_service(db, location_id, patch_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{location_id}")
def delete_inventorylocation(location_id: int, db: Session = Depends(get_db)):
    location = delete_inventorylocation_service(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return {"detail": "deleted"}

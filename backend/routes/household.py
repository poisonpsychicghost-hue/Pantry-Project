"""
- House Hold Routes -
Controls CRUD Routes For Household Entities

"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.household_services import (
    create_household_service,
    update_household_service,
    get_household_service,
    list_households_service,
    delete_household_service
)
from db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/household",
    tags=["household"]
)

@router.get("/{household_id}")
def get_household(household_id: int, db: Session = Depends(get_db)):
    household = get_household_service(db, household_id)
    if not household:
        raise HTTPException(status_code=404, detail="Household not found")
    return household

@router.get("/")
def list_households(db: Session = Depends(get_db)):
    return list_households_service(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_household(household_data: dict, db: Session = Depends(get_db)):
    try:
        return create_household_service(db, household_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{household_id}")
def update_household(household_id: int, update_data: dict, db: Session = Depends(get_db)):
    try: 
        return update_household_service(db, household_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.patch("/{household_id}")
def patch_household(household_id: int, patch_data, db: Session = Depends(get_db)):
    try:
        return update_household_service(db, household_id, patch_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{household_id}")
def delete_household(household_id: int, db: Session = Depends(get_db)):
    household = get_household_service(db, household_id)
    if not household:
        raise HTTPException(status_code=404, detail="Household not found")
    return {"detail": "deleted"}

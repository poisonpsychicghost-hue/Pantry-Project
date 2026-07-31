"""
- Food Item Routes -
Controls CRUD Routes For Food Item Entities

"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.fooditem_service import(
    create_fooditem_service,
    update_fooditem_service,
    get_fooditem_service,
    get_fooditem_by_name_service,
    get_fooditem_by_status_service,
    list_fooditems_service,
    delete_fooditem_service
)
from db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/fooditems",
    tags=["fooditems"]
)

#----------------#
##----Routes----##
#----------------#

@router.get("/{item_id}")
def get_fooditem(item_id: int, db: Session = Depends(get_db)):
    item = get_fooditem_service(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Food Item not found")
    return item

@router.get("/")
def list_fooditems(db: Session = Depends(get_db)):
    return list_fooditems_service(db)

@router.get("/search/")
def get_fooditems_by_name(name: str, db: Session = Depends(get_db)):
    return get_fooditem_by_name_service(db, name)

@router.get("/status/{status_name}")
def get_fooditems_by_status(status_name: str, db: Session = Depends(get_db)):
    return get_fooditem_by_status_service(db, status_name)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_fooditem(fooditem_data: dict, db: Session = Depends(get_db)):
    try:
        return create_fooditem(db, fooditem_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{item_id}")
def update_fooditem(item_id: int, update_data: dict, db: Session = Depends(get_db)):
    try:
        return update_fooditem_service(db, item_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch("/{item_id}")
def patch_fooditem(item_id: int, patch_data: dict, db: Session = Depends(get_db)):
    try:
        return update_fooditem_service(db, item_id, patch_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("{item_id}")
def delete_fooditem(item_id: int, db: Session = Depends(get_db)):
    item = delete_fooditem_service(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="FoodItem Not Found.")
    return {"detail": "deleted"}

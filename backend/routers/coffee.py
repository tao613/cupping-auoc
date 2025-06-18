from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models
import schemas

router = APIRouter(
    prefix="/coffees",
    tags=["coffees"]
)

@router.get("/", response_model=List[schemas.Coffee])
def get_coffees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coffees = db.query(models.Coffee).offset(skip).limit(limit).all()
    return coffees

@router.get("/{coffee_id}", response_model=schemas.Coffee)
def get_coffee(coffee_id: int, db: Session = Depends(get_db)):
    coffee = db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()
    if coffee is None:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return coffee

@router.post("/", response_model=schemas.Coffee)
def create_coffee(coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
    db_coffee = models.Coffee(**coffee.dict())
    db.add(db_coffee)
    db.commit()
    db.refresh(db_coffee)
    return db_coffee 
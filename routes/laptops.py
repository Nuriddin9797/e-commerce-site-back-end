from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from db import database
from functions.laptops import get_laptops, update_laptop, create_laptops, delete_laptops
from models.laptops import Laptops
from routes.login import get_current_active_user
from schemas.laptops import CreateLaptop, UpdateLaptop
from schemas.users import CreateUser

laptops_router = APIRouter(
    prefix="/laptops",
    tags=["Laptops operation"]
)


@laptops_router.get('/get_filter')
def get(ident: int = 0, brand: str = None, first_price: int = 0, second_price: int = 0, page: int = 1,
        limit: int = 25, ram_size: int = 0, rom_size: int = 0, operation_system: str = None,
        country: str = None, corpus_type: str = None, yadro: int = 0, percent: int = 0, discount_price: int = 0, db: Session = Depends(database)):
    a = get_laptops(ident, brand, first_price, second_price, page, limit, ram_size, rom_size, operation_system, country, corpus_type, yadro, percent, discount_price, db)
    return a


@laptops_router.get('/get_laptops_total')
def get_laptops_count(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    total_likes = db.query(func.count(Laptops.id)).filter(
        Laptops.user_id == current_user.id, Laptops.amount == current_user.id
    ).scalar()
    return total_likes


@laptops_router.post('/create')
def create(forms: List[CreateLaptop], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_laptops(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@laptops_router.put("/update")
def update(forms: List[UpdateLaptop], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_laptop(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@laptops_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_laptops(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



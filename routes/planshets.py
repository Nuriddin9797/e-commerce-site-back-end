from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from functions.planshets import get_planshets, update_planshets, create_planshets, delete_planshets
from models.counts import Counts
from models.planshets import Planshets
from routes.login import get_current_active_user
from schemas.planshets import CreatePlanshets, UpdatePlanshets
from schemas.users import CreateUser
from db import database


planshets_router = APIRouter(
    prefix="/planshets",
    tags=["Planshets operation"]
)


@planshets_router.get('/get')
def get(page: int = 1, limit: int = 25, category_id: int = 0, brand: str = None, ram: int = 0,
        rom: int = 0, sim_slot: int = 0, connection: int = 0, color: str = None, camera: int = 0, self_camera: int = 0,
        first_price: int = 0, second_price: int = 0, discount_price: int = 0, db: Session = Depends(database)):
    return get_planshets(page, limit, category_id, brand, ram, rom, sim_slot, connection, color,  camera, self_camera,
                         first_price, second_price, discount_price, db)


@planshets_router.get('/get_planshets_see_num')
def get_planshets_see_num(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    forms = db.query(Planshets).all()
    see_num = 0
    for form in forms:
        if form:
            see_num += 1
        db.commit()
    return see_num


@planshets_router.get('/get_total')
def get_laptops_count(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    total_counts = db.query(func.count(Planshets.id)).filter(
        Planshets.user_id == current_user.id, Planshets.amount == current_user.id).scalar()
    return total_counts


@planshets_router.post('/create')
def create(forms: List[CreatePlanshets], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_planshets(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@planshets_router.put("/update")
def update(forms: List[UpdatePlanshets], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_planshets(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@planshets_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_planshets(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



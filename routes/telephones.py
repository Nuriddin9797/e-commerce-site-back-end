from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from functions.telephones import get_telephones, update_telephones, create_telephones, delete_telephones
from models.counts import Counts
from models.telephones import Telephones
from routes.login import get_current_active_user
from schemas.telephones import CreateTelephones, UpdateTelephones
from schemas.users import CreateUser
from db import database


telephones_router = APIRouter(
    prefix="/telephones",
    tags=["Telephones operation"]
)


@telephones_router.get('/get')
def get(page: int = 1, limit: int = 25, category_id: int = 0, brand: str = None, ram: int = 0, rom: int = 0,
        sim_slot: int = 0, connection: int = 0, camera: int = 0, self_camera: int = 0, first_price: int = 0,
        second_price: int = 0, discount_price: int = 0, db: Session = Depends(database)):
    return get_telephones(page, limit, category_id, brand, ram, rom, sim_slot, connection,
                  camera, self_camera, first_price, second_price, discount_price, db)


@telephones_router.get('/get_telephones_see_num')
def get_telephones_see_num(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    forms = db.query(Telephones).all()
    see_num = 0
    for form in forms:
        if form:
            see_num += 1
        db.commit()
    return see_num


@telephones_router.get('/get_total')
def get_laptops_count(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    total_counts = db.query(func.count(Telephones.id)).filter(
        Telephones.user_id == current_user.id, Telephones.amount == current_user.id).scalar()
    return total_counts


@telephones_router.post('/create')
def create(forms: List[CreateTelephones], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_telephones(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@telephones_router.put("/update")
def update(forms: List[UpdateTelephones], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_telephones(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@telephones_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_telephones(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")



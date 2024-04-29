from typing import List
from functions.order import create_order, delete_order
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.order import Order
from routes.login import get_current_active_user
from schemas.order import Create_Order
from schemas.users import CreateUser
from db import database

order_router = APIRouter(
    prefix="/order",
    tags=["Order operation"]
)


@order_router.get('/get_total')
def get_all_count(db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    total_likes = db.query(func.count(Order.id)).filter(
        Order.user_id == current_user.id
    ).scalar()
    return total_likes


@order_router.get('/get')
def get_orders(user: CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    orders = db.query(Order).filter(Order.user_id == user.id).all()
    return orders


@order_router.post('/create')
def create(form: Create_Order = Depends(Create_Order), db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_order(form.carts_id, form.name, form.user_name, form.city, form.district, form.address, form.tel_number,db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@order_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_order(ident, db, current_user)
    return {"message": "Buyurtma muvaffaqiyatli o'chirildi"}

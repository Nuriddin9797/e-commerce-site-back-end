from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.cart import Carts
from routes.login import get_current_active_user
from schemas.users import CreateUser
from db import database

purchase_router = APIRouter(
    prefix="/income",
    tags=["Income operation"]
)


@purchase_router.get('/get')
def get_purchase(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    forms = db.query(Carts).filter(Carts.status == True, Carts.amount > 0).all()
    for form in forms:
        purchase = max(form.amount)
    return purchase
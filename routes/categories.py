import random

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.categories import get_categories, update_category, create_category, delete_category
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones
from routes.login import get_current_active_user
from schemas.categories import create_mycategories, update_mycategories
from schemas.users import CreateUser
from db import database

categories_router = APIRouter(
    prefix="/categories",
    tags=["Categories operation"]
)


@categories_router.get('/get_all')
def get_all_category(db: Session = Depends(database)):
    laptops = db.query(Laptops).all()
    planshets = db.query(Planshets).all()
    telephones = db.query(Telephones).all()
    items = telephones + planshets + laptops
    random.shuffle(items)
    return items


@categories_router.get('/get')
def get_category(ident: int = 0, search: str = None,  page: int = 1,
                 limit: int = 25, db: Session = Depends(database)):
    return get_categories(ident, search, page, limit, db)


@categories_router.post('/create')
def create(form: create_mycategories, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_category(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@categories_router.put("/update")
def update(form: update_mycategories, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_category(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@categories_router.delete("/delete")
def delete(ident: int = 0, db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_category(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
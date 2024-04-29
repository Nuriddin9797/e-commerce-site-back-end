from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.cart import Carts
from models.income import Income
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones
from models.users_model import Users
from routes.login import get_current_active_user
from schemas.users import CreateUser
from db import database

income_router = APIRouter(
    prefix="/income",
    tags=["Income operation"]
)


@income_router.get('/get')
def get_incomes(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.role == "admin":
        if current_user.role == "admin":
            total_price = 0
            laptop_price = 0
            planshets_price = 0
            telephones_price = 0
            users = db.query(Users).all()
            for user in users:
                if user:
                    user_total_price = 0
                    carts = db.query(Carts).filter(Carts.status == True).all()
                    for cart in carts:
                        if cart.source == "laptop":
                            laptop = db.query(Laptops).filter(Laptops.id == cart.source_id).first()
                            if laptop:
                                laptop_price += laptop.price
                        elif cart.source == "telephone":
                            telephone = db.query(Telephones).filter(Telephones.id == cart.source_id).first()
                            if telephone:
                                telephones_price += telephone.price
                        elif cart.source == "planshet":
                            planshet = db.query(Planshets).filter(Planshets.id == cart.source_id).first()
                            if planshet:
                                planshets_price += planshet.price
                    total_price = planshets_price + laptop_price + telephones_price
                    new_income = Income(total_price=total_price, laptop_price=laptop_price,
                                        telephones_price=telephones_price, planshets_price=planshets_price)
                    db.add(new_income)
            db.commit()
            return (f"Total price {total_price}, laptop_price {laptop_price}, telephones_price {telephones_price},"
                    f" planshets_price {planshets_price}")


@income_router.get('/get_income_user')
def get_incomes_user(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.role == "admin":
        total_price = 0
        users = db.query(Users).all()
        result = ""
        for user in users:
            laptop_price = 0
            telephones_price = 0
            planshets_price = 0
            if user:
                user_total_price = 0
                carts = db.query(Carts).filter(Carts.status == True, Carts.user_id == user.id).all()
                for cart in carts:
                    if cart.source == "laptop":
                        laptop = db.query(Laptops).filter(Laptops.id == cart.source_id).first()
                        if laptop:
                            laptop_price += laptop.price
                    elif cart.source == "telephone":
                        telephone = db.query(Telephones).filter(Telephones.id == cart.source_id).first()
                        if telephone:
                            telephones_price += telephone.price
                    elif cart.source == "planshet":
                        planshet = db.query(Planshets).filter(Planshets.id == cart.source_id).first()
                        if planshet:
                            planshets_price += planshet.price
                user_total_price = planshets_price + laptop_price + telephones_price
                result += (f" User: {user.id}, Total price: {user_total_price}, "
                           f"Laptop price: {laptop_price}, Telephone price: {telephones_price}, "
                           f"Planshet price: {planshets_price};")
                total_price += user_total_price
        new_income = Income(total_price=total_price)
        db.add(new_income)
        db.commit()
        return result


@income_router.delete('/delete')
def delete_incomes(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    if current_user.role == "admin":
        db.query(Income).delete()
        db.commit()
        raise HTTPException(200,"Amaliyot muvafaqiyatli amalga oshirildi")
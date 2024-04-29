from models.cart import Carts
from models.income import Income
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones
from utils.db_operations import save_in_db
from models.order import Order
from fastapi import HTTPException


def create_order(forms, db, user):
    if user:
        for form in forms:
            new_item_db = Order(
                name=form.name,
                user_name=form.user_name,
                user_id=user.id,
                city=form.city,
                district=form.district,
                address=form.address,
                tel_number=form.tel_number,
                status=False,
                carts_id=form.carts_id
            )
            save_in_db(db, new_item_db)


def delete_order(ident, db, user):
    if user:
        order_to_delete = db.query(Order).filter(Order.id == ident and Order.user_id == user.id).first()
        if order_to_delete is None:
            raise HTTPException(400, "Order not found")
        db.delete(order_to_delete)
        db.commit()
        return {"message": "Order successfully deleted"}
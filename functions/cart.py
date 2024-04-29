from fastapi import HTTPException
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones
from utils.db_operations import get_in_db
from models.cart import Carts


def get_cart(db, user):
    if user:
        all = db.query(Carts).filter(Carts.user_id == user.id).all()
        return all


def create_cart(form, db, user):
    if user:
        if (form.source == "laptops" and db.query(Laptops).filter(Laptops.id == form.source_id).first() is None) or \
                (form.source == "telephone" and db.query(Telephones).filter(Telephones.id == form.source_id).first() is None) or \
                (form.source == "planshet" and db.query(Planshets).filter(Planshets.id == form.source_id).first() is None):
            raise HTTPException(400, "File biriktiriladigan obyekt topilmadi")

        new_item_db = Carts(
            user_id=user.id,
            source=form.source,
            source_id=form.source_id,
            amount=form.amount,
            status=False
                )
        db.add(new_item_db)
        db.commit()


def update_carts(ident, current_user, db):
    if current_user and current_user.role == "admin":
        order_to_update = db.query(Carts).filter(Carts.id == ident).first()
        if order_to_update is None:
            raise HTTPException(status_code=404, detail="Order not found")

        db.query(Carts).filter(Carts.id == ident).update({Carts.status: True})
        db.commit()

        order = db.query(Carts).filter(Carts.id == ident, Carts.status == True).first()
        if order:
            carts = db.query(Carts).filter(Carts.id == order.id).first()
            if carts:
                if carts.source == "laptop":
                    laptop = db.query(Laptops).filter(Laptops.id == carts.source_id, Laptops.amount > 0).first()
                    if laptop:
                        db.query(Laptops).filter(Laptops.id == laptop.id).update({Laptops.amount: Laptops.amount - 1})
                elif carts.source == "telephone":
                    telephone = db.query(Telephones).filter(Telephones.id == carts.source_id,
                                                            Telephones.amount > 0).first()
                    if telephone:
                        db.query(Telephones).filter(Telephones.id == telephone.id).update(
                            {Telephones.amount: Telephones.amount - 1})
                elif carts.source == "planshet":
                    planshet = db.query(Planshets).filter(Planshets.id == carts.source_id, Planshets.amount > 0).first()
                    if planshet:
                        db.query(Planshets).filter(Planshets.id == planshet.id).update(
                            {Planshets.amount: Planshets.amount - 1})
            db.commit()
        return "Order status updated successfully"
    else:
        return "User is not authorized to perform this action"


def delete_cart(ident, db, current_user):
    if current_user:
        get_in_db(db, Carts, ident)
        delete = db.query(Carts).filter(Carts.id == ident).delete()
        if delete:
            Carts.amount=-1
        db.commit()


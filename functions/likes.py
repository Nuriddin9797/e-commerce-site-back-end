from fastapi import HTTPException
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones
from utils.db_operations import get_in_db
from models.likes import Likes
from sqlalchemy.orm import joinedload


def get_likes(db, user):
    if user:
        return db.query(Likes).options(joinedload(Likes.laptop), joinedload(Likes.planshets),
                                       joinedload(Likes.telephone)).filter(Likes.user_id == user.id).all()


def create_likes(source, source_id, db, user):
    if user:
        if (source == "laptops" and db.query(Laptops).filter(Laptops.id == source_id).first() is None) or \
                    (source == "telephone" and db.query(Telephones).filter(Telephones.id == source_id).first() is None) or \
                    (source == "planshet" and db.query(Planshets).filter(Planshets.id == source_id).first() is None):
                raise HTTPException(400, "File biriktiriladigan obyekt topilmadi")

        if source_id is None:
            raise HTTPException(400, "Bunday id li ma'liumot yo'q")
        existing_like = db.query(Likes).filter(
            Likes.user_id == user.id,
            Likes.source == source,
            Likes.source_id == source_id
        ).first()
        if existing_like is None:
            new_item_db = Likes(
                user_id=user.id,
                source=source,
                source_id=source_id
                    )
            db.add(new_item_db)
            db.commit()
            if source == "laptops" and Laptops.id == source_id:
                db.query(Laptops).update({
                Laptops.faworite: Laptops.faworite + 1})
            db.commit()
            if source == "telephone" and Telephones.id == source_id:
                db.query(Planshets).update({
                Telephones.faworite: Telephones.faworite + 1
                })
            db.commit()

            if source == "planshet" and Planshets.id == source_id:
                db.query(Planshets).update({
                Planshets.faworite: Planshets.faworite + 1
                })
            db.commit()


def delete_likes(ident, db, user):
    if user:
        get_in_db(db, Likes, ident)
        db.query(Likes).filter(Likes.id == ident).delete()
        db.commit()


def delete_all(db, user):
    if user:
        deleted_likes = db.query(Likes).filter(Likes.user_id == user.id).all()
        db.query(Likes).filter(Likes.user_id == user.id).delete()
        db.commit()
        return deleted_likes


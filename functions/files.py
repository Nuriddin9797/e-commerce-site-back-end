import os
from fastapi import HTTPException

from models.files import Files
from models.users_model import Users
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones
from utils.db_operations import get_in_db


def create_file(new_files, source, source_id, db, user):
    if user.role == "admin":
        if (source == "laptops" and db.query(Laptops).filter(Laptops.id == source_id).first() is None) or \
                (source == "user" and db.query(Users).filter(Users.id == source_id).first() is None) or \
                (source == "telephone" and db.query(Telephones).filter(Telephones.id == source_id).first() is None) or \
                (source == "planshet" and db.query(Planshets).filter(Planshets.id == source_id).first() is None):
            raise HTTPException(400, "File biriktiriladigan obyekt topilmadi")
        uploaded_file_objects = []
        for new_file in new_files:
            ext = os.path.splitext(new_file.filename)[-1].lower()
            if ext not in [".jpg", ".png", ".mp3", ".mp4", ".gif", ".jpeg"]:
                raise HTTPException(400,"Yuklanadigan fayl formati mos emas")
            file_location = f"files/{new_file.filename}"
            with open(file_location, "wb+") as file_objects:
                file_objects.write(new_file.file.read())

            new_item_db = Files(
                file=new_file.filename,
                source=source,
                source_id=source_id,


            )
            uploaded_file_objects.append(new_item_db)

        db.add_all(uploaded_file_objects)
        db.commit()


def delete_files(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Files, ident)
        db.query(Files).filter(Files.id == ident).delete()
        db.commit()


def update_files(new_files, source, source_id, user, db):
    if user.role == "admin":
        items = db.query(Files).filter(Files.source == source,
                                       Files.source_id == source_id).all()
        for item in items:
            delete_files(item.id, db, user)
            create_file(new_files, source, source_id, user, db)
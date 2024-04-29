from fastapi import HTTPException
from utils.db_operations import save_in_db
from utils.pagination import pagination
from models.categories import Categories


def get_categories(ident, search, page, limit, db):

    if ident > 0:
        ident_filter = Categories.id == ident
    else:
        ident_filter = Categories.id > 0

    if search:
        search_formatted = "%{}%".format(search)
        search_filter = (Categories.name.like(search_formatted))
    else:
        search_filter = Categories.id > 0

    items = db.query(Categories).filter(ident_filter, search_filter).order_by(Categories.id.desc())

    return pagination(items, page, limit)


def create_category(form, db, user):
    new_item_db = Categories(
        name=form.name,
        user_id=user.id)
    save_in_db(db, new_item_db)


def update_category(form, db, user):
    if user.role == "admin":
        category = db.query(Categories).filter(Categories.id == form.ident).first()
        if not category:
            raise HTTPException(status_code=404, detail="Kategoriya topilmadi")

        db.query(Categories).filter(Categories.id == form.ident).update({
            Categories.name: form.name
    })
    db.commit()


def delete_category(ident, db, user):
    if user.role == "admin":
        category = db.query(Categories).filter(Categories.id == ident).first()
        if not category:
            raise HTTPException(status_code=404, detail="Kategoriya topilmadi")
    db.query(Categories).filter(Categories.id == ident).delete()
    db.commit()



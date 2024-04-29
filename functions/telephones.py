from fastapi import HTTPException
from models.categories import Categories
from models.counts import Counts
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.telephones import Telephones


def get_telephones(page, limit, category_id, brand, ram, rom, sim_slot, connection,
                  camera, self_camera, first_price, second_price, discount_price, db):
    if category_id > 0:
        category_filter = Categories.id == category_id
    else:
        category_filter = Telephones.id > 0
    if brand:
        search_formatted = "%{}%".format(search)
        brand_filter = (Telephones.brand.like(search_formatted))
    else:
        brand_filter = Telephones.id > 0

    if ram > 0:
        ram_filter = Telephones.ram == ram
    else:
        ram_filter = Telephones.id > 0
    if rom > 0:
        rom_filter = Telephones.rom == ram
    else:
        rom_filter = Telephones.id > 0

    if sim_slot:
        search_formatted = "%{}%".format(search)
        brand_filter = (Telephones.sim_slot.like(search_formatted))
    else:
        sim_filter = Telephones.id > 0

    if connection > 0:
        connection_filter = Telephones.connection == connection
    else:
        connection_filter = Telephones.id > 0

    if camera > 0:
        camera_filter = Telephones.camera == camera
    else:
        camera_filter = Telephones.id > 0
    if self_camera > 0:
        self_camera_filter = Telephones.self_camera == self_camera
    else:
        self_camera_filter = Telephones.id > 0
    if first_price > 0:
        first_price_filter = Telephones.price > first_price
    else:
        first_price_filter = Telephones.id > 0
    if second_price > 0:
        second_price_filter = Telephones.price < second_price
    else:
        second_price_filter = Telephones.id > 0
    if discount_price > 0:
        discount_price_filter = Telephones.discount_price == discount_price
    else:
        discount_price_filter = Telephones.id > 0

    items = db.query(Telephones).filter(
        category_filter, brand_filter, ram_filter, rom_filter, sim_filter, connection_filter,
        camera_filter, self_camera_filter, first_price_filter, second_price_filter, discount_price_filter).order_by(Telephones.id.desc())

    return pagination(items, page, limit)


def create_telephones(forms, db, user):
    for form in forms:
        if user.role == "admin":
            if form.price > 0:
                discount_price = form.price - form.price * (form.percent / 100),
            else:
                discount_price = 0
            new_item_db = Telephones(
                brand=form.brand,
                model=form.model,
                ram=form.ram,
                rom=form.rom,
                color=form.color,
                battery=form.battery,
                connection=form.connection,
                sim_slot=form.sim_slot,
                display=form.display,
                camera=form.camera,
                self_camera=form.self_camera,
                operation_system=form.operation_system,
                year=form.year,
                weight=form.weight,
                country=form.country,
                price=form.price,
                percent=form.percent,
                discount_price=discount_price,
                discount_time=form.discount_time,
                category_id=form.category_id,
                user_id=user.id,
                amount=form.amount,
                see_num=0
            )
            save_in_db(db, new_item_db)


def update_telephones(forms, db, user):
    for form in forms:
        if user.role == "admin":
            update = db.query(Telephones).filter(Telephones.id == form.ident).first()
            if not update:
                raise HTTPException(status_code=404, detail="Telefon topilmadi")
            if form.price > 0:
                discount_price = form.price - form.price * (form.percent / 100),
            else:
                discount_price = 0
            db.query(Telephones).filter(Telephones.id == form.ident).update({
                Telephones.brand: form.brand,
                Telephones.model: form.model,
                Telephones.ram: form.ram,
                Telephones.rom: form.rom,
                Telephones.color: form.color,
                Telephones.battery: form.battery,
                Telephones.connection: form.connection,
                Telephones.sim_slot: form.sim_slot,
                Telephones.display: form.display,
                Telephones.camera: form.camera,
                Telephones.self_camera: form.self_camera,
                Telephones.operation_system: form.operation_system,
                Telephones.year: form.year,
                Telephones.weight: form.weight,
                Telephones.country: form.country,
                Telephones.price: form.price,
                Telephones.percent: form.percent,
                Telephones.discount_price: discount_price,
                Telephones.discount_time: form.discount_time,
                Telephones.category_id: form.category_id
                })
            db.commit()


def delete_telephones(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Telephones, ident)
        db.query(Telephones).filter(Telephones.id == ident).delete()
        db.commit()
from fastapi import HTTPException
from models.categories import Categories
from models.counts import Counts
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.planshets import Planshets


def get_planshets(page, limit, category_id, brand, ram, rom, sim_slot, connection, color,
                  camera, self_camera, first_price, second_price, discount_price, db):
    if category_id > 0:
        category_filter = Categories.id == category_id
    else:
        category_filter = Planshets.id > 0
    if brand:
        search_formatted = "%{}%".format(search)
        brand_filter = (Planshets.brand.like(search_formatted))
    else:
        brand_filter = Planshets.id > 0
    if ram > 0:
        ram_filter = Planshets.ram == ram
    else:
        ram_filter = Planshets.id > 0
    if rom > 0:
        rom_filter = Planshets.rom == ram
    else:
        rom_filter = Planshets.id > 0
    if sim_slot:
        sim_filter = Planshets.sim_slot == sim_slot
    else:
        sim_filter = Planshets.id > 0
    if connection > 0:
        connection_filter = Planshets.connection == connection
    else:
        connection_filter = Planshets.id > 0
    if color:
        color_filter = Planshets.color ==color
    else:
        color_filter = Planshets.id > 0
    if camera > 0:
        camera_filter = Planshets.camera == camera
    else:
        camera_filter = Planshets.id > 0
    if self_camera > 0:
        self_camera_filter = Planshets.self_camera == self_camera
    else:
        self_camera_filter = Planshets.id > 0
    if first_price > 0:
        first_price_filter = Planshets.price > first_price
    else:
        first_price_filter = Planshets.id > 0
    if second_price > 0:
        second_price_filter = Planshets.price < second_price
    else:
        second_price_filter = Planshets.id > 0
    if discount_price > 0:
        discount_price_filter = Planshets.discount_price == discount_price
    else:
        discount_price_filter = Planshets.id > 0

    items = db.query(Planshets).filter(
        category_filter, brand_filter, ram_filter, rom_filter, sim_filter, connection_filter, color_filter,
        camera_filter, self_camera_filter, first_price_filter, second_price_filter, discount_price_filter).order_by(Planshets.id.desc())
    return pagination(items, page, limit)


def create_planshets(forms, db, user):
    planshets_total = 0
    for form in forms:
        if user.role == "admin":
            if form.price > 0:
                discount_price = form.price - form.price * (form.percent / 100),
            else:
                discount_price = 0
            new_item_db = Planshets(
                brand=form.brand,
                model=form.model,
                ram=form.ram,
                rom=form.rom,
                display=form.display,
                matritsa=form.matritsa,
                weight=form.weight,
                year=form.year,
                country=form.country,
                sim_slot=form.sim_slot,
                connection=form.connection,
                operation_system=form.operation_system,
                color=form.color,
                camera=form.camera,
                self_camera=form.self_camera,
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


def update_planshets(forms, db, user):
    for form in forms:
        if user.role == "admin":
            update = db.query(Planshets).filter(Planshets.id == form.ident).first()
            if not update:
                raise HTTPException(status_code=404, detail="Planshet topilmadi")
            if form.price > 0:
                discount_price = form.price - form.price * (form.percent / 100),
            else:
                discount_price = 0

            db.query(Planshets).filter(Planshets.id == form.ident).update({
                Planshets.brand: form.brand,
                Planshets.model: form.model,
                Planshets.ram: form.ram,
                Planshets.rom: form.rom,
                Planshets.display: form.display,
                Planshets.matritsa: form.matritsa,
                Planshets.weight: form.weight,
                Planshets.year: form.year,
                Planshets.country: form.country,
                Planshets.sim_slot: form.sim_slot,
                Planshets.connection: form.connection,
                Planshets.operation_system: form.operation_system,
                Planshets.color: form.color,
                Planshets.camera: form.camera,
                Planshets.self_camera: form.self_camera,
                Planshets.price: form.price,
                Planshets.percent: form.percent,
                Planshets.discount_price: discount_price,
                Planshets.discount_time: form.discount_time,
                Planshets.category_id: form.category_id
                })
            db.commit()



def delete_planshets(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Planshets, ident)
        db.query(Planshets).filter(Planshets.id == ident).delete()
        db.commit()

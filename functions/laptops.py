from sqlalchemy.orm import joinedload
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.laptops import Laptops
from fastapi import HTTPException


def get_laptops(ident, brand, first_price, second_price, page, limit, ram_size, rom_size, operation_system, country,
                corpus_type, yadro, percent, discount_price, db):
    if ident > 0:
        laptop_filter = Laptops.id == ident
        db.query(Laptops).filter(Laptops.id == ident).update({
            Laptops.see_num: Laptops.see_num + 1
        })
        db.commit()
    else:
        laptop_filter = Laptops.id > 0
    if brand:
        search_formatted = "%{}%".format(brand)
        brand_filter = (Laptops.brand.like(search_formatted))
    else:
        brand_filter = Laptops.id > 0

    if first_price > 0:
        first_price_filter = Laptops.price > first_price
    else:
        first_price_filter = Laptops.id > 0
    if second_price > 0:
        second_price_filter = Laptops.price < second_price
    else:
        second_price_filter = Laptops.id > 0

    if ram_size > 0:
        ram_filter = Laptops.ram_size == ram_size
    else:
        ram_filter = Laptops.id > 0
    if rom_size > 0:
        rom_filter = Laptops.rom_size == rom_size
    else:
        rom_filter = Laptops.id > 0

    if operation_system:
        os_search_formatted = "%{}%".format(operation_system)
        os_filter = (Laptops.operation_system.like(os_search_formatted))
    else:
        os_filter = Laptops.id > 0
    if country:
        os_search_formatted = "%{}%".format(operation_system)
        country_filter = (Laptops.country.like(os_search_formatted))
    else:
        country_filter = Laptops.id > 0
    if corpus_type:
        os_search_formatted = "%{}%".format(operation_system)
        corpus_filter = (Laptops.corpus_type.like(os_search_formatted))
    else:
        corpus_filter = Laptops.id > 0
    if yadro:
        os_search_formatted = "%{}%".format(operation_system)
        yadro_filter = (Laptops.yadro.like(os_search_formatted))
    else:
        yadro_filter = Laptops.id > 0
    if percent > 0:
        percent_filter = Laptops.percent == percent
    else:
        percent_filter = Laptops.id > 0
    if discount_price > 0:
        discount_price_filter = Laptops.discount_price == discount_price
    else:
        discount_price_filter = Laptops.id > 0
    items = (db.query(Laptops).options(joinedload(Laptops.files)).filter(laptop_filter,
                                                                         brand_filter, first_price_filter,
                                                                         second_price_filter, ram_filter,
                                                                         rom_filter, os_filter, country_filter,
                                                                         corpus_filter, yadro_filter, percent_filter,
                                                                         discount_price_filter).order_by(Laptops.id.desc()))

    return pagination(items, page, limit)


def create_laptops(forms, db, user):
    for form in forms:
        if user.role == "admin":
            if form.price > 0:
                discount_price = form.price - form.price * (form.percent / 100),
            else:
                discount_price = 0
            new_item_db = Laptops(
                brand=form.brand,
                model=form.model,
                processor=form.processor,
                ram_type=form.ram_type,
                ram_size=form.ram_size,
                rom_type=form.rom_type,
                rom_size=form.rom_size,
                color=form.color,
                operation_system=form.operation_system,
                display=form.display,
                matritsa=form.matritsa,
                videocard_type=form.videocard_type,
                videocard_size=form.videocard_size,
                yadro=form.yadro,
                types=form.types,
                display_refresh=form.display_refresh,
                weight=form.weight,
                corpus_type=form.corpus_type,
                year=form.year,
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


def update_laptop(forms, db, user):
    for form in forms:
        if user.role == "admin":
            update = db.query(Laptops).filter(Laptops.id == form.ident).first()
            if not update:
                raise HTTPException(status_code=404, detail="Laptops topilmadi")
            if form.price > 0:
                discount_price = form.price - form.price * (form.percent / 100),
            else:
                discount_price = 0
            db.query(Laptops).filter(Laptops.id == form.ident).update({
                Laptops.brand: form.brand,
                Laptops.model: form.model,
                Laptops.processor: form.processor,
                Laptops.ram_type: form.ram_type,
                Laptops.ram_size: form.ram_size,
                Laptops.rom_type: form.rom_type,
                Laptops.rom_size: form.rom_size,
                Laptops.color: form.color,
                Laptops.operation_system: form.operation_system,
                Laptops.display: form.display,
                Laptops.matritsa: form.matritsa,
                Laptops.videocard_type: form.videocard_type,
                Laptops.videocard_size: form.videocard_size,
                Laptops.yadro: form.yadro,
                Laptops.types: form.types,
                Laptops.display_refresh: form.display_refresh,
                Laptops.weight: form.weight,
                Laptops.corpus_type: form.corpus_type,
                Laptops.year: form.year,
                Laptops.country: form.country,
                Laptops.price: form.price,
                Laptops.percent: form.percent,
                Laptops.discount_price: discount_price,
                Laptops.discount_time: form.discount_time,
                Laptops.category_id: form.category_id,
                Laptops.amount: form.amount
            })
            db.commit()


def delete_laptops(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Laptops, ident)
        db.query(Laptops).filter(Laptops.id == ident).delete()
        db.commit()
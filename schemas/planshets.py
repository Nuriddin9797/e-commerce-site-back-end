from datetime import datetime

from pydantic import BaseModel, validator, Field
from db import SessionLocal


class CreatePlanshets(BaseModel):
    brand: str
    model: str
    ram: int = Field(..., gt=0)
    rom: int = Field(..., gt=0)
    display: float
    matritsa: str
    weight: int = Field(..., gt=0)
    year: int = Field(..., gt=0)
    country: str
    sim_slot: int = Field(..., gt=0)
    connection: int = Field(..., gt=0)
    operation_system: str
    color: str
    camera: int = Field(..., gt=0)
    self_camera: int = Field(..., gt=0)
    price: int = Field(..., gt=0)
    percent: int
    discount_price: int
    discount_time: datetime
    category_id: int = Field(..., gt=0)
    see_num: int



    #
    #
    # @validator('username')
    # def username_validate(cls, username):
    #     validate_my = db.query(Users).filter(
    #         Users.username == username,
    #     ).count()
    #
    #     if validate_my != 0:
    #         raise ValueError('Bunday login avval ro`yxatga olingan!')
    #     return username
    #
    # @validator('password')
    # def password_validate(cls, password):
    #     if len(password) < 8:
    #         raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
    #     return password


class UpdatePlanshets(BaseModel):
    ident: int = Field(..., gt=0)
    brand: str
    model: str
    ram: int = Field(..., gt=0)
    rom: int = Field(..., gt=0)
    display: float
    matritsa: str
    weight: int = Field(..., gt=0)
    year: int = Field(..., gt=0)
    country: str
    sim_slot: int = Field(..., gt=0)
    connection: int = Field(..., gt=0)
    operation_system: str
    color: str
    camera: int = Field(..., gt=0)
    self_camera: int = Field(..., gt=0)
    price: int = Field(..., gt=0)
    percent: int
    discount_price: int
    discount_time: datetime
    category_id: int = Field(..., gt=0)
    amount: int
#
#
# @validator('username')
#     def username_validate(cls, username):
#         validate_my = db.query(Users).filter(
#             Users.username == username,
#         ).count()
#
#         if validate_my != 0:
#             raise ValueError('Bunday login avval ro`yxatga olingan!')
#         return username
#
#     @validator('password')
#     def password_validate(cls, password):
#         if len(password) < 8:
#             raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
#         return password
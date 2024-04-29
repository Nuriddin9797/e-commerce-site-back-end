from datetime import datetime
from pydantic import BaseModel, Field
from db import SessionLocal

db = SessionLocal()


class CreateLaptop(BaseModel):
    brand: str
    model: str
    processor: str
    ram_type: str
    ram_size: int = Field(..., gt=0)
    rom_type: str
    rom_size: int = Field(..., gt=0)
    color: str
    operation_system: str
    display: float
    matritsa: str
    videocard_type: str
    videocard_size: int = Field(..., gt=0)
    yadro: int = Field(..., gt=0)
    types: str
    display_refresh: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    corpus_type: str
    year: int = Field(..., gt=0)
    country: str
    price: int = Field(..., gt=0)
    percent: int
    discount_price: int
    discount_time: datetime
    category_id: int = Field(..., gt=0)
    amount: int = Field(..., gt=0)


class UpdateLaptop(BaseModel):
    ident: int = Field(..., gt=0)
    brand: str
    model: str
    processor: str
    ram_type: str
    ram_size: int = Field(..., gt=0)
    rom_type: str
    rom_size: int = Field(..., gt=0)
    color: str
    operation_system: str
    display: float
    matritsa: str
    videocard_type: str
    videocard_size: int = Field(..., gt=0)
    yadro: int = Field(..., gt=0)
    types: str
    display_refresh: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    corpus_type: str
    year: int = Field(..., gt=0)
    country: str
    price: int = Field(..., gt=0)
    percent: int
    discount_price: int
    discount_time: datetime
    category_id: int = Field(..., gt=0)
    amount: int = Field(..., gt=0)
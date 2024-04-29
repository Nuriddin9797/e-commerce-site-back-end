from pydantic import BaseModel


class Create_Order(BaseModel):
    name: str
    user_name: str
    city: str
    district: str
    address: str
    tel_number: str
    carts_id: int



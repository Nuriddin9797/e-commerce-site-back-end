from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer, Boolean
from models.cart import Carts
from models.users_model import Users


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    phone_number = Column(String(255), nullable=False)
    gmail = Column(String(255), nullable=False)
    file = Column(String(255), nullable=False)
    carts_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Order.user_id)

    carts = relationship("Carts", foreign_keys=[carts_id],
                         primaryjoin=lambda: Carts.id == Order.carts_id)
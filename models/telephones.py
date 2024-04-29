from sqlalchemy.orm import relationship

from db import Base
from sqlalchemy import Column, String, Integer, Double, DateTime

from models.categories import Categories
from models.users_model import Users


class Telephones(Base):
    __tablename__ = 'telephone'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    ram = Column(Integer, nullable=False)
    rom = Column(Integer, nullable=False)
    color = Column(String(255), nullable=True)
    battery = Column(Integer, nullable=True)
    connection = Column(Integer, nullable=True)
    sim_slot = Column(Integer, nullable=True)
    display = Column(Double, nullable=True)
    camera = Column(Integer, nullable=True)
    self_camera = Column(Integer, nullable=True)
    operation_system = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    country = Column(String(255), nullable=True)
    price = Column(Integer, nullable=True)
    percent = Column(Integer, nullable=False)
    discount_price = Column(Integer, nullable=False)
    discount_time = Column(DateTime, nullable=False, default=0)
    category_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    amount = Column(Integer, nullable=False)
    see_num = Column(Integer, default=0)
    faworite = Column(Integer, default=0)

    category = relationship("Categories", foreign_keys=[category_id],
                            primaryjoin=lambda: Categories.id == Telephones.category_id)

    user = relationship("Users", foreign_keys=[user_id],
                            primaryjoin=lambda: Users.id == Telephones.user_id)

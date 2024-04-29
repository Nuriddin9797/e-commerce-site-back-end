from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer, Double, DateTime
from models.categories import Categories
from models.users_model import Users


class Laptops(Base):
    __tablename__ = 'laptops'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    processor = Column(String(255), nullable=False)
    ram_type = Column(String(255), nullable=True)
    ram_size = Column(Integer, nullable=False)
    rom_type = Column(String(255), nullable=True)
    rom_size = Column(Integer, nullable=False)
    color = Column(String(255), nullable=True)
    operation_system = Column(String(255), nullable=True)
    display = Column(Double, nullable=True)
    matritsa = Column(String(255), nullable=True)
    videocard_type = Column(String(255), nullable=True)
    videocard_size = Column(Integer, nullable=True)
    yadro = Column(Integer, nullable=True)
    types = Column(String(255), nullable=True)
    display_refresh = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    corpus_type = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    country = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False)
    percent = Column(Integer, nullable=False, default=0)
    discount_price = Column(Integer, nullable=False, default=0)
    discount_time = Column(DateTime, nullable=False, default=0)
    category_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    see_num = Column(Integer, default=0)
    faworite = Column(Integer)

    category = relationship("Categories", foreign_keys=[category_id],
                            primaryjoin=lambda: Categories.id == Laptops.category_id)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Laptops.user_id)
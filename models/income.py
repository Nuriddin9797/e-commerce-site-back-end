from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, Numeric
from models.order import Order
from models.users_model import Users


class Income(Base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # order_id = Column(Integer, nullable=False, default=0)
    # user_id = Column(Integer, nullable=False)
    laptop_price = Column(Numeric, nullable=False, default=0)
    planshets_price = Column(Numeric, nullable=False, default=0)
    telephones_price = Column(Numeric, nullable=False, default=0)
    total_price = Column(Numeric, nullable=False)

    # user = relationship("Users", foreign_keys=[user_id],
    #                     primaryjoin=lambda: Users.id == Income.user_id)
    # order = relationship("Order", foreign_keys=[order_id],
    #                     primaryjoin=lambda: Order.id == Income.order_id)
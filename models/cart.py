from sqlalchemy.orm import relationship, backref
from db import Base
from sqlalchemy import Column, String, Integer, and_, Boolean
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones


class Carts(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=True)

    laptop = relationship("Laptops", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Laptops.id == Carts.source_id, Carts.source == "laptop"),
                          backref=backref("carts"))

    telephone = relationship("Telephones", foreign_keys=[source_id],
                             primaryjoin=lambda: and_(Telephones.id == Carts.source_id, Carts.source == "telephone"),
                             backref=backref("carts"))

    planshets = relationship("Planshets", foreign_keys=[source_id],
                             primaryjoin=lambda: and_(Planshets.id == Carts.source_id, Carts.source == "planshet"),
                             backref=backref("carts"))

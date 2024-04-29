from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer
from models.users_model import Users


class Counts(Base):
    __tablename__ = 'counts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    laptops_total = Column(Integer, nullable=False, default=0)
    planshets_total = Column(Integer, nullable=False, default=0)
    telephones_total = Column(Integer, nullable=False, default=0)
    user_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Counts.user_id)
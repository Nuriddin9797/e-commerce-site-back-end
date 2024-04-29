from sqlalchemy.orm import backref, relationship
from db import Base
from sqlalchemy import Column, String, Integer, and_, Boolean
from models.laptops import Laptops
from models.planshets import Planshets
from models.telephones import Telephones
from models.users_model import Users


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Likes.user_id)

    laptop = relationship("Laptops", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Laptops.id == Likes.source_id, Likes.source == "laptop"),
                          backref=backref("likes"))

    telephone = relationship("Telephones", foreign_keys=[source_id],
                             primaryjoin=lambda: and_(Telephones.id == Likes.source_id, Likes.source == "telephone"),
                             backref=backref("likes"))

    planshets = relationship("Planshets", foreign_keys=[source_id],
                             primaryjoin=lambda: and_(Planshets.id == Likes.source_id, Likes.source == "planshet"),
                             backref=backref("likes"))

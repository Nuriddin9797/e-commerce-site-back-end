from sqlalchemy.orm import relationship

from db import Base
from sqlalchemy import Column, String, Integer

from models.users_model import Users


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Categories.user_id)
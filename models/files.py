from db import Base
from sqlalchemy import Column, String, Integer, and_, Text
from sqlalchemy.orm import relationship, backref
from models.laptops import Laptops
from models.telephones import Telephones
from models.planshets import Planshets
from models.users_model import Users



class Files(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)
    file = Column(String(255), nullable=False)

    laptop = relationship("Laptops", foreign_keys=[source_id],
                        primaryjoin=lambda: and_(Laptops.id == Files.source_id, Files.source == "laptop"),
                        backref=backref("files"))

    telephone = relationship("Telephones", foreign_keys=[source_id],
                        primaryjoin=lambda: and_(Telephones.id == Files.source_id, Files.source == "telephone"),
                        backref=backref("files"))

    planshets = relationship("Planshets", foreign_keys=[source_id],
                        primaryjoin=lambda: and_(Planshets.id == Files.source_id, Files.source == "planshet"),
                        backref=backref("files"))
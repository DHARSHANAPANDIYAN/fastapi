
from multiprocessing.managers import BaseManager
from sqlalchemy import Column, Integer,ForeignKey, String
from .database import Base
from sqlalchemy.orm import relationship

class Item(Base):

    __tablename__ = 'items_table'
    __table_args__ = {"schema": "freshers_dev"}
    id = Column(Integer,primary_key=True, index=True)
    item_descp = Column(String)
    supplier = Column(String)
    # cpmrp_id = Column(Integer, ForeignKey('freshers_dev.cpmrp_table.cpmrp_item'))

    owner = relationship("CPMRP", back_populates="items_table")


class CPMRP(Base):
    __tablename__ = 'cpmrp_table'
    __table_args__ = {"schema": "freshers_dev"} 
    cpmrp_item = Column(Integer,ForeignKey('freshers_dev.items_table.id'),primary_key=True, index=True)
    item = Column(String)
    city = Column(String)
    cost = Column(String)

    items_table = relationship('Item', back_populates="owner")
from sqlalchemy import Column, Integer, String, DateTime,Text, Boolean,func
from db.base_class import Base
from sqlalchemy.orm import relationship


class ProductsModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name =Column(String, nullable=False, unique=True)
    bp =Column(Integer, nullable=False)
    sp =Column(Integer, nullable=False)
    
    slase = relationship("SalesModel", back_populates="prod")
    
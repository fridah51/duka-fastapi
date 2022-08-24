from sqlalchemy import Column, Integer, String, DateTime,Text, Boolean,func,ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class SalesModel(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    
    prod = relationship("ProductsModel", back_populates="slase")
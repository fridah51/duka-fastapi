from sqlalchemy import Column, Integer, String, Text,ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class StkModel(Base):
    __tablename__ = "stkmodel"
    id = Column(Integer, primary_key=True, index=True)
    merchantRequestID = Column(Integer, nullable=False)
    checkoutRequestID = Column(Integer, nullable=False)
    ResultCode = Column(Integer, nullable=False)
    ResultDesc = Column(String, nullable=False)
    Amount = Column(Integer, nullable=False)
    MpesaReceiptNumber = Column(String, nullable=False)
    Balance = Column(Integer, nullable=False)
    PhoneNumber = Column(Integer, nullable=False)
    TransactionDate = Column(String, nullable=False)
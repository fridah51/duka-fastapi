from datetime import datetime
from pydantic import BaseModel
from typing import Optional,List



class SalesBase(BaseModel): 
   quantity:int
   product_id:int
   
class SalesCreate(SalesBase):
    pass
   

class SalesPut(BaseModel):
    quantity:Optional[int]
    

class Sales(SalesBase):
    id:int
    product_id:int
    created:datetime
    
    class Config:
        orm_mode = True
    
    
#products schema sasa

class ProductsBase(BaseModel):  
    name:str
    bp:int
    sp:int
    

class ProductsCreate(ProductsBase):
    pass
   

class ProductsPut(BaseModel):
    name:Optional[str]
    bp:Optional[int]
    sp:Optional[int]
    

class Products(ProductsBase):
    id:int
    
    class Config:
        orm_mode = True
    
class ProductsInDb(Products):
    slase:List[Sales]
    
    class Config:
        orm_mode = True

class SalesInDb(SalesBase):
    id:int
    created:datetime
    prod:Products
    class Config:
        orm_mode = True



#stkpush schema sasa
class StkResponse(BaseModel):
    MerchantRequestID:int
    CheckoutRequestID: str
    ResponseCode: str
    ResponseDescription: str
    CustomerMessage: str


class StkRequestBody(BaseModel):
    BusinessShortCode: Optional[int] 
    Password: str
    Timestamp: str
    TransactionType: Optional[str] 
    Amount: int
    PartyA: int
    PartyB: int
    PhoneNumber: int
    CallBackURL: Optional[str] 
    AccountReference: Optional[str]
    TransactionDesc: Optional[str] 


class CallBackResponse():
    pass
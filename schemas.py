from datetime import datetime
from pydantic import BaseModel
from typing import Optional,List
import itertools


# id_iter = itertools.count()
#(next(id_iter))

class SalesBase(BaseModel): 
   quantity:int
   
   
class SalesCreate(SalesBase):
    product_id:int
   

class SalesPut(BaseModel):
    quantity:Optional[int]
    

class Sales(SalesBase):
    id:int
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
    
class ProductsInDb(ProductsBase):
    id:int
    slase:List[Sales]
    
    class Config:
        orm_mode = True

class SalesInDb(SalesBase):
    id:int
    created:datetime
    prod:Products
    class Config:
        orm_mode = True
from fastapi import APIRouter,Depends, HTTPException
from typing import List,Dict,Generator
from sqlalchemy.orm import Session


from db.session import SessionLocal
from models.sales import SalesModel
from models.inventory import ProductsModel
from schemas import Sales,SalesCreate,SalesInDb,SalesPut


sales_router = APIRouter()

#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




@sales_router.get("", 
summary="get a list of all todo items",
status_code=200,
response_model=List[Sales]
)
def sales(db:Session = Depends(get_db)):
   
    return db.query(SalesModel).all()



@sales_router.get("/{saleID}", 
response_model=SalesInDb,
summary="get a todo item",
status_code=200
)
def sale(saleID:int, db:Session = Depends(get_db)):
    
    tod = db.query(SalesModel).filter(SalesModel.id == saleID).first()
    prodID = db.query(ProductsModel).filter(ProductsModel.id == tod.product_id).first()
    
    if not prodID:
        raise HTTPException(status_code=401, detail=f"{prodID} :user id doesn't exists ")
    
    return tod


@sales_router.post("", 
response_model=Sales,
summary="make a sale",
status_code=201
)
def  post_sales( payload:SalesCreate, db:Session = Depends(get_db)):
    
    prodID = db.query(ProductsModel).filter(ProductsModel.id == payload.product_id).first()
    
    if not prodID:
        raise HTTPException(status_code=401, detail=f"{prodID} :product id doesn't exists ")
    
    res:Sales = SalesModel( quantity = payload.quantity, product_id = payload.product_id)
    db.add(res)
    db.commit()
    return res


@sales_router.put("/{saleID}", 
response_model=Sales,
summary="update a SALE",
status_code=200
)
def  update_sales(saleID:int, payload:SalesPut, db:Session = Depends(get_db)):
    item = db.query(SalesModel).filter(SalesModel.id == saleID).first()
    
    if not item:
        raise HTTPException(status_code=401, detail=f"{saleID} doesn't exists ")
    
    item.quantity = payload.quantity
    
    db.add(item)
    db.commit()
    
    return item


@sales_router.delete("/{saleID}", 
status_code=200,
summary="delete item",
response_model=Dict[str,str]
)
def  delete_sale(saleID:int, db:Session = Depends(get_db)):
    item = db.query(SalesModel).filter(SalesModel.id == saleID).first()
    db.delete(item)
    db.commit()
    
    return {"message":"saleID deleted"}
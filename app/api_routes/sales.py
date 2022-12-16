from fastapi import APIRouter,Depends, HTTPException
from typing import List,Dict,Generator
from sqlalchemy.orm import Session


from app.db.session import SessionLocal
from app.models.sales import SalesModel
from app.models.inventory import ProductsModel
from ..schemas import Sales,SalesCreate,SalesInDb,SalesPut,QtyPrice


sales_router = APIRouter()

#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close() #type: ignore




@sales_router.get("", 
summary="get a list of all sales",
status_code=200,
response_model=List[Sales]
)
def sales(db:Session = Depends(get_db)):
   
    return db.query(SalesModel).all()



@sales_router.get("/{saleID}", 
response_model=List[SalesInDb],
summary="get one sale",
status_code=200
)
def sale(saleID:int, db:Session = Depends(get_db)):
    
    sID = db.query(SalesModel).filter(SalesModel.id == saleID).all()
    
    if not sID:
        raise HTTPException(status_code=401, detail=f"{sID} : sale doesn't exists ")
    
    return sID


@sales_router.get("/s/{prodID}", 
response_model=List[SalesInDb],
summary="get one sale",
status_code=200
)
def salep(prodID:int, db:Session = Depends(get_db)):
    
    sID = db.query(SalesModel).filter(SalesModel.product_id == prodID).all()
    # all sales of one product
    if not sID:
        raise HTTPException(status_code=401, detail=f"{sID} : sale doesn't exists ")
    
    return sID



@sales_router.post("", 
response_model=SalesInDb,
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
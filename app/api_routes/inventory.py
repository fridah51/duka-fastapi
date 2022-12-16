from fastapi import APIRouter,Depends, HTTPException
from typing import List,Dict,Generator
from sqlalchemy.orm import Session


from ..schemas import Products,ProductsCreate,ProductsInDb,ProductsPut
from app.db.session import  SessionLocal
from app.models.inventory import ProductsModel


products_router = APIRouter()


#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()         #type:ignore




#get all products
@products_router.get("",
response_model=List[Products],
summary="all products",
status_code=200
)
def prods(db:Session= Depends(get_db)):
    return db.query(ProductsModel).all()


#get single product
@products_router.get("/{prodID}",
response_model=List[ProductsInDb],
summary="single product",
status_code=200
)
def prod(prodID:int, db:Session= Depends(get_db)):
    oneP = db.query(ProductsModel).filter(ProductsModel.id == prodID).first()
    if not oneP:
        raise HTTPException(status_code=401, detail=f"{prodID} doesn't exists ")
    return oneP


@products_router.post("",
response_model=ProductsInDb,
summary="create new product",
status_code=201
)
def prod_post(payload: ProductsCreate, db: Session= Depends(get_db)):
    # print ("payload", payload.dict())
    
    name = db.query(ProductsModel).filter(ProductsModel.name == payload.name).first()
    
    if name:
        raise HTTPException(status_code=400, detail=f"{payload.name} already exists ")
    # res:UsersInDb = UserModel(**dict())
    
    res:ProductsInDb = ProductsModel(name=payload.name, bp=payload.bp, sp=payload.sp)
    db.add(res)
    db.commit()
    return res


@products_router.put("/{prodID}",
summary="update a product",
status_code=200
)
def prod_put(prodID:int, payload:ProductsPut,  db:Session= Depends(get_db)):
    item = db.query(ProductsModel).filter(ProductsModel.id == prodID).first()
    
    if not item:
        raise HTTPException(status_code=401, detail=f"{prodID} doesn't exists ")
    
    item.name = payload.name
    item.bp= payload.bp,
    item.sp= payload.sp
    
    db.add(item)
    db.commit()
    return {"message":"item updated successfully"}



@products_router.delete("/{prodID}",
response_model=Dict[str,str],
summary="delete a product",
status_code=200
)
def prod_delete(prodID:int,  db:Session= Depends(get_db)):
    pay = db.query(ProductsModel).filter(ProductsModel.id == prodID).first()
    db.delete(pay)
    db.commit()
    return {"response":"item deleted successfully from db"}
from fastapi import FastAPI
from datetime import datetime
from typing import Dict, Generator, List
from fastapi.middleware.cors import CORSMiddleware



from db.base_class import *
from db.session import SessionLocal, engine
from models.inventory import ProductsModel
from models.sales import SalesModel

#create tables
Base.metadata.create_all(bind=engine)


#router
from api_routes.api import router

app = FastAPI(
    title="Duka API",
    description = "A basic duka api",
    version = "0.2.0",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[ "Accept: application/json; odata=nometadata" ],
)


app.include_router(router, responses={200:{"description":"Ok"}})


#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.get("/", 
summary="Home route",
status_code=200,
)
def home():
    
   return "Hello you!"


from fastapi import FastAPI
from datetime import datetime
from typing import Dict, Generator, List
from fastapi.middleware.cors import CORSMiddleware
import requests
from requests.auth import HTTPBasicAuth


from  app.db.base_class import Base
from  app.db.session import SessionLocal, engine
from  .models import inventory,sales,stkcallback

#create tables

Base.metadata.create_all(bind=engine)  # type: ignore


#router
from  app.api_routes.api import router

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
    allow_headers=["*"]
)


app.include_router(router, responses={200:{"description":"Ok"}})


#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()          # type: ignore



@app.get("/", 
summary="Home route",
status_code=200,
)
def home():
    
   return "Hello you!"



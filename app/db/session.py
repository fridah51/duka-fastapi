from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine("sqlite:///duka.db")
SessionLocal = sessionmaker(bind=engine, autocommit=False , autoflush=False)
conn = SessionLocal()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///duka.db")
SessionLocal = sessionmaker(bind=engine, autocommit=False , autoflush=False)
conn = SessionLocal()
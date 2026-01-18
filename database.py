
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "postgresql://postgres:Rohit%40123@localhost:5433/telusko"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
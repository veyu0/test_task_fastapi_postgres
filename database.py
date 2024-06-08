from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@localhost/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if Base:
    print("Base is working!")
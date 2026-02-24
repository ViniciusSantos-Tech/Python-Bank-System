from sqlalchemy import create_engine, String, Integer, Column, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()
url_bank = os.getenv("DATABASE_URL")

class Account(Base):
    __tablename__ = "BankAccounts"

    id =  Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String)
    gmail = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    balance = Column(Numeric)
    
engine = create_engine(url_bank)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


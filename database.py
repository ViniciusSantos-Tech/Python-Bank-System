from sqlalchemy import create_engine, String, Integer, Column, Numeric, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()
url_bank = os.getenv("DATABASE_URL")

class Account(Base):
    __tablename__ = "BankAccounts"
    __table_args__ = {"schema": "Bank"}

    id =  Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String)
    gmail = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    balance = Column(Numeric)

class Transactions(Base):
    __tablename__ = "History"
    __table_args__ = {"schema": "Bank"}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    account_id = Column(Integer, ForeignKey("Bank.BankAccounts.id", ondelete="CASCADE"), nullable=False)
    type = Column(String, nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    description = Column(String)

    
engine = create_engine(url_bank)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


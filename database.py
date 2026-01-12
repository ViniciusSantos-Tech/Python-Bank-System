import psycopg2
from sqlalchemy import create_engine, Integer, Column, String, Float, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base
import hashlib
from datetime import datetime, timezone

Base = declarative_base()
URL_BANK = "postgresql://postgres:211508@localhost:5432/postgres"



class Account(Base):
    """
    Represents a bank account within the Bank schema.

    Attributes:
        id (int): Primary key, auto-incremented.
        user (str): Username for the account holder.
        password (str): Hashed password string.
        cpf (str): Unique Brazilian tax ID.
        balance (Decimal): Current available funds, defaults to 100 FOR TESTS!.
    """
    __tablename__ = 'Accounts'
    __table_args__ = {'schema': 'Bank'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(255), nullable=False )
    password = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    balance = Column(Numeric(10, 2), default=100)

class Transactions(Base):
    """
    Records all financial movements linked to an Account.

    Attributes:
        id (int): Primary key, auto-incremented.
        account_id (int): Foreign key referencing Bank.Accounts.id.
        value (Decimal): The amount involved in the transaction.
        kind (str): The type of transaction (e.g., 'deposit', 'withdraw').
        date (datetime): Timestamp of the operation (UTC).
    """
    __tablename__ = 'Transactions'
    __table_args__ = {'schema': 'Bank'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey('Bank.Accounts.id'), nullable=False)
    value = Column(Numeric(10, 2), nullable=False )
    kind = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

def get_session():
    try:
        engine = create_engine(URL_BANK)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        raise
session = get_session()

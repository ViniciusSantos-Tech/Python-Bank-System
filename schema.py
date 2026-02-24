from pydantic import BaseModel
from decimal import Decimal

class UserCreate(BaseModel):
    full_name: str
    gmail: str
    cpf: str
    username: str
    password: str
class UserTransactions(BaseModel):
    destiny_cpf: str
    quantity: Decimal


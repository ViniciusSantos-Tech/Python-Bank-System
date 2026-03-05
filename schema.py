from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class UserCreate(BaseModel):
    full_name: str
    gmail: str
    cpf: str
    username: str
    password: str
class UserTransactions(BaseModel):
    destiny_cpf: str
    quantity: Decimal
    model_config = {
        "from_attributes": True
    }
class StandardResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
    

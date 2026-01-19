from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
from crud import Crud
from auth import gerar_token, SECRET_KEY, ALGORITHM
from jose import jwt

db = Crud()

app = FastAPI(
    title="Elite Secure Bank API",
    description="A secure banking API with JWT authentication and transaction protection.",
    version="1.1.0"
)
class Initial(BaseModel):
    """Schema for new user registration."""
    name: str
    password: str
    cpf: str
class Login(BaseModel):
    """Schema for user authentication credentials."""
    password: str = Field(min_length=5, max_length=10)
    cpf: str = Field(min_length=11, max_length=14)
class SendMoney(BaseModel):
    """Schema for transferring funds between accounts."""
    from_id: int
    to_id: int
    quantity: float

class ConfirmDelete(BaseModel):
    """Schema for identity verification before account deletion."""
    user: str
    password: str
@app.post("/accounts", tags=["Auth"])
def register_user(user: Initial):
    """
    Register a new user account in the system.
    Returns the registered name and unique ID.
    """
    mgs, new_id = db.create_account(user.name, user.cpf, user.password)
    if mgs == False:
        raise HTTPException(status_code=400, detail="User with this CPF already exists.")
    return {"Name": user.name, "Id": new_id}

@app.post("/login", tags=["Auth"])
def login_user(user: Login):
    """
    Authenticate user and return a JWT Access Token.
    The token is required for all sensitive operations.
    """
    user_db = db.login(user.password, user.cpf)
    if not user_db:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    token = gerar_token(user_db.id)
    return {"access_token": token, "token_type": "bearer"}

@app.post("/transactions", tags=["Banking"])
def send_money_route(user: SendMoney, token: str = Header(None)):
    """
    Transfer funds between accounts. 
    Requires a valid token matching the sender's ID (from_id).
    """
    if not token:
        raise HTTPException(status_code=401, detail="Missing authentication token.")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        tokenid = payload.get("user_id")
    except Exception:
        raise HTTPException(status_code=401, detail="Token is invalid or expired.")

    if tokenid != user.from_id:
        raise HTTPException(status_code=403, detail="Forbidden: You cannot transfer from another user's ID.")

    success = db.send_money(user.from_id, user.to_id, user.quantity)
    if not success:
        raise HTTPException(status_code=400, detail="Transaction failed: Insufficient balance or invalid destination.")
    return {"status": "success", "message": "Transfer completed."}

@app.get("/History/{user_id}", tags=["Banking"])
def history(user_id: int, token: str = Header(None)):
    """
    Retrieve transaction history for a specific account.
    Requires a valid token matching the requested user_id.
    """
    if not token:
        raise HTTPException(status_code=401, detail="Authentication token required.")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        tokenid = payload.get("user_id")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token.")

    if tokenid != user_id:
        raise HTTPException(status_code=403, detail="Forbidden: Access denied to other user's history.")

    extract = db.get_history(user_id)
    if not extract:
        return {"msg": "No transactions found."}
    return extract

@app.delete("/Delete/{user_id}", tags=["Admin"])
def delete_account(user: ConfirmDelete, user_id: int):
    """
    Permanently delete an account and its history.
    Verification of username and password is required.
    """
    success = db.delete(user.user, user.password, user_id)
    if not success:
        raise HTTPException(status_code=401, detail="Invalid credentials or account not found.")
    return {'Status': 'Account deleted successfully'}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import Account
from datetime import date
from crud import Crud

db = Crud()

app = FastAPI()
class Initial(BaseModel):
    """Schema for new user registration."""
    name: str
    password: str
    cpf: str

@app.post("/accounts")
def register_user(user: Initial):
    """
    Register a new user account in the Bank Table.
    
    Returns:
        dict: The registered username and the newly generated unique ID.
    Raises:
        HTTPException: 400 if the user (CPF) already exists.
    """
   
    mgs, new_id = db.create_account(user.name, user.cpf, user.password)
    if mgs == False:
        raise HTTPException(status_code=400, detail="Existing user")
    else:
        return {"Name": user.name, "Id": new_id }
    
class Login(BaseModel):
    """Schema for user authentication credentials."""
    password: str = Field(min_length=5, max_length=10)
    cpf: str = Field(min_length=11, max_length=14)
@app.post("/login")
def login_user(user: Login):
    """
    Authenticate a user and grant access.
    
    Returns:
        dict: Status login successfully if credentials are valid.
    Raises:
        HTTPException: 401 if credentials do not match any record.
    """
    response = db.login( user.password, user.cpf )
    if response == False:
        raise HTTPException(status_code=401, detail="Usuario ou senha invalidos")
    else:
        return {"Status": "login successfully"}
    
class SendMoney(BaseModel):
    """Schema for transferring funds between accounts."""
    from_id: int
    to_id: int
    quantity: float
@app.post("/transactions")
def Send(user: SendMoney):
    """
    Transfer money from one account to another.
    Returns:
        dict: Status 200 on successful transfer.
    Raises:
        HTTPException: 400 if the sender has insufficient balance.
    """
    response = db.send_money(user.from_id, user.to_id, user.quantity)
    if response:
        return {"Status": 200}
    raise HTTPException(status_code=400, detail="Saldo insuficente")

class ConfirmDelete(BaseModel):
    """Schema for identity verification before account deletion."""
    user: str
    password: str
@app.delete("/Delete/{user_id}")
def Delet_account(user: ConfirmDelete, user_id: int):
    """
    Permanently delete a user account after verification.
    
    Args:
        user_id (int): The ID of the account to be deleted.
    Returns:
        dict: Account deleted successfully
    """
    sucess = db.delete(user.user, user.password, user_id)
    if not sucess:
        raise HTTPException(status_code=401, detail="Invalid credentials or account not found")
    return {'Status': 'Account deleted successfully'}

@app.get("/History/{user_id}")
def history(user_id: int):
    """
    Retrieve the complete transaction history for a specific user.
    
    Returns:
        list: A list of transactions or a message if none are found.
    """
    extract = db.get_history(user_id)
    if not extract:
        return {"msg": "No transfer found or user does not exist."}
    return extract

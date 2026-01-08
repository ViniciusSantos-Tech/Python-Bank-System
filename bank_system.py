from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import DataBase
from datetime import date

db = DataBase()

app = FastAPI()
class Initial(BaseModel):
    Name: str
    password: str
    cpf: str
@app.post("/Register")
def register_user(user: Initial):
    '''Function of the procedure to create and register a new account.'''
    mgs, new_id = db.Register(user.Name, user.password, user.cpf)
    if mgs == False:
        raise HTTPException(status_code=400, detail="Existing user")
    else:
        return {"Name": user.Name, "Password": user.password, "Id": new_id }
    
class Login(BaseModel):
    Name: str
    password: str = Field(min_length=5, max_length=10)
    cpf: str = Field(min_length=11, max_length=11)
@app.post("/Login")
def login_user(user: Login):
    '''Função para efetuar login utilizando HTTPException.'''
    response = db.Login(user.Name, user.password, user.cpf )
    if response == False:
        raise HTTPException(status_code=401, detail="Usuario ou senha invalidos")
    else:
        return {"Status": 200}
class SendMoney(BaseModel):
    from_id: int
    to_id: int
    quantity: float

@app.post("/Send")
def Send(user: SendMoney):
    '''function to register using the database method'''
    response = db.SendMoney(user.from_id, user.to_id, user.quantity)
    if response:
        return {"Status": 200}
    raise HTTPException(status_code=400, detail="Saldo insuficente")

@app.get("/History/{id_user}")
def History(id_user: int):
    '''Function to display payment history using the database method.'''
    response = db.history(id_user)
    return {"History": response}

class ConfirmDelete(BaseModel):
    user: str
    password: str
@app.delete("/Delete/{user_id}")
def Delet_account(user: ConfirmDelete, user_id: int):
    '''Function to delete an account using database methods.'''
    response = db.Delet(user.user, user.password, user_id)
    return response

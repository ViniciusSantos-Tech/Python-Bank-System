from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import DataBase
from datetime import date

db = DataBase()


app = FastAPI()
class Initial(BaseModel):
    Name: str
    password: str
@app.post("/Register")
def Register(user: Initial):
    new_id = db.Register(user.Name, user.password, 0)
    return {"Name": user.Name, "Password": user.password, "Id": new_id }
class Login(BaseModel):
    Name: str
    password: str
@app.post("/Login")
def Login(user: Login):
    response = db.Login(user.Name, user.password )
    if response:
        return {"Status": 200}
    raise HTTPException(status_code=401, detail="Usuario ou senha invalidos")
class SendMoney(BaseModel):
    from_id: int
    to_id: int
    quantity: float
@app.post("/Send")
def Send(user: SendMoney):
    response = db.Enviar(user.from_id, user.to_id, user.quantity)
    if response:
        return {"Status": 200}
    raise HTTPException(status_code=400, detail="Saldo insuficente")
@app.get("/History/{id_user}")
def History(id_user: int):
    response = db.history(id_user)
    return {"History": response}

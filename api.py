from fastapi import FastAPI
from codify import hashpsswd
from schema import UserCreate, UserTransactions, StandardResponse
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from crud import create_user, loginapp, send_money, deleteuser, history
from auth import create_token
import bank
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import SECRET_KEY 
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def user_logged(token: str = Depends(oauth2_scheme)) -> list:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload 
    except:
        raise HTTPException(status_code=401, detail="Token inválido")

#-------------
def get_db():
    db = bank.SessionLocal()
    try:
        yield db
    finally:
        db.close()
#--------------
app = FastAPI(
    title="Bank API",
    swagger_ui_parameters={"deepLinking": False}
)

@app.post("/register", tags=["Authentication"], response_model=StandardResponse)
def regsiter_user(userdata: UserCreate, db: Session = Depends(get_db)):
    full_name = userdata.full_name
    gmail = userdata.gmail
    cpf = userdata.cpf
    username = userdata.username
    password = userdata.password
    try:
        security_password = hashpsswd(password)
        response, message = create_user(db=db, full_name=full_name, gmail=gmail,
                    cpf=cpf, username=username, security_password=security_password)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Data already registered!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")

    return StandardResponse(
        success=response,
        message=message,
        data=None
    )
@app.post("/login", tags=["Authentication"])
def login(userdata: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) ->dict:
    cpf = userdata.username
    password = userdata.password
    verify, user, userid = loginapp(db=db, cpf=cpf, password=password)
    if not verify:
        raise HTTPException(status_code=401, detail="Incorrect password or CPF ")
    token = create_token(user_id=userid, user=user)
    return {"access_token": token, "token_type": "bearer"}
@app.post("/transactions", tags=["Banking"], response_model=StandardResponse)
def transaction(userdata: UserTransactions, db: Session = Depends(get_db), token_data = Depends(user_logged)):
    my_id = token_data.get("sub")
    code, response = send_money(db=db, destiny_cpf=userdata.destiny_cpf, own_id=my_id, quantity=userdata.quantity)
    return StandardResponse(
        success=code,
        message=response,
        data=None
    )
@app.delete("/deleteaccount", tags=["Delete"], response_model=StandardResponse)
def deletaccount(token_data = Depends(user_logged), db: Session = Depends(get_db)):
    my_id = token_data.get("sub")
    status, msg = deleteuser(db=db, user_id=my_id)
    if status == False:
        return msg
    return StandardResponse(
        success=status,
        message=msg,
        data=None
    )

@app.get("/statement", tags=["Banking"], response_model=StandardResponse)
def get_history(token_data = Depends(user_logged), db: Session = Depends(get_db)):
    my_id = token_data.get("sub")
    cleaned_data = history(db=db, user_id=my_id)
    
    return StandardResponse(
        success=True,
        message="History",
        data={"transactions": cleaned_data}
    )

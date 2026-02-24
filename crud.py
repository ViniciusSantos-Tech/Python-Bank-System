from sqlalchemy.orm import Session
from bank import Account
from codify import verifyc
from decimal import Decimal

def create_user(db: Session, full_name, gmail, cpf, username, security_password):
    db_user = Account(
        full_name=full_name,
        gmail=gmail,
        cpf=cpf,
        username=username,
        hashed_password=security_password,
        balance=100
 
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def loginapp(db: Session, cpf: str, password: str):
    user = db.query(Account).filter_by(cpf=cpf).first()
    security_password = verifyc(password, user.hashed_password)
    return security_password, user.username, user.id

def send_money(db: Session, destiny_cpf:str, quantity: Decimal, own_id):
    user = db.query(Account).filter_by(cpf=destiny_cpf).with_for_update().first()
    user2 = db.query(Account).filter_by(id=own_id).with_for_update().first()
    if not user:
        return False, "user does not exist"
    if destiny_cpf == user2.cpf:
        return False, "You can't send it to yourself."
    if quantity == 0:
        return False,  "Error"

    if user2.balance > quantity:
        try:
            user.balance += quantity
            user2.balance -= quantity
            db.commit()
            return True, "Sucess"
        except Exception as e:
            db.rollback()
            return False, f"Error: {e}"



from sqlalchemy import delete, desc
from sqlalchemy.orm import Session
from bank import Account, Transactions
from codify import verifyc
from decimal import Decimal
from typing import Union

def create_user(db: Session, full_name, gmail, cpf, username, security_password):
    try:
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
        return True, "Account Created"
    except Exception as e:
        return False, str(e)

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

    if user2.balance >= quantity:
        try:
            user.balance += quantity
            user2.balance -= quantity
            history_sender = Transactions(
                account_id=user.id,
                type="transfer_out",
                amount=-quantity,
                description=f"sended to: {user2.full_name}"

            )
            history_destiny = Transactions(
            account_id=user2.id,
            type="transfer_in",
            amount=quantity,
            description=f"Received from {user.full_name}"
            )

            db.add(history_sender)
            db.add(history_destiny)
            db.commit()

            return True, "Sucess"
        except Exception as e:
            db.rollback()
            return False, f"Error: {e}"
        
def deleteuser(db: Session, user_id: str) -> Union[bool, str, tuple]:
    try:
        stmt = delete(Account).where(Account.id == user_id)
        response = db.execute(stmt)
        count = response.rowcount
        db.commit()
        if count == 0:
            return False, {"success": True, "message": "Account Deleted", "data": None}
        
        return True, {"msg": "Account Deleted"}
    except Exception as e:
        return False, e
    
def history(db: Session, user_id: str) -> str:
    try:
        transactions = (db.query(Transactions).filter(Transactions.account_id == user_id)
            .order_by(desc(Transactions.created_at))
            .limit(10)
            .all()
        )
        if not history:
            return []
        return [
            {
                "id": t.id,
                "tipo": t.type,
                "valor": float(t.amount),
                "descricao": t.description,
                "data": t.created_at.strftime("%d/%m/%Y %H:%M")
            } for t in transactions
        ]
    except Exception as e:
        return e

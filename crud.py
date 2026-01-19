from database import Account, session, Transactions
import hashlib
from decimal import Decimal

class Crud():
    def __init__(self):
        self.db = session

    def generate_hash(self, password):
        """
        Hashes a raw password string using the SHA-256 algorithm.
        """
        return hashlib.sha256(str(password).encode()).hexdigest()
    
    def create_account(self, user, cpf, password):
        """
        Creates a new bank account if the CPF is not already registered.
        """
        try:
            security_password = self.generate_hash(password)
            exists_user = self.db.query(Account).filter_by(cpf=cpf).first()
            if exists_user:
                return False, None
            
            new_account = Account(user=user, cpf=cpf, password=security_password)
            self.db.add(new_account)
            self.db.commit()
            self.db.refresh(new_account)
        except Exception as e:
            return {"Error": e}
        return True, new_account.id

    def login(self, password, cpf):
        """
        Authenticates a user by checking CPF and hashed password.
        """
        security_password = self.generate_hash(password)
        exists_user = self.db.query(Account).filter_by(password=security_password, cpf=cpf).first()
        if exists_user:
            return exists_user
    def send_money(self, from_id, to_id, value):
        '''
        Function to transfer funds between two accounts
        '''
        try:
            From = self.db.query(Account).filter_by(id=from_id).first()
            To = self.db.query(Account).filter_by(id=to_id).first()
            value_decimal = Decimal(str(value))
            if From and To and From.id != To.id and From.balance >= value:
                From.balance -= value_decimal
                To.balance += value_decimal
                h_send = Transactions(account_id=From.id, value=value, kind='Send')
                h_receive = Transactions(account_id=To.id, value=value, kind='Receive')
                self.db.add(h_send)
                self.db.add(h_receive)
                self.db.commit()
                return True
        except Exception as e:
            return {'Error': e}
        return False
    
    def delete(self, user, password, id):
        """
        Deletes an account and its transaction history after verifying credentials.
        """
        security_password = self.generate_hash(password)
        account = self.db.query(Account).filter_by(user=user, password=security_password, id=id).first()
        if account:
            try:
                self.db.query(Transactions).filter_by(account_id=id).delete()
                self.db.delete(account)
                self.db.commit()
                return True
            except Exception as e:
                self.db.rollback()
                print(f"Error: {e}")
            return False
        return False
        
    def get_history(self, user_id):
        '''Fetches all transaction records associated with a specific user ID.'''
        return self.db.query(Transactions).filter_by(account_id=user_id).all()

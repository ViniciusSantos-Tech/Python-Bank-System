import sqlite3
from datetime import datetime
import hashlib

class DataBase():
    def __init__(self):
        self.database = "Bankdb.db"
        self.conection()
    def conection(self):
        '''A function to create the main database and its tables.'''
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Bank_accounts(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user TEXT NOT NULL,
                            password TEXT,
                            cpf TEXT UNIQUE NOT NULL,
                            balance FLOAT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS history(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       from_id INT,
                       to_id INT,
                       date TEXT,
                       quantity INT)""")
        conn.commit()
        conn.close()
    def generate_hash(self, password):
        return hashlib.sha256(str(password).encode()).hexdigest()
    def Register(self, name, password, cpf):
        
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            security_password = self.generate_hash(password)
            cursor.execute("INSERT INTO Bank_accounts(user, password, balance, cpf) VALUES (?, ?, ?, ?)", (name, security_password, 100, cpf))
            id_logged = cursor.lastrowid
            conn.commit()
            return True, id_logged
        except sqlite3.IntegrityError:
            return False, 'Existing user'
        finally:
            conn.close()
    def Login(self, name, password, cpf):
        '''Esta função foi criada para receber argumentos da API para a criação de novas contas.'''
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        security_password = self.generate_hash(password)
        cursor.execute("SELECT id, user, password FROM Bank_accounts WHERE user = ? AND password = ? AND cpf = ?", (name, security_password, cpf))
        response = cursor.fetchone()
        if response:
            return response
        else:
            return False
    def SendMoney(self, from_id, to_id, quantity):
        '''This function was created to send money.'''
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            sender = cursor.execute("SELECT balance FROM Bank_accounts WHERE id = ?", (from_id,))
            balance = cursor.fetchone()[0]
            if quantity > balance or from_id == to_id:
                conn.close()
                return False
            cursor.execute("SELECT id FROM Bank_accounts WHERE id = ?", (to_id,))
            response = cursor.fetchone()
            if response == None:
                conn.close()
                return False
            else:
                cursor.execute("UPDATE Bank_accounts SET balance = balance - ? WHERE id = ? ", (quantity, from_id))
                cursor.execute("UPDATE Bank_accounts SET balance = balance + ? WHERE id = ? ", (quantity, to_id))
                date_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                cursor.execute("INSERT INTO history(from_id, to_id, date, quantity) VALUES (?, ?, ?, ?)", (from_id, to_id, date_now, quantity))
                conn.commit()
                conn.close()
                return True
        finally:
            conn.close()
    def history(self, id_user):
        '''Function to display payment history. 
        This function returns a clean dictionary.'''
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM history WHERE from_id = ? OR to_id = ?", (id_user,id_user))
            lines = cursor.fetchall()
            conn.close()
            result = []
            for line in lines:
                result.append({
                "Sent": line[1],
                "Received": line[2],
                "Date": line[3],
                "Quantity": line[4]})
            conn.close()
            return result
        except Exception as e:
            print (e)
            return False
    def Delet(self, name, password, user_id):
        '''This function was created to delete accounts and their history,
        preventing the database from becoming disorganized.'''

        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        security_password = self.generate_hash(password)
        cursor.execute("SELECT password FROM Bank_accounts WHERE user = ? AND password = ?", (name, security_password))
        response = cursor.fetchone()
        if response == None:
            conn.close()
            return False
        else:
            cursor.execute("DELETE FROM history WHERE from_id = ? OR to_id = ?", (user_id, user_id))
            cursor.execute("DELETE FROM Bank_accounts WHERE id = ?", (user_id,))
            conn.commit()
            conn.close()
            return True

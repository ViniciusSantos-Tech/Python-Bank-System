import sqlite3
from datetime import datetime

class DataBase():
    def __init__(self):
        self.database = "Bankdb.db"
        self.conection()
    def conection(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Bank_accounts(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user TEXT,
                            password TEXT,
                            balance FLOAT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS history(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       from_id INT,
                       to_id INT,
                       date TEXT,
                       quantity INT)""")
        conn.commit()
        conn.close()
    def Register(self, name, password, balance):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Bank_accounts(user, password, balance) VALUES (?, ?, ?)", (name, password, 100))
        id_logged = cursor.lastrowid
        conn.commit()
        conn.close()
        return id_logged
    def Login(self, name, password):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT id, user FROM Bank_accounts WHERE user = ? AND password = ? ", (name, password))
        response = cursor.fetchone()
        conn.close()
        return response
    def Enviar(self, from_id, to_id, quantity):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        sender = cursor.execute("SELECT balance FROM Bank_accounts WHERE id = ?", (from_id,))
        balance = cursor.fetchone()[0]
        if quantity > balance:
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
    def history(self, id_user):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM history WHERE from_id = ? OR to_id = ?", (id_user,id_user))
        lines = cursor.fetchall()
        conn.close()
        result = []
        for line in lines:
            result.append({""
            "Sent": line[1],
            "Received": line[2],
            "Date": line[3],
            "Quantity": line[4]})
        return result

            
        



    

        
        



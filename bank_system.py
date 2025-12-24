#MADE BY VINICIUS SANTOS-TECH❤️
#Python Bank System

import sqlite3
from time import sleep

class Bank:
    def __init__(self, balance):
        
        self.balance = balance
        self.conection = sqlite3.connect("Bank.db")
        self.cursor = self.conection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS bank_accounts(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL,
               balance  FLOAT NULL,
               cpf TEXT NOT NULL UNIQUE
               )''')
        pass
    def login(self):
        '''User login function that stores data in the database.'''
        self.User = input("Hey! welcome to the login page. first, we need you enter your username: ")
        self.Pasword = input("Now, create yout password: ")
        self.Cpf = input("Enter your CPF(!!fictitious number!!): ")
        self.cursor.execute("""INSERT OR IGNORE INTO bank_accounts
                    (titular, balance, cpf) VALUES (?, ?, ?)
                    """, (self.User, self.balance, self.Cpf))
        self.conection.commit()
        sleep(3)
        pass
    def withdraw(self):
        '''This function processes user withdrawals and updates the balance.'''
        if self.value1 > self.balance:
            print("The amount of your funds is insufficient!")
        else:
            self.balance -= self.value1
            self.cursor.execute("""UPDATE bank_accounts SET balance = ? WHERE cpf = ? """, (self.balance, self.Cpf))
            self.conection.commit()
            print("✅| withdrawal made!")
            print("="* 10 )

    def deposit(self):
        '''This function processes user deposits and updates the balance.'''
        self.balance += self.value2
        self.cursor.execute("""UPDATE bank_accounts SET balance = ? WHERE cpf = ?""", (self.balance, self.Cpf))
        self.conection.commit()
        print("✅| Amount deposited successfully.")
        print("="* 10 )


    def front(self):
        '''Displays the bank's interactive menu
          and manages user options (Balance, Withdrawal, or Deposit) in a continuous loop.'''
        print("---Menu---")
        print(f"Hey, {self.User}! Welcome to your bank!")
        while True:
            self.choose = int(input("Enter 1 for see your Balance, 2 for withdraw and 3 for deposit: "))
            if self.choose == 1:
                print(f'💰 Balance: U${self.balance}')
                pass
            
            elif self.choose == 2:
                self.value1 = float(input("Now choose the quantity that you want withdraw: "))
                self.withdraw()
                pass
            elif self.choose == 3:
                self.value2 = float(input("Now choose the quantity that you want deposit: "))
                self.deposit()
                pass
            else:
                print("Error! Just put 1 or 2 or 3!:")

    def activate(self):
        '''The bank's workflow begins: first the login, then the main menu.'''
        self.login()
        self.front()

ac = Bank(100)
ac.activate()

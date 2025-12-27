#MADE BY VINICIUS SANTOS-TECH❤️
#Python Bank System
import sqlite3
import streamlit as st
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Bank.db")
connection = sqlite3.connect(db_path, check_same_thread=False)

if "page" not in st.session_state:
    st.session_state.page = "bank"

class Bank:
    """Class responsible for handling bank database operations like balance lookup, withdrawals, and deposits."""
    
    def __init__(self, connection):
        """Initializes the bank logic with a database connection and cursor."""
        self.connection = connection
        self.cursor = self.connection.cursor()

    def get_user_data(self, name):
        """Retrieves the balance and CPF of a specific user by their name."""
        self.cursor.execute("SELECT balance, cpf FROM bank_accounts WHERE titular = ?", (name,))
        return self.cursor.fetchone()

    def withdraw(self, amount, current_balance, cpf):
        """Validates and processes a cash withdrawal, updating the database if funds are available."""
        if amount > current_balance:
            st.error("Insufficient funds!")
        else:
            new_balance = current_balance - amount
            self.cursor.execute("UPDATE bank_accounts SET balance = ? WHERE cpf = ?", (new_balance, cpf))
            self.connection.commit()
            st.success(f"Withdrawal of ${amount:.2f} successful!")
            st.rerun()

    def deposit(self, amount, current_balance, cpf):
        """Processes a cash deposit and updates the user's balance in the database."""
        new_balance = current_balance + amount
        self.cursor.execute("UPDATE bank_accounts SET balance = ? WHERE cpf = ?", (new_balance, cpf))
        self.connection.commit()
        st.success(f"Deposit of ${amount:.2f} successful!")
        st.rerun()

class BankApp:
    """Class responsible for rendering the Streamlit user interface and managing navigation."""
    
    def __init__(self):
        """Initializes the app interface and connects it to the Bank logic."""
        self.logic = Bank(connection)

    def login_screen(self):
        """Renders the login form and validates user credentials against the database."""
        st.title("🏦 Vinícius Tech Bank")
        name = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            self.logic.cursor.execute("SELECT titular FROM bank_accounts WHERE titular = ? AND senha = ?", (name, password))
            if self.logic.cursor.fetchone():
                st.session_state.logged_in = True
                st.session_state.username = name
                st.rerun()
            else:
                st.error("Invalid credentials")

    def main_screen(self):
        """Renders the main dashboard, including navigation sidebar, balance display, and transaction forms."""
        # Sidebar Buttons
        if st.sidebar.button("Home"):
            st.session_state.page = "bank"
            st.rerun()
        if st.sidebar.button("About Project"):
            st.session_state.page = "about"
            st.rerun()
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

        if st.session_state.page == "bank":
            username = st.session_state.username
            data = self.logic.get_user_data(username)
            if data:
                balance, cpf = data
                st.title(f"Welcome back, {username}!")
                st.metric("Current Balance", f"$ {balance:.2f}")
                st.divider()
                
                col1, col2 = st.columns(2)
                with col1:
                    w_amount = st.number_input("Withdraw amount:", min_value=0.0, key="w")
                    if st.button("Confirm Withdrawal"):
                        self.logic.withdraw(w_amount, balance, cpf)
                with col2:
                    d_amount = st.number_input("Deposit amount:", min_value=0.0, key="d")
                    if st.button("Confirm Deposit"):
                        self.logic.deposit(d_amount, balance, cpf)
        
        elif st.session_state.page == "about":
            st.title("📖 About the Project")
            st.header("This project was developed by Vinícius Santos-Tech.")
            st.write('''This is a **study project** focused on mastering Python, SQLite, and Streamlit. 
                I am currently working hard on it to implement new features and improve the code structure.''')
            st.divider()
            st.markdown("<img src='https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif' width='100%'>", unsafe_allow_html=True)
            st.markdown("""
            ### 🔵 Project Purpose
            This application is a **full-stack study project** developed to bridge the gap between 
            theoretical Python concepts and real-world implementation. The goal was to build a 
            secure, functional, and intuitive banking interface that handles persistent data.

            ### 🛠️ The Tech Behind the Scenes
            I chose this specific stack to master the fundamentals of modern software development:
            - **Python & OOP:** The entire logic is built using **Object-Oriented Programming**, 
              ensuring the code is modular, reusable, and easy to maintain.
            - **SQLite3:** Instead of temporary variables, I'm using a relational database to 
              ensure that user balances and credentials are saved securely.
            - **Streamlit:** A powerful framework used to transform Python scripts into 
              interactive web applications.

            ### 🔵 My Learning Journey
            Currently, I am working intensely on this project to evolve it from a simple 
            prototype to a robust system. 
            
            **What I've mastered so far:**
            - Managing **Session States** to create a seamless user experience.
            - Implementing **CRUD operations** (Create, Read, Update, Delete) via SQL.
            - Designing a clean **User Interface (UI)** with real-time feedback and animations.""")
                        
            st.markdown("<img src='https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif' width='100%'>", unsafe_allow_html=True)
            
            st.markdown("""### 📅 What's Coming Next? (Roadmap)
            I believe that a project is never truly finished. My next steps are:
            1. **Transaction Logs:** A full history of every cent that moves in the account.
            2. **Password Hashing:** Adding a layer of professional security to the database.
            3. **Account Transfers:** Enabling users to send money to each other.""")
            st.subheader("🛠️ Current Goals")
            st.write("- [x] User Login System")
            st.write("- [x] Database Integration (SQLite)")
            st.write("- [ ] Transaction History (Coming Soon)")
            st.write("- [ ] Enhanced Security (Password Hashing)")
            st.success("Developed with ❤️ by **Vinícius Santos-Tech**")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

app = BankApp()

if st.session_state.logged_in:
    app.main_screen()
else:
    app.login_screen()

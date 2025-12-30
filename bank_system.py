# MADE BY VINICIUS SANTOS-TECH ❤️
# Python Bank System

import sqlite3
import streamlit as st
from time import sleep

connection = sqlite3.connect('bank.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS bank_accounts(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titular TEXT,
               password TEXT,
               cpf INTEGER UNIQUE,
               balance FLOAT)""")
connection.commit()

class Register:
    """Class responsible for creating new user accounts."""
    def create_account(self, name, password, cpf, initial_balance=0.0):
        try:
            cursor.execute("SELECT id FROM bank_accounts WHERE cpf = ?", (cpf,))
            if cursor.fetchone():
                return "Error! CPF already registered."
            
            cursor.execute("""
                INSERT INTO bank_accounts (titular, password, cpf, balance) 
                VALUES (?, ?, ?, ?)
            """, (name, password, cpf, initial_balance))
            
            connection.commit()
            return "Account created successfully!"
        except Exception as e:
            return f"An error occurred: {e}"

class Login:
    """Class responsible for handling user authentication."""
    def validate_credentials(self, user, password):
        if user and password:
            cursor.execute("SELECT titular FROM bank_accounts WHERE titular = ? AND password = ?", (user, password))
            response = cursor.fetchone()
            if response:
                return response[0]
        return None

class Bank:
    """Class representing the banking operations for a logged-in user."""
    def __init__(self, logged_user):
        self.user = logged_user
        cursor.execute("SELECT balance FROM bank_accounts WHERE titular = ?", (self.user,))
        self.balance = cursor.fetchone()[0]

    def send_money(self, key, quantity):
        if quantity > self.balance:
            return "Error! Insufficient funds"
        else:
            cursor.execute("SELECT id FROM bank_accounts WHERE id = ?", (key,))
            if cursor.fetchone() is None:
                return "Error! Key not found"
            else:
                cursor.execute("UPDATE bank_accounts SET balance = balance - ? WHERE titular = ?", (quantity, self.user))
                cursor.execute("UPDATE bank_accounts SET balance = balance + ? WHERE id = ?", (quantity, key))
                connection.commit()
                self.balance -= quantity
                return "Money sent successfully!"

st.set_page_config(page_title="My Python Bank")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "bank"
if "register_mode" not in st.session_state:
    st.session_state.register_mode = False

if not st.session_state.logged_in:
    if st.session_state.register_mode:
        st.title("📝 Register New Account")
        new_user = st.text_input("Full Name")
        new_pass = st.text_input("Choose a Password", type="password")
        new_cpf = st.number_input("CPF (Numbers only)", step=1, value=0)
        
        if st.button("Confirm Registration"):
            reg = Register()
            msg = reg.create_account(new_user, new_pass, new_cpf, initial_balance=100.0)
            if "successfully" in msg:
                st.success(msg)
                sleep(1)
                st.session_state.register_mode = False
                st.rerun()
            else:
                st.error(msg)
        
        if st.button("Already have an account? Login"):
            st.session_state.register_mode = False
            st.rerun()
    
    else:
        st.title("🏦 Banking Login")
        user_input = st.text_input("Username")
        pass_input = st.text_input("Password", type="password")

        col1, col2 = st.columns([0.2, 1])
        with col1:
            if st.button("Login"):
                app_login = Login()
                result = app_login.validate_credentials(user_input, pass_input)
                if result:
                    st.session_state.user = result
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        
        with col2:
            if st.button("Don't have an account? Sign up"):
                st.session_state.register_mode = True
                st.rerun()

else:
    app_bank = Bank(st.session_state.user)
    with st.expander("🛠️ TEST INSTRUMENTS (Read this to test)"):
        st.write("""
        To visualize how the system works and see the balance changing:
        
        1. **Option A (Quick Test):** Logout and login with the test user:
           - **Username:** `Marcus`
           - **Password:** `21345`
           - Use the 'Send Money' tab to send an amount to your own ID.
           
        2. **Option B (Recommended):** Use the **Register** screen to create a second account. 
           This way, you can simulate a real transfer between two users created by you!
        
        *Don't forget to check your ID in the 'My Key' tab before switching accounts!*
        """)

    st.sidebar.title(f"Welcome, {app_bank.user}!")
    if st.sidebar.button("Home"):
        st.session_state.page = "bank"
        st.rerun()
    if st.sidebar.button("About"):
        st.session_state.page = "about"
        st.rerun()
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    if st.session_state.page == "about":
        st.title("About the Project")
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
        st.subheader("🛠️ Current Goals")
        st.write("- [x] User Login System")
        st.write("- [x] Database Integration (SQLite)")
        st.write("- [ ] Transaction History (Coming Soon)")
        st.write("- [ ] Enhanced Security (Password Hashing)")
        st.success("Developed with ❤️ by **Vinícius Santos-Tech**")
    
    else:
        st.title(f"Current Balance: $ {app_bank.balance:.2f}")
        tab1, tab2 = st.tabs(["Send Money", "My Key"])

        with tab1:
            dest_key = st.number_input("Recipient ID (Key)", step=1)
            send_value = st.number_input("Amount to send", min_value=0.0)
            if st.button("Confirm Transfer"):
                msg = app_bank.send_money(dest_key, send_value)
                if "success" in msg.lower():
                    st.success(msg)
                    st.balloons()
                    sleep(1)
                    st.rerun()
                else:
                    st.error(msg)

        with tab2:
            cursor.execute("SELECT id FROM bank_accounts WHERE titular = ?", (app_bank.user,))
            my_id = cursor.fetchone()[0]
            st.info(f"Your key to receive deposits is: {my_id}")

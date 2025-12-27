# $${\color{blue}\text{🏦 Python Bank System (Streamlit Edition)}}$$
### A modern, interactive, and secure **web banking application** built with Python, SQLite, and Streamlit.  
This project showcases the evolution from a CLI system to a **full interactive web interface**, focusing on **OOP**, **database persistence**, and **state management**.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

---

## 🚀 Features

- **User Authentication System**
  - Secure login with username and password
  - Session-based authentication using Streamlit Session State

- **Real-time Banking Operations**
  - 💰 Deposits and withdrawals with instant balance updates
  - 📊 Live balance display using Streamlit metrics

- **Persistent Database**
  - All user data is stored in a local **SQLite (`Bank.db`)** database
  - Data remains intact even after closing the application

- **Interactive Web Interface**
  - Sidebar navigation (Home, About Project, Logout)
  - Clean layout with columns, dividers, and visual feedback
  - Success and error alerts for every transaction

- **Security-Oriented SQL**
  - Uses **SQL parameterized queries (`?`)** to prevent SQL Injection

> [!NOTE]
> This project is under **active development**.  
> New features and security improvements are continuously being added 🚀

---

## 🛠️ Technologies Used

- **Language:** Python 3.x  
- **Web Framework:** Streamlit  
- **Database:** SQLite3  
- **Concepts & Skills:**
  - Object-Oriented Programming (OOP)
  - Session State Management
  - CRUD Operations
  - Secure SQL Queries
  - UI Design for Web Apps

---

## 📸 Application Preview

### The image below represents how account data (balance, CPF, credentials) is structured and stored in the SQLite database.

![Database Structure](assets/photo.png)

---

## 🧠 Project Architecture

```text
├── Bank.db              # SQLite database
├── app.py               # Main Streamlit application
├── Bank (Class)         # Handles all database logic
├── BankApp (Class)      # UI rendering & navigation
└── assets/              # Images used in the project

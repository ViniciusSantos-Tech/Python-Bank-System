# $${\color{blue}\text{🏦 Secure Banking API}}$$
### A functional **Banking REST API** built with FastAPI, JWT Authentication, SQLAlchemy ORM, and secure password hashing.

This project is a backend banking system designed to simulate real financial operations such as user registration, authentication, transfers between accounts, and transaction history management.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

> [!IMPORTANT]
> ### 📝 Project Status
> This is a functional backend study project focused on **secure authentication**, **database integrity**, and **financial transaction logic**.  
> The system includes password hashing, JWT-based authentication, and safe balance updates to prevent race conditions.

---

# 🟦 Project Overview

The system simulates a simple banking infrastructure where users can create accounts, authenticate, send money to other users, and view their transaction history.

The project emphasizes three main pillars:

- **Security**
- **Reliable financial operations**
- **Structured backend architecture**

Each account starts with an **initial balance of 100 units**, allowing users to immediately test transactions.

---

# 🟦 Core System Logic

### 🔐 Authentication System
Authentication is handled using **JWT tokens**.

- Users authenticate with **CPF and password**
- A **JWT access token** is returned
- Protected routes require a valid token via **OAuth2PasswordBearer**

---

### 🔒 Password Security

Passwords are **never stored in plain text**.

They are processed using a hashing function before being stored in the database. During login, the provided password is verified against the stored hash.

---

### 🗄️ Database Design

The system uses **SQLAlchemy ORM** with relational tables.

Main entities:

**BankAccounts**
- Stores user information
- Contains current balance
- Uses unique identifiers such as CPF, Gmail, and Username

**History**
- Stores all financial transactions
- Linked to accounts through a foreign key
- Automatically records timestamps

---

# $${\color{blue}\text{🏦 Python Banking API - Enterprise Grade}}$$
### A high-performance, secure, and professional **Banking REST API** built with FastAPI, PostgreSQL, and SQLAlchemy ORM.

This project represents a major evolution in backend engineering, moving from simple scripts to a structured **Enterprise Architecture** focused on **Financial Precision**, **Relational Schemas**, and **Scalability**.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

> [!CAUTION]
> ### ⚠️ Project Under Active Development
> This system receives frequent updates (typically every 3 days or less). Any unexpected behavior or incomplete information is due to this continuous process of improvement, refactoring, and security enhancement.

---

## 🧠 Project Overview

The **Python Banking API** is a robust backend system designed for complex financial operations. It utilizes an **ORM (Object-Relational Mapping)** approach to ensure that business logic and database management are decoupled, following the best practices of modern software development.

### 🟦 Key Engineering Focus:
- **Financial Precision:** Implementation of `Numeric(10, 2)` types to eliminate floating-point rounding errors.
- **ORM Integration:** Powered by **SQLAlchemy** for advanced database abstraction and security.
- **Relational Schemas:** Data is organized within custom PostgreSQL schemas (`Bank`) for better isolation.
- **Self-Documented:** Fully documented using Python **Docstrings** (Google Style) and Swagger UI.

---

## 🟦 Main Features

### 🔐 Advanced Security & Integrity
- **SHA-256 Hashing:** Strong encryption for credentials using `hashlib`.
- **Relational Constraints:** Foreign Keys and Unique constraints managed by the database engine.
- **Transactional Safety:** Full ACID compliance for money transfers using SQLAlchemy sessions.

### 💰 Professional Financial Engine
- **Decimal-Based Calculations:** Precise fund management using the `Decimal` library to avoid cent loss.
- **Automated Transactions:** Every movement creates a detailed record in the `Transactions` table.
- **Schema Isolation:** Optimized table organization within the PostgreSQL environment.

### 🛠️ Professional Documentation
- **Swagger UI Integration:** Interactive API documentation available at the `/docs` endpoint.
- **Docstrings:** High-level code explanation directly in the source files.

---

## 🛠️ Technologies Used

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Language:** Python 3.13+
- **Database:** PostgreSQL (Professional Grade)
- **Database Driver:** Psycopg2
- **Data Validation:** Pydantic
- **Security:** Hashlib (SHA-256)

---

## 📸 API Preview

### **Documentation & Testing:** Real-time testing of all endpoints via auto-generated Swagger interface.
![API Preview](assets/photo2.png)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

---

## 📖 Quick Guide (Endpoints)

1. **`POST /accounts`**: Create a new account with hashed credentials.
2. **`POST /login`**: Secure authentication and identity verification.
3. **`POST /transactions`**: Precise money transfer between validated accounts.
4. **`GET /History/{user_id}`**: Complete audit trail of financial movements.
5. **`DELETE /Delete/{user_id}`**: Secure account termination with cascade history cleanup.

---

## 🛠️ Local Setup (For Developers)

<details>
  <summary>Click to see how to run this project on your machine</summary>

  1. **Clone the repo:**
     ```bash
     git clone [https://github.com/ViniciusSantos-Tech/python-bank-system.git](https://github.com/ViniciusSantos-Tech/python-bank-system.git)
     ```
  2. **Install requirements:**
     ```bash
     pip install -r requirements.txt
     ```
  3. **Setup Database:**
     Ensure you have a PostgreSQL instance running and update the `URL_BANK` in `database.py`.
     
  4. **Run the API:**
     ```bash
     uvicorn main:app --reload
     ```
  5. **Access Documentation:**
     Open `http://127.0.0.1:8000/docs` in your browser.

</details>
---
### Developed with ❤️ by **Vinícius Santos-Tech**

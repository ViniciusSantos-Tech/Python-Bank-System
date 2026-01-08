# $${\color{blue}\text{🏦 Python Banking API}}$$
### A high-performance, secure, and professional **Banking REST API** built with FastAPI, SQLite, and SHA-256 Hashing.

This project represents a major evolution in backend engineering, moving from simple scripts to a structured **API architecture** focused on **security**, **scalability**, and **data integrity**.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

> [!CAUTION]
> ### ⚠️ Project Under Active Development
> This system receives frequent updates (typically every 3 days or less). Any unexpected behavior or incomplete information is due to this continuous process of improvement, refactoring, and security enhancement.
---

## 🧠 Project Overview

The **Python Banking API** is a robust backend system designed to handle core financial operations. It features a clean separation between the database layer and the application routes, ensuring modularity and easy maintenance.

### 🎯 Key Engineering Focus:
- **Security First:** Implementation of manual SHA-256 hashing for sensitive data.
- **RESTful Architecture:** Clear endpoints for full CRUD operations.
- **Relational Integrity:** Automated handling of transaction history and account relationships.
- **Validation:** Strict data typing using Pydantic models.

---

## 🚀 Main Features

### 🔐 Advanced Security
- **SHA-256 Password Hashing:** User passwords are encrypted before storage. No plain-text passwords ever touch the database.
- **CPF Uniqueness:** Native SQLite constraints to prevent duplicate identity records.
- **Protected Endpoints:** Validation of credentials for sensitive operations like account deletion.

### 💰 Financial Engine
- **Transactional Transfers:** Atomic logic to ensure money is debited from one account and credited to another simultaneously.
- **Double-Check Validation:** The system verifies recipient existence and sender balance before any transfer.
- **Dynamic History:** Automatic logging of every transaction with timestamps and quantity tracking.

### 🛠️ Data Management
- **Persistence:** Full SQLite integration for permanent data storage.
- **Relational Cleanup:** Smart deletion logic that clears a user's history when an account is closed to prevent database bloating.

---

## 🛠️ Technologies Used

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High performance)
- **Language:** Python 3.13+
- **Database:** SQLite3
- **Data Validation:** Pydantic
- **Security:** Hashlib (SHA-256)
- **Documentation:** Swagger UI (Auto-generated)

---

## 📸 API Preview

### **Documentation & Testing:** The API features an auto-generated Swagger interface for real-time testing of all endpoints.
![Login Screen](assets/photo2.png)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

---

## 📖 Quick Guide (How to Use)

1. **Register:** Send a `POST` request to `/Register` with name, password, and CPF.
2. **Login:** Validate your credentials at `/Login`.
3. **Send Money:** Use the `/Send` endpoint to transfer values using account IDs.
4. **Audit:** Check the `/History/{id_user}` to see all movements for a specific account.

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
     pip install fastapi uvicorn
     ```
  3. **Run the API:**
     ```bash
     uvicorn main:app --reload
     ```
  4. **Access Documentation:**
     Open `http://127.0.0.1:8000/docs` in your browser.

</details>

---
### Developed with ❤️ by **Vinícius Santos-Tech**

# $${\color{blue}\text{🏦 Personal Bank API}}$$
### A functional **Banking REST API** featuring JWT Authentication, Argon2 Password Hashing, and SQLAlchemy.

This project is a backend system designed to handle secure user registration, authentication, and financial transfers.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

> [!IMPORTANT]
> ### 📝 Project Status
> This is a functional study project focused on backend logic. It implements real security standards like Argon2 for passwords and JWT for session management.

---

## 🟦 Project Overview

The system focuses on three core pillars: Security, Database Integrity, and Financial Logic. It uses a relational database to ensure that transfers are consistent and that user data is protected.

### 🟦 Core Logic:
- **Authentication:** JWT (JSON Web Tokens) used via the `OAuth2PasswordBearer` flow.
- **Security:** Passwords are never stored in plain text; they are hashed using **Argon2**.
- **Database:** Managed by **SQLAlchemy** with support for PostgreSQL (via `DATABASE_URL`).
- **Safety:** Transfers use `with_for_update()` to prevent race conditions during balance updates.

---

## 🟦 API Endpoints

The API is organized into the following functional groups:

### 🔐 Authentication
- **`POST /login`**: Users provide their CPF (as username) and Password to receive an `access_token`.

### 👤 User Management
- **`POST /register`**: Registers a new user with Full Name, Gmail, CPF, and Username. All new accounts start with a balance of **100**.

### 💰 Banking Operations
- **`POST /transactions`**: Allows a logged-in user to send money to another user by providing the destination CPF.
  - *Validation:* Prevents sending to yourself, sending 0, or sending more than your current balance.

---

## 🛠️ Technologies Used

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Security & Hashing:** Argon2 (`argon2-cffi`)
- **Token Management:** PyJWT
- **Environment:** Python-dotenv
- **Validation:** Pydantic

---

## 🛠️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>

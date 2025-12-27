# $${\color{blue}\text{🏦 Python Bank System}}$$
### A modern, interactive, and secure **web banking application** built with Python, SQLite, and Streamlit.  
This project showcases the evolution from a CLI system to a **full interactive web interface**, focusing on **OOP**, **database persistence**, and **state management**.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

---
## 🧠 Project Overview

The project is a study-driven yet professional-grade project designed to simulate the **core backend logic of a real banking system**.

Although the application includes a web interface built with **Streamlit**, the **main focus of this project is backend engineering**, including:

- Business rules implementation  
- Database modeling and persistence  
- Secure data handling  
- Object-Oriented architecture  
- Separation of concerns  

The UI exists **only to demonstrate and test the backend logic in a realistic environment**.

## 🌐 Deploy
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://python-bank-system-2ymuuuwsrs85wpl32blgxu.streamlit.app/)
> [!CAUTION]
> ### ⚠️ Access Credentials Required
> To explore the features of the Live Demo, you **must** use the following pre-registered credentials (case-sensitive):
>
> - **Username:** `Vinicius` (The "V" must be uppercase)
> - **Password:** `12345`

---

## 🚀 Key Features

### 🔐 Authentication & Session Control
- User login with username and password
- Session-based authentication using Streamlit Session State
- Controlled access to sensitive operations

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

### **Secure Login:** A secure access point where user authentication takes place, as shown in the image below. Improvements coming soon.

![Database Structure](assets/photo2.png)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## The image below shows the main banking interface after a successful login. It features a personalized welcome message, real-time balance display, and intuitive controls for deposits and withdrawals, all powered by Streamlit's reactive components
![Database Structure](assets/photo3.png)

> **Acesse a versão online para testes rápidos.**
### 🌐 [Click here to Open the Live App](https://python-bank-system-2ymuuuwsrs85wpl32blgxu.streamlit.app/)

---

## 📖 Quick Guide (How to Use)
1. Open the **Live App** link above.
2. Login with user `Vinicius` and password `12345`.
3. Use the sidebar to navigate between Home and About.

---

## 🛠️ Local Setup (For Developers only)
<details>
  <summary>Click to see how to run this project on your machine</summary>

  1. **Clone the repo:**
     ```bash
     git clone [https://github.com/SeuUsuario/python-bank-system.git](https://github.com/SeuUsuario/python-bank-system.git)
     ```
  2. **Install requirements:**
     ```bash
     pip install -r requirements.txt
     ```
  3. **Run the app:**
     ```bash
     streamlit run bank_system.py
     ```

</details>

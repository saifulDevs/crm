# 🧠 AI Agent-Based CRM System

A modern, modular, and AI-enhanced CRM platform inspired by **ServiceNow**, built with **FastAPI** (backend), **Remix** (frontend), and **PostgreSQL** for storage.

## ✨ Features

### ✅ Core Modules

- **User Authentication** (JWT + Role-Based Access)
- **Agent Management** (Add, Assign, Track Performance)
- **Customer Management** (CRM with status and tagging)
- **Task & Workflow Automation**
- **Activity Logs & Notes**
- **Customizable Dashboards**
- **Notifications**

### 🤖 AI Capabilities (Upcoming)

- AI-powered chatbot for agents
- Email & lead summarization
- Auto-classification & task recommendations

---

## 📦 Tech Stack

| Layer     | Tech                         |
| --------- | ---------------------------- |
| Backend   | FastAPI, SQLAlchemy, Alembic |
| Database  | PostgreSQL                   |
| Auth      | JWT, Passlib, Bcrypt         |
| Frontend  | Remix (React), Tailwind CSS  |
| AI Layer  | (Planned) LangChain/OpenAI   |
| Dev Tools | Docker, dotenv, SlowAPI      |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/saifulDevs/crm.git
cd crm
```

##  Project Structure
crm/
└── src/
    ├── main.py
    ├── api.py
    ├── exceptions.py
    ├── logging.py
    ├── rate_limiter.py
    ├── database/
    │   ├── __init__.py
    │   ├── connection.py
    │   └── seed.py
    ├── auth/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── models.py
    │   ├── schema.py
    │   ├── service.py
    │   └── utils.py
    ├── users/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── models.py
    │   ├── schema.py
    │   ├── service.py
    │   └── utils.py
    ├── todos/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── models.py
    │   ├── schema.py
    │   ├── service.py
    │   └── utils.py
    ├── agents/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── models.py
    │   ├── schema.py
    │   ├── service.py
    │   └── utils.py
    ├── tasks/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── models.py
    │   ├── schema.py
    │   ├── service.py
    │   └── utils.py
    ├── tickets/
    │   ├── __init__.py
    │   ├── controller.py
    │   ├── models.py
    │   ├── schema.py
    │   ├── service.py
    │   └── utils.py


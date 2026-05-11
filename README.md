# Task Manager — Flask + SocketIO

A simple full-stack task management system with real-time updates, built using Flask, SQLAlchemy, and Socket.IO.

---

## 🚀 Features

- ➕ Add / Edit / Delete Tasks
- ⚡ Real-time updates using Socket.IO
- 📊 Task analytics dashboard
- 🔐 Login / Register authentication
- 🎯 Priority & status tracking

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Flask, Flask-Login, Flask-SocketIO |
| Database | SQLAlchemy |
| Analytics | Pandas, NumPy |
| Frontend | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
app/
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
│
├── __init__.py
├── auth.py
├── config.py
├── models.py
├── tasks.py
├── analytics.py
└── websocket.py

run.py
requirements.txt
schema.sql
README.md
```

---

## ⚙️ Setup

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Run the app**

```bash
python run.py
```

**3. Open in browser**

```
http://127.0.0.1:5000
```

---

## 🔌 API Routes

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/tasks` | Get all tasks |
| `POST` | `/api/tasks` | Create a new task |
| `PUT` | `/api/tasks/<id>` | Update a task |
| `DELETE` | `/api/tasks/<id>` | Delete a task |
| `GET` | `/api/analytics` | Get dashboard stats |

---

## ⚡ Real-Time Events (WebSockets)

| Event | Trigger |
|---|---|
| `new_task` | A new task is created |
| `task_updated` | An existing task is modified |
| `task_deleted` | A task is removed |

> UI updates automatically without a page refresh.

---

## 👨‍💻 Summary

A real-time task manager with authentication, live analytics, and WebSocket-based updates — no refresh needed.

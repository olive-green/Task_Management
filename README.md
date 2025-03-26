# Task_Management

A Django + Django REST Framework-based application for managing tasks and users. This API allows you to:

- Create users
- Create tasks
- Assign tasks to one or more users
- Retrieve all tasks assigned to a specific user

---

##  Project Structure

```
taskmanager/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── taskmanager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/taskmanager-api.git
cd taskmanager-api
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install manually:

```bash
pip install django djangorestframework
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint                            | Description                       |
|--------|-------------------------------------|-----------------------------------|
| POST   | `/api/users/create/`                | Create a new user                 |
| POST   | `/api/tasks/create/`                | Create a new task                 |
| POST   | `/api/tasks/<task_id>/assign/`      | Assign a task to users           |
| GET    | `/api/users/<user_id>/tasks/`       | Get all tasks for a user         |

---

##  Example Requests

###  Create User

**POST** `/api/users/create/`
```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "mobile": "9876543210"
}
```

###  Create Task

**POST** `/api/tasks/create/`
```json
{
  "name": "Design Dashboard",
  "description": "Create UI for the analytics dashboard",
  "assigned_users_ids": [1, 2]
}
```

###  Assign Task

**POST** `/api/tasks/1/assign/`
```json
{
  "user_ids": [1, 3]
}
```

###  Get Tasks by User

**GET** `/api/users/1/tasks/`

---

## Tech Stack

- Python 3.8+
- Django 4.x
- Django REST Framework

---

##  To-Do

- Task creation
-  User creation
-  Task assignment
-  Fetch tasks for a user
-  JWT Authentication (optional next step)
-  Basic admin panel for browsing models

---



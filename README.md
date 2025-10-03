# 📝 Task & Project Management API

A REST API built with **Django + Django REST Framework** for managing teams, projects, and tasks.  
It uses **JWT authentication** and provides fine-grained permissions for team leaders, members, and admins.  

---

## ⚙️ Features

- 👤 User registration & JWT-based authentication  
- 👥 Teams with leaders and members  
- 📂 Projects linked to teams  
- ✅ Tasks linked to projects  
- 🔒 Role-based permissions (Admin, Leader, Member)  

---

## 🚀 Getting Started

### 1. Clone repository
```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Run server
```bash
python manage.py runserver
```

API will be available at:  
👉 http://127.0.0.1:8000/api/

---

## 🔑 Authentication

The API uses **JWT Authentication**.  
Install tokens app if not already:
```bash
pip install djangorestframework-simplejwt
```

### Obtain Token
`POST /api/users/login/`

```json
{
  "username": "john",
  "password": "password123"
}
```

Response:
```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

### Refresh Token
`POST /api/users/refresh/`

```json
{
  "refresh": "<jwt_refresh_token>"
}
```

Response:
```json
{
  "access": "<new_access_token>"
}
```

👉 Use the token in requests:

```
Authorization: Bearer <your_token>
```

---

## 📘 API Endpoints

### 👤 Users

#### Register
`POST /api/users/register/`
```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

#### Login
`POST /api/users/login/`

---

### 👥 Teams

#### List Teams
`GET /api/teams/`

```json
[
  {
    "id": 1,
    "name": "Dev Team",
    "leader": 2,
    "members": [2, 3, 4]
  }
]
```

#### Create Team *(Leader/Admin only)*
`POST /api/teams/`

```json
{
  "name": "Dev Team",
  "leader": 2,
  "members": [2, 3, 4]
}
```

---

### 📂 Projects

#### List Projects *(Authenticated users)*
`GET /api/projects/`

```json
[
  {
    "id": 1,
    "title": "API Development",
    "description": "Build task manager API",
    "team_info": {
      "id": 1,
      "name": "Dev Team",
      "leader": 2,
      "members": [2, 3, 4]
    }
  }
]
```

#### Retrieve Project *(Team members & leader)*
`GET /api/projects/{id}/`

#### Create Project *(Admin only)*
`POST /api/projects/`
```json
{
  "title": "API Development",
  "description": "Build task manager API",
  "team": 1
}
```

#### Update Project *(Leader only)*
`PATCH /api/projects/{id}/`

#### Delete Project *(Leader only)*
`DELETE /api/projects/{id}/`

---

### ✅ Tasks

#### List Tasks
`GET /api/tasks/`

#### Retrieve Task *(Leader & members)*
`GET /api/tasks/{id}/`

```json
{
  "id": 10,
  "title": "Implement permissions",
  "description": "Setup DRF permissions for projects",
  "project_info": {
    "id": 1,
    "title": "API Development",
    "team_info": {
      "id": 1,
      "name": "Dev Team"
    }
  }
}
```

#### Create Task *(Leader only)*
`POST /api/tasks/`

```json
{
  "title": "Implement permissions",
  "description": "Setup DRF permissions",
  "project": 1
}
```

#### Update Task *(Leader only)*
`PATCH /api/tasks/{id}/`

#### Delete Task *(Leader only)*
`DELETE /api/tasks/{id}/`

---

## 🔒 Permissions Summary

| Action                   | Who can do it? |
|---------------------------|----------------|
| View project list         | Any authenticated user |
| View project detail       | Team members & leader |
| Create project            | Admin only |
| Update/Delete project     | Project leader only |
| View task                 | Project leader & members |
| Create/Update/Delete task | Project leader only |

---

## 🛠 Tech Stack

- [Django](https://www.djangoproject.com/)  
- [Django REST Framework](https://www.django-rest-framework.org/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)  

---

## 📌 Notes

- Future improvements:
  - 📩 In-app messenger for members  
  - 🏷️ Task & project status indexing  
  - 🔍 Advanced search & filters

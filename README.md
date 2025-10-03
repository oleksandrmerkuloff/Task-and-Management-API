# Team Management API

This API allows managing Users, Teams, Projects, and Tasks.
Built with **Django REST Framework**, with custom permissions for team leaders and members.

---

## **Base URLs**

* Admin panel: `/admin/`
* Users app: `/users/`
* Teams app: `/teams/`
* Projects app: `/projects/`

---

## **Authentication**

Uses JWT authentication via **djangorestframework-simplejwt**.

### Obtain token

```
POST /users/token/  (or your configured path)
```

Request body:

```json
{
  "email": "your_email",
  "password": "your_password"
}
```

Response:

```json
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

### Refresh token

```
POST /users/token/refresh/
```

Request body:

```json
{
  "refresh": "refresh_token"
}
```

---

## **API Documentation**

All endpoints, schemas, and authentication details are available via **DRF Spectacular**:

* OpenAPI schema: `/api/schema/`
* Swagger UI: `/api/schema/swagger-ui/`
* Redoc: `/api/schema/redoc/`

This allows users to explore the full API and try requests directly in the browser.

---

## **Permissions**

* **Team Leader**: full access to team and memberships.
* **Team Member**: can view tasks and add tasks if allowed.
* **Staff**: full access.
* **Other users**: blocked from team-specific endpoints.

---

## **Setup**

1. Clone the repository

```bash
git clone <repo_url>
cd <project_folder>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Apply migrations

```bash
python manage.py migrate
```

4. Create superuser (optional)

```bash
python manage.py createsuperuser
```

5. Run server

```bash
python manage.py runserver
```

---

## **Testing**

* Use **Django default testing framework**:

```bash
python manage.py test
```

---

## **Notes**

* All POST/PATCH requests require **JWT token in Authorization header**:

```
Authorization: Bearer <access_token>
```

* Full API documentation is available via DRF Spectacular (Swagger UI / Redoc).


## 🔒 Permissions Summary

| Action                   | Who can do it? |
|---------------------------|----------------|
| View project list         | Any authenticated user |
| View project detail       | Team members & leader |
| Create project            | Admin only |
| Update/Delete project     | Project leader and Admin only |
| View task                 | Project leader & members |
| Create/Update/Delete task | Team members |

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

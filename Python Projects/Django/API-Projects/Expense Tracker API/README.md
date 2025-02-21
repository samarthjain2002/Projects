# Expense Tracker API

Project URL: https://roadmap.sh/projects/expense-tracker-api

A RESTful API for managing personal expenses, built using Django and Django REST Framework (DRF). This API allows users to sign up, log in, and manage their personal expenses securely.

![Blogging Platorm API](https://assets.roadmap.sh/guest/expense-tracker-api-m72p5.png)

## Features
- User registration and authentication (JWT-based authentication)
- CRUD operations for expenses
- User-based authorization for expenses

## API Endpoints

### User Registration
#### Request:
```sh
curl -X POST http://127.0.0.1:8000/register/ \
     -H "Content-Type: application/json" \
     -d '{
           "name": "John Doe",
           "email": "john@doe.com",
           "password": "password"
         }'
```
#### Response:
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
**Status Code:** `201 Created` or `400 Bad Request` if email is already taken.

### User Login
#### Request:
```sh
curl -X POST http://127.0.0.1:8000/login/ \
     -H "Content-Type: application/json" \
     -d '{
           "email": "john@doe.com",
           "password": "password"
         }'
```
#### Response:
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
**Status Code:** `200 OK` or `401 Unauthorized` if credentials are invalid.

### Add a New Expense
#### Request:
```sh
curl -X POST http://127.0.0.1:8000/expenses/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <access>" \
     -d '{
           "category": "Groceries",
           "amount": 50.75,
           "description": "Bought groceries",
           "date": "2025-02-21"
         }'
```
#### Response:
```json
{
  "id": 1,
  "category": "Groceries",
  "amount": 50.75,
  "description": "Bought groceries",
  "date": "2025-02-21"
}
```
**Status Code:** `201 Created` or `401 Unauthorized` if the token is missing or invalid.

### Update an Expense
#### Request:
```sh
curl -X PUT http://127.0.0.1:8000/expenses/1/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <access>" \
     -d '{
           "category": "Groceries",
           "amount": 60.00,
           "description": "Updated grocery expenses",
           "date": "2025-02-21"
         }'
```
#### Response:
```json
{
  "id": 1,
  "category": "Groceries",
  "amount": 60.00,
  "description": "Updated grocery expenses",
  "date": "2025-02-21"
}
```
**Status Code:** `200 OK`, `403 Forbidden` if unauthorized, or `401 Unauthorized` if the token is missing.

### Delete an Expense
#### Request:
```sh
curl -X DELETE http://127.0.0.1:8000/expenses/1/ \
     -H "Authorization: Bearer <access>"
```
**Status Code:** `204 No Content` if deletion is successful, `403 Forbidden` if unauthorized, or `401 Unauthorized` if the token is missing.

## Running the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/samarthjain2002/Projects.git
   cd "Python Projects\Django\API-Projects\Expense Tracker API\expenses"
   ```

2. Install dependencies:
   ```sh
   pip install django djangorestframework djangorestframework-simplejwt
   ```

3. Apply migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:
   ```sh
   python manage.py runserver
   ```

5. Access the API at `http://127.0.0.1:8000/expenses/`

## Dependencies
- Django
- Django REST Framework
- Simple JWT (for authentication)

## License
This project is licensed under the MIT License.


# To-Do List API

Project URL: https://roadmap.sh/projects/todo-list-api

A RESTful API for managing to-do lists built using Django and Django REST Framework (DRF). This API allows users to register, authenticate, and manage their personal to-do items securely.

![Blogging Platorm API](https://assets.roadmap.sh/guest/todo-list-api-bsrdd.png)

## Goals
The skills you will learn from this project include:

- User authentication
- Schema design and Databases
- RESTful API design
- CRUD operations
- Error handling
- Security

## Requirements
You are required to develop a RESTful API with following endpoints

- User registration to create a new user
- Login endpoint to authenticate the user and generate a token
- CRUD operations for managing the to-do list
- Implement user authentication to allow only authorized users to access the to-do list
- Implement error handling and security measures
- Use a database to store the user and to-do list data (you can use any database of your choice)
- Implement proper data validation
- Implement pagination and filtering for the to-do list

## Features
- User registration and authentication (Token-based authentication)
- CRUD operations for to-do items
- User-based authorization for to-do items
- Paginated responses for listing to-do items
- Refresh token mechanism for the authentication
- Logout to erase the token

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
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
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
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
```
**Status Code:** `200 OK` or `401 Unauthorized` if credentials are invalid.

### Create a To-Do Item
#### Request:
```sh
curl -X POST http://127.0.0.1:8000/todos/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token <token>" \
     -d '{
           "title": "Buy groceries",
           "description": "Buy milk, eggs, and bread"
         }'
```
#### Response:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Buy milk, eggs, and bread"
}
```
**Status Code:** `201 Created` or `401 Unauthorized` if the token is missing or invalid.

### Update a To-Do Item
#### Request:
```sh
curl -X PUT http://127.0.0.1:8000/todos/1/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token <token>" \
     -d '{
           "title": "Buy groceries",
           "description": "Buy milk, eggs, bread, and cheese"
         }'
```
#### Response:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Buy milk, eggs, bread, and cheese"
}
```
**Status Code:** `200 OK`, `403 Forbidden` if unauthorized, or `401 Unauthorized` if the token is missing.

### Delete a To-Do Item
#### Request:
```sh
curl -X DELETE http://127.0.0.1:8000/todos/1/ \
     -H "Authorization: Token <token>"
```
**Status Code:** `204 No Content` if deletion is successful, `403 Forbidden` if unauthorized, or `401 Unauthorized` if the token is missing.

### Get To-Do Items (Paginated)
#### Request:
```sh
curl -X GET "http://127.0.0.1:8000/todos/?page=1&limit=10" \
     -H "Authorization: Token <token>"
```
#### Response:
```json
{
  "data": [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Buy milk, eggs, bread"
    },
    {
      "id": 2,
      "title": "Pay bills",
      "description": "Pay electricity and water bills"
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 2
}
```
**Status Code:** `200 OK` or `401 Unauthorized` if the token is missing.

## Running the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/samarthjain2002/Projects.git
   cd "Python Projects\Django\API-Projects\Todo List API\todolist"
   ```

2. Install dependencies:
   ```sh
   pip install django djangorestframework
   ```

3. Apply migrations:
   ```sh
   python manage.py migrate
   ```

4. Start the development server:
   ```sh
   python manage.py runserver
   ```

5. Access the API at `http://127.0.0.1:8000/todos/`

## Dependencies
- Django
- Django REST Framework

## License
This project is licensed under the MIT License.


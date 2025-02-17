# Blogging Platform API

Project URL: https://roadmap.sh/projects/blogging-platform-api

A RESTful API for a personal blogging platform built using Django and Django REST Framework (DRF) with basic CRUD operations for a personal blogging platform. CRUD stands for Create, Read, Update, and Delete.

![Blogging Platorm API](https://assets.roadmap.sh/guest/blogging-platform-api.png)

## Goals
The goals of this project are to help you:

- Understand what the RESTful APIs are including best practices and conventions
- Learn how to create a RESTful API
- Learn about common HTTP methods like GET, POST, PUT, PATCH, DELETE
- Learn about status codes and error handling in APIs
- Learn how to perform CRUD operations using an API
- Learn how to work with databases

## Requirements
You should create a RESTful API for a personal blogging platform. The API should allow users to perform the following operations:

- Create a new blog post
- Update an existing blog post
- Delete an existing blog post
- Get a single blog post
- Get all blog posts
- Filter blog posts by a search term

## Features
- CRUD operations for blog posts
- Filtering by title, content, and category
- JSON-based API responses

## API Endpoints

### List all posts
#### Request:
```sh
curl -X GET http://127.0.0.1:8000/posts/
```
#### Response:
```json
[
  {
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"],
    "createdAt": "2021-09-01T12:00:00Z",
    "updatedAt": "2021-09-01T12:00:00Z"
  }
]
```
**Status Code:** `200 OK`

### Search and Filter posts
#### Request:
```sh
curl -X GET "http://127.0.0.1:8000/posts/?search=Technology"
```
#### Response:
```json
[
  {
    "id": 2,
    "title": "Tech Innovations",
    "content": "Latest updates in technology.",
    "category": "Technology",
    "tags": ["Tech", "Innovation"],
    "createdAt": "2021-10-01T10:30:00Z",
    "updatedAt": "2021-10-01T10:30:00Z"
  }
]
```
**Status Code:** `200 OK`

### Retrieve a specific post
#### Request:
```sh
curl -X GET http://127.0.0.1:8000/posts/1/
```
#### Response:
```json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```
**Status Code:** `200 OK` or `404 Not Found` if the post does not exist.

### Create a new post
#### Request:
```sh
curl -X POST http://127.0.0.1:8000/posts/ \ 
     -H "Content-Type: application/json" \ 
     -d '{
           "title": "New Blog Post",
           "content": "This is a new blog post.",
           "category": "Lifestyle",
           "tags": ["Life", "Wellness"]
         }'
```
#### Response:
```json
{
  "id": 2,
  "title": "New Blog Post",
  "content": "This is a new blog post.",
  "category": "Lifestyle",
  "tags": ["Life", "Wellness"],
  "createdAt": "2021-09-02T15:00:00Z",
  "updatedAt": "2021-09-02T15:00:00Z"
}
```
**Status Code:** `201 Created` or `400 Bad Request` if the request is invalid.

### Update an existing post
#### Request:
```sh
curl -X PUT http://127.0.0.1:8000/posts/1/ \ 
     -H "Content-Type: application/json" \ 
     -d '{
           "title": "Updated Blog Post",
           "content": "Updated content.",
           "category": "Technology",
           "tags": ["Updated", "Tech"]
         }'
```
#### Response:
```json
{
  "id": 1,
  "title": "Updated Blog Post",
  "content": "Updated content.",
  "category": "Technology",
  "tags": ["Updated", "Tech"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-03T08:00:00Z"
}
```
**Status Code:** `200 OK` or `400 Bad Request` if the request is invalid or `404 Not Found` if the post does not exist.

### Delete a post
#### Request:
```sh
curl -X DELETE http://127.0.0.1:8000/posts/1/
```
**Status Code:** `204 No Content` if the deletion is successful, or `404 Not Found` if the post does not exist.

## Running the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/samarthjain2002/Projects.git
   cd Python Projects/Django/API-Projects/Blogging Platform API/blog_proj
   ```

2. Install dependencies:
   ```sh
   pip install djangorestframework
   ```

3. Apply migrations:
   ```sh
   python manage.py migrate
   ```

4. Start the development server:
   ```sh
   python manage.py runserver
   ```

5. Access the API at `http://127.0.0.1:8000/posts/`

## Dependencies
- Django
- Django REST Framework

## License
This project is licensed under the MIT License.


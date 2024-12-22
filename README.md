
# Project FastAPI Skeleton

This is a FastAPI project that provides a backend API with features including user authentication, role-based access control (RBAC), and CRUD operations for blogs, stores, and products. It also supports public and private routes and integrates a PostgreSQL database.

`!!!This Skeleton Still Development and Imporovement!!!`

## Features

 - User Authentication:
    - User registration and login with hashed passwords.
    - JWT-based authentication and authorization.
 - Role-Based Access Control (RBAC):
    - Secure access to APIs based on user roles (admin, editor, user).
 - CRUD Operations:
    - Manage Users, Roles, Blogs, Stores, and Products.
 - Middleware for Public/Private APIs:
    - Public endpoints are accessible without authentication.
    - Private endpoints require token authentication.
 - Database Integration:
    - PostgreSQL support via SQLAlchemy ORM.
 - Environment Variables:
    - Secure configuration through .env file.
 - Seeding:
    - Predefined roles and admin accounts using database seeders.
## Tech Stack
 - Framework: FastAPI
 - Database: PostgreSQL
 - ORM: SQLAlchemy
 - Authentication: JWT
 - Environment Management: Python dotenv
 - Dependency Management: Pip



## Installation

- Clone the Repository
```bash
git clone <repository-url>
cd fastapi-blog-api
```
- Folder Structure

```bash
  .
├── config/                     # Database and environment configuration
│   ├── database.py             # Database connection
├── models/                     # Database models
│   ├── user.py                 # User models
│   ├── role.py                 # Role models
│   ├── blog.py                 # Blog model
│   ├── store.py                # Store model
│   ├── product.py              # Product model
├── schemas/                    # Pydantic schemas
│   ├── user_schema.py          # User schemas
│   ├── role_schema.py          # Role schemas
│   ├── blog_schema.py          # Blog schemas
│   ├── store_schema.py         # Store schemas
│   ├── product_schema.py       # Product schemas
├── services/                   # Business logic services
│   ├── auth.py                 # Auth logic
│   ├── rbac.py                 # Role Access
│   ├── user_service.py         # User CRUD
│   ├── blog_service.py         # Blog CRUD logic
│   ├── store_service.py        # Store CRUD logic
│   ├── product_service.py      # Product CRUD logic
├── routes/                     # API route definitions
│   ├── auth_routes.py          # Routes for auth user
│   ├── user_routes.py          # Routes for user management
│   ├── blog_routes.py          # Routes for blogs
│   ├── store_routes.py         # Routes for stores
│   ├── product_routes.py       # Routes for products
├── seeder/                     # Database seeders
│   ├── role_seeder.py          # Seeder for roles
├── .env                        # Environment variables
├── main.py                      # Application entry point
└── requirements.txt             # Python dependencies

```
 - Create and Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate  # Linux/MacOS
env\Scripts\activate     # Windows

```
 - Install Dependencies
```bash
pip install -r requirements.txt
``` 
 - Setup Environment Variables
```bash
DATABASE_URL=postgresql://username:password@localhost/db_name
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

``` 
 - Seed Database
```bash
python -m seeder.role_seeder
``` 
 -  Start the Application
```bash
uvicorn main:app --reload --port 8000
``` 
 - API Documentation
   - Swagger UI: http://localhost:8000/docs
   - Check Folder Postman

 - Example API Usage

```bash
# Create New User
POST /api/v1/users/
Content-Type: application/json
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "password",
  "role_id": 1
}

# Sign and Generate Token
POST /api/v1/users/login
Content-Type: application/json

{
  "username": "admin",
  "password": "password"
}

``` 
```bash
# Response Example:
{
  "access_token": "<token>",
  "token_type": "bearer"
}

``` 
## Dependencies
 - FastAPI: Web framework
 - SQLAlchemy: ORM for database interaction
 - PyJWT: Token authentication
 - Python-dotenv: Environment variables management
 - Uvicorn: ASGI server

## Author
> Developed by Muhamad Jumadil Akbar\
> For Question or Support, contact : muhamadjumadilakbar@gmail.com

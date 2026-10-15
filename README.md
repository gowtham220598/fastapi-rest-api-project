# FastAPI REST API Project

A beginner-friendly backend development project built using **Python and FastAPI**. This project demonstrates REST API development, request handling, data validation, and interactive API testing using Swagger UI.

## Project Overview

This project focuses on understanding the fundamentals of backend API development using FastAPI.

It includes multiple GET and POST endpoints for retrieving user information, searching data, creating users, and managing product information.

The APIs are tested using FastAPI's built-in Swagger UI documentation.

## Technologies Used

- **Python** – Backend programming language
- **FastAPI** – Modern Python web framework
- **Pydantic** – Request data validation
- **Uvicorn** – ASGI application server
- **Swagger UI** – Interactive API documentation
- **VS Code** – Development environment

## Key Features

- REST API development using FastAPI
- GET and POST HTTP methods
- Path parameter handling
- Query parameter handling
- User creation using Pydantic models
- Product creation with field validation
- HTTP status code handling
- JSON request and response processing
- Interactive API testing using Swagger UI
- Example endpoint for retrieving user data from a database

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api` | Returns a welcome message |
| GET | `/users/{user_id}` | Retrieves user information by ID |
| GET | `/search` | Demonstrates query parameters |
| POST | `/users` | Creates a user using request data |
| POST | `/products` | Creates a product |
| POST | `/items` | Demonstrates HTTP 201 Created |
| GET | `/users/db/{user_id}` | Retrieves user data from a database |

## Project Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-rest-api-project.git
```

### Step 2: Open the Project Directory

```bash
cd fastapi-rest-api-project
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Step 5: Install Required Packages

```bash
pip install fastapi uvicorn
```

### Step 6: Run the Application

Assuming the FastAPI instance is named `app` inside `app.py`:

```bash
uvicorn app:app --reload
```

### Step 7: Open Swagger UI

Visit:

```text
http://127.0.0.1:8000/docs
```

## API Testing

FastAPI automatically generates interactive API documentation using Swagger UI.

Through Swagger UI, developers can:

- Explore available API endpoints
- Send GET and POST requests
- Provide path and query parameters
- Submit JSON request bodies
- Inspect response data
- Check HTTP status codes
- Identify validation errors

## Example: Get User

Request:

```http
GET /users/10
```

Example Response:

```json
{
  "user_id": 10,
  "type": "class info"
}
```

## Example: Create Product

Request:

```http
POST /products
```

Request Body:

```json
{
  "name": "pen",
  "price": 15,
  "stock": 10
}
```

Example Response:

```json
{
  "name": "pen",
  "price": 15,
  "stock": 10
}
```

## Data Validation

Pydantic models are used to define expected request data and validate incoming values.

The project demonstrates:

- Required fields
- String validation
- Numeric data types
- Minimum and maximum length restrictions
- Automatic validation error responses

## Testing Results

The screenshots demonstrate:

- Successful GET requests with HTTP 200 responses
- Successful product creation with HTTP 200
- User request validation with HTTP 422
- Swagger UI endpoint documentation
- JSON request and response handling

**Note:** The HTTP 422 response demonstrates validation behavior and should not be treated as a successful user creation.

## Future Improvements

- Complete CRUD operations
- Database integration with SQLAlchemy
- JWT authentication
- User login and registration
- Improved exception handling
- Automated API testing
- Deployment to a cloud hosting platform

## Learning Outcomes

Through this project, I gained practical experience in:

- Building backend REST APIs with Python
- Understanding HTTP methods and status codes
- Working with FastAPI routing
- Using Pydantic for data validation
- Handling JSON requests and responses
- Testing APIs using Swagger UI
- Understanding the fundamentals of backend application development

## Author

**Gowtham M**

Python | FastAPI | Backend Development | Generative AI Learner

## Project Status

**Learning Project – API Development and Testing**

This project demonstrates fundamental FastAPI concepts and provides a foundation for developing larger backend applications.
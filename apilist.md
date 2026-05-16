# API Documentation

Base URL: `http://localhost:8000`

---

## Authentication

### Register
`POST /auth/register`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123",
  "confirm_password": "password123"
}
```

**Validation:**
- `name` — min 3, max 50 characters
- `password` — min 6, max 20 characters
- `confirm_password` — must match password

**Response (200):**
```json
{
  "message": "User registered successfully",
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "access_token": "Bearer eyJhbGci..."
  }
}
```

---

### Login
`POST /auth/login`

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "message": "Login successful",
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "access_token": "Bearer eyJhbGci..."
  }
}
```

**Response (401):**
```json
{
  "detail": "Invalid email or password"
}
```

---

### Get Authenticated User
`GET /auth/me`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "message": "User is authenticated",
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

**Response (401):**
```json
{
  "detail": "Invalid or expired token"
}
```

---

## Todo

> All todo endpoints require `Authorization` header.

**Headers:**
```
Authorization: Bearer <access_token>
```

---

### Get All Todos
`GET /todo/`

**Response (200):**
```json
{
  "message": "List of TODO items",
  "data": [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false,
      "created_at": "2026-01-01T00:00:00",
      "updated_at": "2026-01-01T00:00:00"
    }
  ]
}
```

---

### Get Todo by ID
`GET /todo/{id}`

**Response (200):**
```json
{
  "message": "Todo item",
  "data": {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2026-01-01T00:00:00",
    "updated_at": "2026-01-01T00:00:00"
  }
}
```

**Response (404):**
```json
{
  "detail": "Todo not found"
}
```

---

### Create Todo
`POST /todo/`

**Request Body:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "isCompleted": false
}
```

**Validation:**
- `title` — min 3, max 10 characters
- `description` — optional
- `isCompleted` — default false

**Response (200):**
```json
{
  "message": "Todo created successfully",
  "data": {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2026-01-01T00:00:00",
    "updated_at": "2026-01-01T00:00:00"
  }
}
```

---

### Update Todo
`PUT /todo/{id}`

**Request Body (all fields optional):**
```json
{
  "title": "Updated title",
  "description": "Updated desc",
  "isCompleted": true
}
```

**Response (200):**
```json
{
  "message": "Todo updated successfully",
  "data": {
    "id": 1,
    "title": "Updated title",
    "description": "Updated desc",
    "completed": true,
    "created_at": "2026-01-01T00:00:00",
    "updated_at": "2026-01-01T00:00:00"
  }
}
```

**Response (404):**
```json
{
  "detail": "Todo not found"
}
```

---

### Delete Todo
`DELETE /todo/{id}`

**Response (200):**
```json
{
  "message": "Todo deleted successfully"
}
```

**Response (404):**
```json
{
  "detail": "Todo not found"
}
```

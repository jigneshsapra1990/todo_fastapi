# FastAPI Todo Application

A modern todo list application built with FastAPI, featuring user authentication with JWT tokens and a complete database management system. This project demonstrates best practices for building REST APIs with FastAPI, SQLAlchemy, and Alembic.

## Features

- 🔐 **User Authentication** - Secure login and registration using JWT tokens
- 📝 **Todo Management** - Create, read, update, and delete todo items
- 🗄️ **Database Migrations** - Version-controlled database changes with Alembic
- 🛡️ **Password Security** - Passwords are hashed and never stored in plain text
- 🚀 **Modern API** - Built with FastAPI for high performance and automatic documentation

## Prerequisites

Before you start, make sure you have:

- **Python 3.8 or higher** - Check your version with `python --version`
- **uv package manager** - Learn more at https://docs.astral.sh/uv/

## Quick Start

### Step 1: Install uv (if not already installed)

On macOS, Linux, or Windows with WSL:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows (PowerShell):

```powershell
powershell -ExecutionPolicy BypassUser -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Clone the project and navigate to it

```bash
cd /path/to/fastapi-project
```

### Step 3: Install dependencies

This will install all required packages in an isolated environment:

```bash
uv sync
```

### Step 4: Set up the database

First, create a `.env` file in the project root with your database configuration:

```
DATABASE_URL="postgresql://postgres@localhost:5431/fastapi_yt"
APP_NAME=FastAPI Todo App
APP_ENV=development
SECRET_KEY=your-secret-key-here-change-this
```

Then, run the database migrations:

```bash
uv run alembic upgrade head
```

This command will create all the necessary database tables based on your migrations.

### Step 5: Run the application

Start the development server:

```bash
uv run fastapi dev main.py
```

You should see output similar to:

```
INFO:     Uvicorn running on http://localhost:8000
```

Visit http://localhost:8000 in your browser to see the application running.

## API Documentation

Once the app is running, you can view interactive API documentation at:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Available Endpoints

### Authentication Endpoints

#### Register a new user

```
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword",
  "name": "John Doe"
}
```

**Response** (Success - 200):

```json
{
  "message": "User created successfully",
  "data": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

#### Login

```
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response** (Success - 200):

```json
{
  "message": "Login successful",
  "data": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "access_token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

### Todo Endpoints

**All todo endpoints require authentication.** Include the JWT token in the `Authorization` header:

```
Authorization: Bearer <your-access-token>
```

#### Get all todos

```
GET /api/todo/
```

**Response**:

```json
{
  "message": "List of TODO items",
  "data": [
    {
      "id": 1,
      "content": "Learn FastAPI",
      "is_completed": false
    }
  ]
}
```

#### Create a todo

```
POST /api/todo/
Content-Type: application/json
Authorization: Bearer <your-access-token>

{
  "content": "Buy groceries"
}
```

#### Get a specific todo

```
GET /api/todo/{id}
Authorization: Bearer <your-access-token>
```

#### Update a todo

```
PUT /api/todo/{id}
Content-Type: application/json
Authorization: Bearer <your-access-token>

{
  "content": "Updated task",
  "is_completed": true
}
```

#### Delete a todo

```
DELETE /api/todo/{id}
Authorization: Bearer <your-access-token>
```

## Project Structure

```
fastapi/
├── main.py                 # Application entry point - run this to start the server
├── requirements.txt        # List of all dependencies
├── alembic.ini            # Alembic configuration
├── .env                   # Environment variables (create this file)
├── alembic/
│   ├── versions/          # Database migration files
│   └── env.py             # Alembic environment configuration
└── app/
    ├── app.py             # FastAPI application setup
    ├── config/
    │   └── app_config.py   # Configuration settings
    ├── database/
    │   ├── db.py          # Database connection
    │   └── schema/        # Database table definitions
    ├── models/            # Data models for request/response
    │   ├── auth.py        # Auth-related models
    │   └── todo.py        # Todo-related models
    └── routing/           # API endpoint definitions
        ├── auth.py        # Authentication routes
        └── todo.py        # Todo routes
```

## Understanding Key Concepts

### JWT Authentication

JWT (JSON Web Tokens) are used to securely authenticate requests. When you log in, you receive a token that you must include in subsequent requests:

1. **Login** → Receive a JWT token
2. **Store** → Save the token (in browser storage, local storage, etc.)
3. **Use** → Include `Authorization: Bearer <token>` in request headers
4. **Verify** → Server validates the token before processing the request

### Database Migrations

Migrations are like version control for your database. Each migration file describes a change to the database:

- Run all pending migrations: `uv run alembic upgrade head`
- Revert to previous version: `uv run alembic downgrade -1`
- Create a new migration: `uv run alembic revision --autogenerate -m "description"`

### Password Security

Passwords are hashed using industry-standard algorithms. This means:

- Original passwords are never stored
- Even the database administrator can't see passwords
- Hashed passwords can't be converted back to original passwords
- Attempting to log in with the wrong password will fail safely

## Common Tasks

### Add a new dependency

```bash
uv add package-name
```

### Update all dependencies

```bash
uv sync --upgrade
```

### Create a new database migration

First, modify your schema files in `app/database/schema/`, then:

```bash
uv run alembic revision --autogenerate -m "description of changes"
uv run alembic upgrade head
```

### Test an endpoint with curl

Example - Register a user:

```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123","name":"Test User"}'
```

Example - Get todos (with authentication):

```bash
curl -X GET "http://localhost:8000/api/todo/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Troubleshooting

### Port already in use

If you get an error that port 8000 is already in use, you can use a different port:

```bash
uv run python main.py --port 8001
```

### Database connection error

Make sure your `DATABASE_URL` in `.env` is correct and the database file/server is accessible.

### JWT token expired or invalid

Generate a new token by logging in again with `/api/auth/login`.

### Migration conflicts

If you get migration conflicts, check the `alembic/versions/` directory and resolve any conflicting migration files.

## Development Tips

- Use the Swagger UI at http://localhost:8000/docs to test endpoints interactively
- Check logs in the terminal to see what's happening
- Use `.env` to store sensitive information (never commit this file!)
- Make database changes by modifying schema files, then let Alembic generate migrations

## Next Steps

- Add more features (filtering, pagination, etc.)
- Deploy to a production server
- Add tests for your endpoints
- Implement additional authentication methods
- Add email verification for registration

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:

1. Check the FastAPI documentation: https://fastapi.tiangolo.com/
2. Check the SQLAlchemy documentation: https://docs.sqlalchemy.org/
3. Review the Alembic documentation: https://alembic.sqlalchemy.org/

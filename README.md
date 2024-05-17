# E-commerce API

## Project Overview
This is a RESTful API for an e-commerce platform built with FastAPI and PostgreSQL. The API includes functionalities for user authentication, product management, cart management, order processing, and more.

## Features
- User Authentication (Signup, Login, Password Reset)
- Product Management (CRUD Operations)
- Cart Management
- Order Processing
- Payment Integration
- Reviews and Ratings

## Tech Stack
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **Environment Management**: Docker, Virtualenv
- **Deployment**: Uvicorn, Docker Compose

## Project Structure
```bash
ecommerce_api/
├── alembic/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/
│   │   └── __init__.py
│   ├── crud/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── main.py
│   ├── db.py
│   └── dependencies.py
├── migrations/
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
└── requirements.txt

```

## Installation

### Prerequisites
- Docker
- Docker Compose

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ecommerce_api.git
    cd ecommerce_api
    ```

2. **Create a `.env` file**:
    Create a `.env` file in the root directory and add the following:
    ```env
    DATABASE_URL=postgresql://ecom_user:ecom_pass@db:5432/ecommerce_db
    SECRET_KEY=your_generated_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

3. **Build and start the Docker containers**:
    ```bash
    docker-compose up --build
    ```

4. **Apply database migrations**:
    ```bash
    docker-compose run web alembic upgrade head
    ```

### Accessing the Application

- **FastAPI Application**: Open your browser and go to `http://localhost:8000/docs` to see the interactive API documentation (Swagger UI).
- **pgAdmin**: Open your browser and go to `http://localhost:5050` to access pgAdmin.
  - **Login**: Use the default email `admin@admin.com` and password `admin`.
  - **Add a New Server**:
    - **General**:
      - **Name**: `PostgreSQL`
    - **Connection**:
      - **Host name/address**: `db`
      - **Port**: `5432`
      - **Username**: `ecom_user`
      - **Password**: `ecom_pass`
      - **Maintenance database**: `ecommerce_db`

## Usage
- Open your browser and go to `http://localhost:8000/docs` to see the interactive API documentation (Swagger UI).
- You can also visit `http://localhost:8000/redoc` for ReDoc documentation.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-foo`)
3. Commit your changes (`git commit -am 'Add some foo'`)
4. Push to the branch (`git push origin feature-foo`)
5. Create a new Pull Request

## License
[MIT](https://choosealicense.com/licenses/mit/)

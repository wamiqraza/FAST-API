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
- **Environment Management**: Virtualenv
- **Deployment**: Uvicorn

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
├── .env
├── .gitignore
└── requirements.txt

```

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ecommerce_api.git
    cd ecommerce_api
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5. **Run database migrations**:
    ```bash
    alembic upgrade head
    ```

6. **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage
- Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation (Swagger UI).
- You can also visit `http://127.0.0.1:8000/redoc` for ReDoc documentation.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-foo`)
3. Commit your changes (`git commit -am 'Add some foo'`)
4. Push to the branch (`git push origin feature-foo`)
5. Create a new Pull Request

## License
[MIT](https://choosealicense.com/licenses/mit/)

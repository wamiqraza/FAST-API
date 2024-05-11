# SQL (Relational) Databases

FastAPI doesn't require you to use a SQL (relational) database. But you can use any relational database that you want.

You can easily adapt it to any database supported by SQLAlchemy, like:

- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server, etc.

## ORMs

FastAPI works with any database and any style of library to talk to the database. A common pattern is to use an **ORM**: an "object-relational mapping" library.

An ORM has tools to convert ("map") between objects in code and database tables ("relations"). With an ORM, you normally create a class that represents a table in a SQL database, each attribute of the class represents a column, with a name and a type. For example a class Pet could represent a SQL table pets.

## File structure
For these examples, let's say you have a directory named my_super_project that contains a sub-directory called sql_app with a structure like this:

```
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├─ database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```
The file `__init__`.py is just an empty file, but it tells Python that sql_app with all its modules (Python files) is a package.

## Install SQLAlchemy
First you need to install SQLAlchemy:

```
pip install sqlalchemy
```


from fastapi import APIRoute, Depends, HTTPException
from sqlalchemy.orm import Session
from app import curd, schemas
from app.db.dependencies import get_db

router = APIRoute()



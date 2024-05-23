from fastapi import APIRouter, Depends, HTTPException
# from fastapi.routing import APIRoute, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.user import get_user_by_email, create_user
from app.schemas.user import User, UserCreate
from app.db.dependencies import get_db


router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

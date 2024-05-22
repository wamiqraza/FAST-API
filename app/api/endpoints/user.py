from fastapi import APIRouter, Depends, HTTPException
# from fastapi.routing import APIRoute, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user
from app.schemas.user import User, UserBase
from app.db.dependencies import get_db


router = APIRouter()

@router.post("/", response_model=User)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user.create_user(db=db, user=user)

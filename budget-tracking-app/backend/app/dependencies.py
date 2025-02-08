from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import User
from .core.security import get_current_user

def get_current_active_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
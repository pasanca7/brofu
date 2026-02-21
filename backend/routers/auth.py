from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status

from backend.models.User import User
from backend.schemas.UserSchema import UserReadSchema
from backend.utils.database import get_db
from backend.controllers import auth_controller
from backend.utils.auth import verify_password, create_access_token, get_current_user


router = APIRouter(prefix="", tags=["Auth"])


@router.post("/login")
async def login(
    form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):

    user = await auth_controller.get_user_by_usename(db, form.username)
    if user is None or not verify_password(form.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/profile", response_model=UserReadSchema)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

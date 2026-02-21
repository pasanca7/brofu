from typing import Optional
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from backend.models.User import User
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import HTTPException, status
from backend.utils.database import get_db
from backend.settings import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
oauth2_optional = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

UNAUTHORIZED_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Permission Denied",
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise CREDENTIALS_EXCEPTION
        return username
    except JWTError:
        raise CREDENTIALS_EXCEPTION


def get_current_user(token: str = Depends(oauth2), db: Session = Depends(get_db)):
    username = verify_token(token)
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise CREDENTIALS_EXCEPTION
    return user


def get_current_or_none(
    token: Optional[str] = Depends(oauth2_optional), db: Session = Depends(get_db)
):
    try:
        username = verify_token(token)
        return db.query(User).filter(User.username == username).first()
    except:
        return None

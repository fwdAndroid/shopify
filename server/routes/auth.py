
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter, HTTPException
from database import db
import uuid
import bcrypt


router = APIRouter()


@router.post("/signUp")
def signup_user(user: UserCreate):
    # extract user data from request
    print(user.name, user.email, user.password)
    # Here you check user avaialbe yes or no
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    # If user does not exist, create a new user
    hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4),email=user.email,name=user.name,password=hashed_pw)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db
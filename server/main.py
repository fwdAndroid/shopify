from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Database connection setup
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary, Text, create_engine
from sqlalchemy.orm import sessionmaker

#Database connection
from sqlalchemy.ext.declarative import declarative_base

import uuid
import bcrypt

app = FastAPI()

Database_URL = "postgresql://postgres:zeo123456@localhost:5432/music"  # PROJECT_NAME Path
engine = create_engine(Database_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
db = SessionLocal()



class UserCreate(BaseModel):
    name: str
    email: str
    password: str     

# Base class for SQLAlchemy models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)


@app.post("/signUp")
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

# Create the database tables    
Base.metadata.create_all(engine)
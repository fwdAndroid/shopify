from fastapi import FastAPI
from pydantic import BaseModel

# Database connection setup
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary, Text, create_engine
from sqlalchemy.orm import sessionmaker

#Database connection
from sqlalchemy.ext.declarative import declarative_base

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
    # Here you would typically hash the password and save the user to the database
    pass

# Create the database tables    
Base.metadata.create_all(engine)
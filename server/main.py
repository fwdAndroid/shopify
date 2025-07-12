from fastapi import FastAPI
from routes import auth
from models.base import Base
from database import engine

app = FastAPI()


app.include_router(auth.router, prefix="/auth")

# Create the database tables    
Base.metadata.create_all(engine)
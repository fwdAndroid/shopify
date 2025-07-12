
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Database_URL = "postgresql://postgres:zeo123456@localhost:5432/music"  # PROJECT_NAME Path
engine = create_engine(Database_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

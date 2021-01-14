import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def db_url_string():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    return f"postgresql+psycopg2://{user}:{password}@{host}:5432/{db}"


if os.getenv("DB_URL") is None:
    DATABASE_URL = db_url_string()
else:
    DATABASE_URL = os.environ["DB_URL"]

# Create SQLALchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

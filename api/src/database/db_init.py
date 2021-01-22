import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.utils.config import config, CONFIG_ENV


if os.getenv("DB_URL") is None:
    DATABASE_URL = config[CONFIG_ENV].db_url_string()
else:
    DATABASE_URL = os.environ["DB_URL"]

# Create SQLALchemy engine
engine = create_engine(DATABASE_URL)
# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

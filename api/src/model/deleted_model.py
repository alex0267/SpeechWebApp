from sqlalchemy import Column, Integer, String
from src.database.db_init import Base


class Deleted(Base):
    __tablename__ = "deleted"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True)
    timestamp = Column(String, unique=True)

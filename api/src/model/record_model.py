from sqlalchemy import Column, Integer, String, DateTime
from src.database.db_init import Base


class Record(Base):
    __tablename__ = "record"
    id = Column(Integer, primary_key=True, index=True)
    record_url = Column(String, unique=False)
    emotion = Column(String, unique=False)
    timestamp = Column(DateTime, unique=False)
    uuid = Column(String, unique=True)

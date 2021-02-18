from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from ser_api.database.db_init import Base

class Record(Base):
    __tablename__ = "record"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    record_url = Column(String, unique=False)
    emotion = Column(String, unique=False)
    timestamp = Column(DateTime, unique=False,default=func.now())
    uuid = Column(String, unique=True)
    sentence_id = Column(Integer, ForeignKey("sentence.id"))

from sqlalchemy import Column, Integer, String
from api.database.db_init import Base

class Deleted(Base):
    __tablename__ = "deleted"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True)
    timestamp = Column(String, unique=True)

from sqlalchemy import Column, Integer, String
from src.database.db_init import Base


class Sentence(Base):
    __tablename__ = "sentence"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    sentence = Column(String, unique=True)

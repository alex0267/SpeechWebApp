from sqlalchemy import Column, Integer, String
from src.database.db_init import Base


class Sentence(Base):
    __tablename__ = "sentence"
    id = Column(Integer, primary_key=True, index=True)
    sentence = Column(String, unique=True)

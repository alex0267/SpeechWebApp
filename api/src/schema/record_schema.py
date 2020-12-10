from pydantic import BaseModel
from datetime import datetime


class Record(BaseModel):
    record_url: str
    emotion: str
    timestamp: datetime
    uuid: str = ""

    class Config:
        orm_mode = True

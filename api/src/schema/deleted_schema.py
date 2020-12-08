from pydantic import BaseModel
from datetime import datetime


class Deleted(BaseModel):
    uuid: str
    timestamp: datetime

    class Config:
        orm_mode = True

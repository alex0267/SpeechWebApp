from pydantic import BaseModel


class Sentence(BaseModel):
    sentence: str
    id: int

    class Config:
        orm_mode = True

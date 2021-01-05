from pydantic import BaseModel


class Sentence(BaseModel):
    sentence: str

    class Config:
        orm_mode = True

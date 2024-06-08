from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    author: str
    views: int
    position: int

    class Config:
        orm_mode = True
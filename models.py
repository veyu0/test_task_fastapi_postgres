from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    views = Column(Integer)
    position = Column(Integer, unique=True)

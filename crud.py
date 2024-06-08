import models
from database import SessionLocal


def get_items(db: SessionLocal, skip: int = 0):
    return db.query(models.Item).offset(skip).all()


def get_items_by_id(db: SessionLocal, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()
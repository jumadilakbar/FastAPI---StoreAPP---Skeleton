from sqlalchemy.orm import Session
from models.store import Store

def create_store(db: Session, name: str, description: str, user_id: int):
    store = Store(name=name, description=description, user_id=user_id)
    db.add(store)
    db.commit()
    db.refresh(store)
    return store

def get_stores(db: Session):
    return db.query(Store).all()

def get_store_by_id(db: Session, store_id: int):
    return db.query(Store).filter(Store.id == store_id).first()

def delete_store(db: Session, store_id: int):
    store = db.query(Store).filter(Store.id == store_id).first()
    if store:
        db.delete(store)
        db.commit()
    return store

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from models import Store, User

router = APIRouter(prefix="/stores", tags=["Stores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_store(name: str, description: str, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    store = Store(name=name, description=description, user_id=user_id)
    db.add(store)
    db.commit()
    db.refresh(store)
    return store

@router.get("/")
def get_stores(db: Session = Depends(get_db)):
    return db.query(Store).all()

@router.get("/{store_id}")
def get_store(store_id: int, db: Session = Depends(get_db)):
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.delete("/{store_id}")
def delete_store(store_id: int, db: Session = Depends(get_db)):
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    db.delete(store)
    db.commit()
    return {"message": "Store deleted successfully"}

from sqlalchemy.orm import Session
from models.user import User
from services.auth import hash_password
from fastapi import HTTPException
from schemas.user_schema import UserUpdate


def create_user(db: Session, username: str, email: str, hashed_password: str, role_id:int):
    user = User(username=username, email=email, hashed_password=hash_password(hashed_password), role_id=role_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# def update_user(user_id: int, username: str, email: str, hashed_password: str, db: Session):
def update_user(user_id: int, user_update: UserUpdate, db: Session):
    # Find the user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update fields if provided
    # print("ce",user_upd/ate)
    # if username:
    #     user.username = username
    # if email:
    #     user.email = email
    # if hashed_password:
    #     user.hashed_password = hash_password(hashed_password)
    if user_update.username:
        user.username = user_update.username
    if user_update.email:
        user.email = user_update.email
    if user_update.password:
        user.hashed_password = hash_password(user_update.password)
    
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

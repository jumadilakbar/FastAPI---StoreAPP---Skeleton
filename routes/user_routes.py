from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from services.rbac import has_role
from services.user_service import create_user, get_users, get_user_by_id, delete_user, update_user
from schemas.user_schema import UserCreate, UserUpdate
from services.auth import hash_password
from models.user import User


router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user_endpoint(user:UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.email, user.password, user.role_id)

@router.get("/", dependencies=[Depends(has_role("admin"))])
def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}")
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user_endpoint(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    # user = db.query(User).filter(User.id == user_id).first()
    # if not user:
    #     raise HTTPException(status_code=404, detail="User not found")
    
    # # Update fields if provided
    # if user_update.username:
    #     user.username = user_update.username
    # if user_update.email:
    #     user.email = user_update.email
    # if user_update.password:
    #     user.hashed_password = hash_password(user_update.password)
    
    # db.commit()
    # db.refresh(user)
    # return {"message": "User updated successfully", "user": {"id": user.id, "username": user.username, "email": user.email}}
    # user = update_user(
    #     user_id, 
    #     user_update.username,
    #     user_update.email,
    #     user_update.password,
    #     db)
    user = update_user(user_id=user_id, user_update=user_update, db=db)
    return {
        "message": "User updated successfully",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role_id": user.role_id,
        }
    }
    
@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from models import Blog

router = APIRouter(prefix="/blogs", tags=["Blogs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_blog(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    blog = Blog(title=title, content=content, user_id=user_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

@router.get("/")
def get_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).all()

@router.get("/{blog_id}")
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.delete("/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}

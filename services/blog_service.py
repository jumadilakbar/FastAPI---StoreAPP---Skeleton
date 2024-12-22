from sqlalchemy.orm import Session
from models.blog import Blog

def create_blog(db: Session, title: str, content: str, user_id: int):
    blog = Blog(title=title, content=content, user_id=user_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_blogs(db: Session):
    return db.query(Blog).all()

def get_blog_by_id(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()

def delete_blog(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog:
        db.delete(blog)
        db.commit()
    return blog

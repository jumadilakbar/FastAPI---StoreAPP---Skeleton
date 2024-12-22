from sqlalchemy.orm import Session
from models.product import Product

def create_product(db: Session, name: str, price: int, description: str, store_id: int):
    product = Product(name=name, price=price, description=description, store_id=store_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product

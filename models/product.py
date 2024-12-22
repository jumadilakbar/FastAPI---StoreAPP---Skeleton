from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    description = Column(String)
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="products")

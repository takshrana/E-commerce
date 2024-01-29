from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Stone(db.Model):
    __tablename__ = "stone"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    product = relationship("Product", back_populates="stone")


class Metal(db.Model):
    __tablename__ = "metal"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    product = relationship("Product", back_populates="metal")


class Subcategory(db.Model):
    __tablename__ = "subcategory"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)

    product = relationship("Product", back_populates="subcategory")
    category = relationship("Category", back_populates="subcategory")


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    product = relationship("Product", back_populates="category")
    subcategory = relationship("Subcategory", back_populates="category")


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String())
    stock = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)
    subcategory_id = db.Column(db.Integer, ForeignKey("subcategory.id"))
    stone_id = db.Column(db.Integer, ForeignKey("stone.id"))
    metal_id = db.Column(db.Integer, ForeignKey("metal.id"))

    category = relationship("Category", back_populates="product")
    subcategory = relationship("Subcategory", back_populates="product")
    stone = relationship("Stone", back_populates="product")
    metal = relationship("Metal", back_populates="product")


class Price(db.Model):
    __tablename__ = "price"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    product_id = db.Column(db.Integer, ForeignKey("product.id"), nullable=False)

    product = relationship("Product")


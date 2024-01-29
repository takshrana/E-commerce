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
    category_id = db.Column(db.Integer, ForeignKey("category.id"))

    product = relationship("Product", back_populates="subcategory")
    category = relationship("Category", back_populates="subcategory")


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    product = relationship("Product", back_populates="category")
    subcategory =  relationship("Subcategory", back_populates="category")


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String())
    stock = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Integer)
    img_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)
    subcategory_id = db.Column(db.Integer, ForeignKey("subcategory.id"))
    stone_id = db.Column(db.Integer, ForeignKey("stone.id"))
    metal_id = db.Column(db.Integer, ForeignKey("metal.id"))

    category = relationship("Category", back_populates="product")
    subcategory = relationship("Subcategory", back_populates="product")
    stone = relationship("Stone", back_populates="product")
    metal = relationship("Metal", back_populates="product")

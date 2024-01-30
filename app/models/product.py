from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Style(db.Model):
    __tablename__ = "style"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)

    # product = relationship("Product", back_populates="stone")


class Metal(db.Model):
    __tablename__ = "metal"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)

    # product = relationship("Product", back_populates="metal")


# class Subcategory(db.Model):
#     __tablename__ = "subcategory"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)
#
#     product = relationship("Product", back_populates="subcategory")
#     category = relationship("Category", back_populates="subcategory")


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)

    # product = relationship("Product", back_populates="category")
    # subcategory = relationship("Subcategory", back_populates="category")


class Color(db.Model):
    __tablename__ = "color"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, default=1)
    price = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)
    style_id = db.Column(db.Integer, ForeignKey("style.id"))
    color_id = db.Column(db.Integer, ForeignKey("color.id"))
    metal_id = db.Column(db.Integer, ForeignKey("metal.id"))
    active = db.Column(db.Boolean, default=True)

    category = relationship("Category")
    # subcategory = relationship("Subcategory", back_populates="product")
    style = relationship("Style")
    color = relationship("Color")
    metal = relationship("Metal")


# class Price(db.Model):
#     __tablename__ = "price"
#
#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.DateTime, nullable=False)
#     product_id = db.Column(db.Integer, ForeignKey("product.id"), nullable=False)

    # product = relationship("Product")


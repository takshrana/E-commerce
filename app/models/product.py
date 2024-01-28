from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String())
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    category_id = db.Column(db.Integer, ForeignKey("category.id"))
    subcategory_id = db.Column(db.Integer, ForeignKey("subcategory.id"))


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Subcategory(db.Model):
    __tablename__ = "subcategory"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("category.id"))

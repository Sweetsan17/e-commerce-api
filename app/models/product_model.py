from unicodedata import decimal

from app.extensions import db


class Seller(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("sellers.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text(255), nullable=True)
    price = db.Column(db.Decimal(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        """Return a dictionary representation of the product."""
        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "name": self.name,
            "description": self.description,
            "price": decimal.Decimal(self.price) if self.price is not None else None,
            "stock": self.stock,
            "image": self.image,
            "is_active": self.is_active,
        }

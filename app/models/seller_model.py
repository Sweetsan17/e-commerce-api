from app.extensions import db
class Seller(db.Model):
    __tablename__="sellers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    shop_name = db.Column(db.String(120), nullable=False)
    phone=db.Column(db.String(20),nullable=True)
    address=db.Column(db.Text(255),nullable=True)
    
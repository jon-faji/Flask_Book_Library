### wishlist/models.py
from project import db  
from datetime import datetime

class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'book_id': self.book_id,
            'date_added': self.date_added.isoformat()
        }


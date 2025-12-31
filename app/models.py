from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class RepairOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    device = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    customer = db.relationship('Customer', backref=db.backref('repair_orders', lazy=True))
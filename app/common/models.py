from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from app import app

migrate=Migrate(app ,db)

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.username
    

@property
def password(self):
    """Reading the plaintext password value is not possible or allowed."""
    raise AttributeError("cannot read password")

@password.setter
def password(self, password):
    """
    Intercept writes to the `password` attribute and hash the given
    password value.
    """
    self._password = generate_password_hash(password)

def verify_password(self, password):
    """
    Accept a password and hash the value while comparing the hashed
    value to the password hash contained in the database.
    """
    return check_password_hash(self._password, password)


class AvailableSlot(db.Model):
    __tablename__ = 'available_slots'
    
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    is_cancelled = db.Column(db.Boolean, default=False)
    is_booked = db.Column(db.Boolean, default=False)


class Appointment(db.Model):
    __tablename__ = 'appointments'  
    id = db.Column(db.Integer, primary_key=True)
    available_slot_id = db.Column(db.Integer, db.ForeignKey('available_slots.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    is_visited = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    admin_feedback = db.Column(db.Text)



from datetime import datetime

from .. import db


class Fleet(db.Model):
    """ Fleet Model for storing fleet related details """
    __tablename__ = 'Fleet'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(45), default='active')
    users = db.relationship("User", back_populates="fleet", lazy="dynamic")
    vehicles = db.relationship("Vehicle", back_populates="fleet", lazy="dynamic")

    def __init__(self, name, status='active', registered_on=datetime.now()):
        self.name = name
        self.registered_on = registered_on
        self.status = status


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(45), nullable=False)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    email_confirmation_sent_on = db.Column(db.DateTime, nullable=True)
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmed_on = db.Column(db.DateTime, nullable=True)
    registered_on = db.Column(db.DateTime, nullable=True)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    current_logged_in = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String(45), default='user')
    fleet_id = db.Column(db.Integer, db.ForeignKey("Fleet.id"))
    fleet = db.relationship("Fleet", back_populates="users")

    #
    #
    # fleet = db.relationship("Fleet", back_populates="users")
    # fleet_id = db.Column(db.String(45), db.ForeignKey("Fleet.id"))

    def __init__(self, email, first_name, last_name, password, email_confirmation_sent_on=None, role='user',
                 fleet_id=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.authenticated = False
        self.email_confirmation_sent_on = email_confirmation_sent_on
        self.email_confirmed = False
        self.email_confirmed_on = None
        self.registered_on = datetime.now()
        self.last_logged_in = None
        self.current_logged_in = datetime.now()
        self.role = role
        self.fleet_id = fleet_id


class Vehicle(db.Model):
    """ Vehicle Model for storing vehicle related details """
    __tablename__ = "Vehicle"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    plate_number = db.Column(db.String(45), unique=True, nullable=False)
    fleet_id = db.Column(db.Integer, db.ForeignKey("Fleet.id"))
    fleet = db.relationship("Fleet", back_populates="vehicles")

    def __init__(self, model, plate_number):
        self.model = model
        self.plate_number = plate_number
        self.registered_on = datetime.now()

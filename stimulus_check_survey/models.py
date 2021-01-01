from werkzeug.security import generate_password_hash

from .extensions import db

member_stimulus_table = db.Table('member_stimulus',
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'), primary_key=True),
    db.Column('stimulus_id', db.Integer, db.ForeignKey('stimulus.id'), primary_key=True)
)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password_hash = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    birthdate = db.Column(db.DateTime)
    county = db.Column(db.ForeignKey('county.id'))
    address = db.Column(db.String(100))
    state = db.Column(db.String(50))
    annual_income_2019 = db.Column(db.String(50))
    work_income_reduction = db.Column(db.Boolean)
    comments = db.Column(db.Text)
    email_consent = db.Column(db.Boolean)

    stimulus_dollars_receieved = db.relationship(
        'Stimulus',
        secondary=member_stimulus_table,
        lazy=True,
        backref=db.backref('stimulus_dollars',lazy=True)
    )

    @property
    def password(self):
        raise AttributeError('Cannot view password')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Stimulus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(20))
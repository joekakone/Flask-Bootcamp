from app import db

class Url(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    long_url = db.Column(db.String(255))
    short_url = db.Column(db.String(50))
    created_date = db.Column(db.Date)

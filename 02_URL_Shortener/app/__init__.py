from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

# Import Views and Models
from app import views, models

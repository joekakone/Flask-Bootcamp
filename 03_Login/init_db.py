from app import app, db, bcrypt
from app.models import User


with app.app_context():
    db.create_all()

    try:
        password = bcrypt.generate_password_hash("1234").decode("utf-8")
        user = User(username="joekakone",
                    email="joseph.kakone@gmail.com",
                    password=password)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        pass

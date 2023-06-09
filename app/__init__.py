from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "Appointment.db"

def create_app():
    global app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .auth.controllers import auth_blueprint
    app.register_blueprint(
        auth_blueprint,
        url_prefix=f"/api/{auth_blueprint.url_prefix}",
    )

    from .common.controllers import common_blueprint
    app.register_blueprint(
        common_blueprint,
        url_prefix=f"/api/{common_blueprint.url_prefix}",
    )

    # from app.common.models import User, AvailableSlot , Appointment

    create_database()

    return app

def create_database():
    if not path.exists('app/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    if not os.path.exists("instance"):
        os.makedirs("instance")

    if not os.path.exists("instance/tasks.db"):
        open("instance/tasks.db", "w").close()

    db.init_app(app)
    csrf.init_app(app)

    from app.views import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
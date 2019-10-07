from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import ProductionConfig

db = SQLAlchemy()

app = Flask(__name__)


def create_app():
    app.config.from_object(ProductionConfig)
    db.init_app(app)
    return app

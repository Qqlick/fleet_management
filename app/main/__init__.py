from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import ProductionConfig

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(ProductionConfig)
db.init_app(app)


def create_app():
    return app

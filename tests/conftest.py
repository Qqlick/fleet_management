import pytest

from app import blueprint
from app.main import app


@pytest.fixture
def client():
    app.register_blueprint(blueprint)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

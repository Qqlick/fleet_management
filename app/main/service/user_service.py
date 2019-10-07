from app.main import db
from app.main.model.models import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(**data)
        save_changes(new_user)
        return new_user
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    r =  User.query.filter_by(id=public_id).first()
    return r


def save_changes(data):
    db.session.add(data)
    db.session.commit()


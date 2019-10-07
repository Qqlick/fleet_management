from app.main import db


class Dbservices:
    name = "name"
    id_name = "id"
    model = db.Model

    def __init__(self, data=None, public_id=None):
        self.data = data
        self.public_id = public_id

    def save_new_item(self):
        item = self.model.query.filter_by(
            **{self.name: self.data.get(self.name)}
        ).first()
        if not item:
            new_item = self.model(**self.data)
            self.save_changes(new_item)
            return new_item
        else:
            response_object = {
                "status": "fail",
                "message": "{} already exists.".format(self.model.__tablename__),
            }
            return response_object, 409

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    def get_an_item(self):
        return self.model.query.filter_by(**{self.id_name: self.public_id}).first()

    @staticmethod
    def save_changes(data):
        db.session.add(data)
        db.session.commit()

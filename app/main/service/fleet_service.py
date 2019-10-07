from app.main import db
from app.main.model.models import Fleet
from app.main.service.common_services import Dbservices


class FleetServices(Dbservices):
    name = "name"
    model = Fleet
    id_name = "id"

#
# def save_new_fleet(data):
#     fleet = Fleet.query.filter_by(name=data['name']).first()
#     if not fleet:
#         new_fleet = Fleet(**data)
#         save_changes(new_fleet)
#         return new_fleet
#     else:
#         response_object = {
#             'status': 'fail',
#             'message': 'Fleet already exists.',
#         }
#         return response_object, 409
#
#
# def get_all_fleets():
#     return Fleet.query.all()
#
#
# def get_a_fleet(public_id):
#     return Fleet.query.filter_by(id=public_id).first()
#
#
# def save_changes(data):
#     db.session.add(data)
#     db.session.commit()
#

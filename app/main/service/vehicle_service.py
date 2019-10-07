from app.main.model.models import Vehicle
from app.main.service.common_services import Dbservices


class VehicleServices(Dbservices):
    model = Vehicle
    id_name = 'id'
    name = 'id'

from app.main.model.models import Fleet
from app.main.service.common_services import Dbservices


class FleetServices(Dbservices):
    name = "name"
    model = Fleet
    id_name = "id"

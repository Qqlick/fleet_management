from app.main.model.models import User
from app.main.service.common_services import Dbservices


class UserServices(Dbservices):
    model = User
    id_name = 'id'
    name = 'email'

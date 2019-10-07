from flask_restplus import Api
from flask import Blueprint

from app.main.controller.user_controller import api as user_ns
from app.main.controller.fleet_controller import api as fleet_ns
from app.main.controller.vehicle_controller import api as vehicle_ns

blueprint = Blueprint("api", __name__)

api = Api(blueprint, title="FLEET MANAGEMENT API", version="1.0.0", description="")

api.add_namespace(user_ns, path="/user")
api.add_namespace(fleet_ns, path="/fleet")
api.add_namespace(vehicle_ns, path="/vehicle")

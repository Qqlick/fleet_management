from flask import request
from flask_restplus import Resource

from app.main.service.vehicle_service import VehicleServices
from app.main.util.vehicle_dto import VehicleDto

api = VehicleDto.api


@api.route("/")
class VehicleList(Resource):
    @api.doc("list_of_registered_vehicles")
    @api.marshal_list_with(VehicleDto.vehicle_req, envelope="data", code=200)
    def get(self):
        """List all registered users"""
        return VehicleServices.get_all()

    @api.expect(VehicleDto.vehicle_req, validate=True)
    @api.response(201, "Vehicle successfully created.")
    @api.doc("create a new vehicle")
    @api.marshal_with(VehicleDto.vehicle_resp, code=201)
    def post(self):
        """Creates a new Vehicle """
        data = request.json
        return VehicleServices(data=data).save_new_item()


@api.route("/<vehicle_id>")
@api.param("vehicle_id", "The Vehicle identifier")
@api.response(404, "Vehicle not found.")
class Vehicle(Resource):
    @api.doc("get a vehicle")
    @api.marshal_with(VehicleDto.vehicle_resp, skip_none=True)
    def get(self, vehicle_id):
        """get a vehicle given its identifier"""
        vehicle = VehicleServices(public_id=vehicle_id).get_an_item()
        if not vehicle:
            api.abort(404)
        else:
            return vehicle

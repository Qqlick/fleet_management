from flask import request
from flask_restplus import Resource

from app.main.service.fleet_service import FleetServices
from app.main.util.fleet_dto import FleetDto

api = FleetDto.api


@api.route("/")
class FleetList(Resource):
    @api.doc("list_of_fleets")
    @api.marshal_list_with(FleetDto.fleet_resp, envelope="data")
    def get(self):
        """List all registered fleets"""
        return FleetServices.get_all()

    @api.expect(FleetDto.fleet, validate=True)
    @api.response(201, "Fleet successfully created.")
    @api.doc("create a new fleet")
    @api.marshal_with(FleetDto.fleet_resp, code=201)
    def post(self):
        """Creates a new Fleet """
        data = request.json
        return FleetServices(data=data).save_new_item()


@api.route("/<fleet_id>")
@api.param("fleet_id", "The Fleet identifier")
@api.response(404, "Fleet not found.")
class Fleet(Resource):
    @api.doc("get a fleet")
    @api.marshal_with(FleetDto.fleet_detailed)
    def get(self, fleet_id):
        """get a fleet given its identifier"""
        fleet = FleetServices(public_id=fleet_id).get_an_item()
        if not fleet:
            api.abort(404)
        else:
            return fleet

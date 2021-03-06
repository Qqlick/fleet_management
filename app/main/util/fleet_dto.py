from flask_restplus import Namespace, fields

from app.main.util.user_dto import UserDto
from app.main.util.vehicle_dto import VehicleDto


class FleetDto:
    api = Namespace("fleet", description="fleet related operations")
    fleet = api.model(
        "Fleet_request",
        {
            "registered_on": fields.DateTime(description="fleet register datetime"),
            "name": fields.String(required=True, description="fleet name"),
            "status": fields.String(description="Fleet status", default="active"),
        },
    )
    fleet_resp = api.model(
        "Fleet_resp",
        {
            "registered_on": fields.DateTime(description="fleet register datetime"),
            "name": fields.String(description="fleet name"),
            "status": fields.String(description="fleet status"),
            "fleet_id": fields.String(attribute="id"),
        },
    )

    fleet_detailed = api.inherit(
        "Fleet_detailed",
        fleet_resp,
        {
            "users": fields.List(fields.Nested(UserDto.user_resp, skip_none=True)),
            "vehicles": fields.List(
                fields.Nested(VehicleDto.vehicle_resp, skip_none=True)
            ),
        },
    )

from flask_restplus import Namespace, fields


class VehicleDto:
    api = Namespace("vehicle", description="vehicle related operations")
    vehicle_req = api.model(
        "Vehicle_req",
        {
            "model": fields.String(required=True, description="vehicle model"),
            "plate_number": fields.String(
                required=True, description="vehicle plate number"
            ),
            "fleet_id": fields.Integer(description="fleet id"),
        },
    )

    vehicle_resp = api.inherit(
        "Vehicle_resp",
        vehicle_req,
        {"registered_on": fields.DateTime(description="user email address")},
    )

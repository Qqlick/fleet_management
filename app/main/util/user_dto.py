from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace("user", description="user related operations")
    user_req = api.model(
        "User_req",
        {
            "email": fields.String(required=True, description="user email address"),
            "first_name": fields.String(required=True, description="user first_name"),
            "last_name": fields.String(required=True, description="user last_name"),
            "password": fields.String(required=True, description="user password"),
            "fleet_id": fields.Integer(description="fleet id"),
        },
    )
    user_resp = api.model(
        "User_resp",
        {
            "email": fields.String(description="user email address"),
            "first_name": fields.String(description="user first_name"),
            "last_name": fields.String(description="user last_name"),
            "user_id": fields.String(attribute="id"),
        },
    )

    # import app.main.util.fleet_dto
    # user_detailed = user_resp.clone('User_detailed', {
    #     'fleet': fields.Nested(app.main.util.fleet_dto.FleetDto.fleet_resp, skip_none=True)
    # })

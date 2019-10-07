from flask import request
from flask_restplus import Resource

from app.main.service.user_service import UserServices
from app.main.util.user_dto import UserDto

api = UserDto.api


@api.route("/")
class UserList(Resource):
    @api.doc("list_of_registered_users")
    @api.marshal_list_with(UserDto.user_resp, envelope="data", code=200)
    def get(self):
        """List all registered users"""
        return UserServices.get_all()

    @api.expect(UserDto.user_req, validate=True)
    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    @api.marshal_with(UserDto.user_resp, code=201)
    def post(self):
        """Creates a new User """
        data = request.json
        return UserServices(data=data).save_new_item()


@api.route("/<user_id>")
@api.param("user_id", "The User identifier")
@api.response(404, "User not found.")
class User(Resource):
    @api.doc("get a user")
    @api.marshal_with(UserDto.user_resp, skip_none=True)
    def get(self, user_id):
        """get a user given its identifier"""
        user = UserServices(public_id=user_id).get_an_item()
        if not user:
            api.abort(404)
        else:
            return user

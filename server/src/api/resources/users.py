from flask import Blueprint
from flask_restful import Resource, Api

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

class UsersResource(Resource):
  def get(self):
    return {
      'status': 'success'
    }

api.add_resource(UsersResource, '/users')
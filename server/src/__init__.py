import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# app instantiation
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

# import user model
from src.models.users import User

api = Api(app)

# example log
# import sys
# print(app.config, file=sys.stderr)
# can be accessed by docker-compose logs if running docker-compose up with -d argument (running in background)


class UsersResource(Resource):
  def get(self):
    return {
      'status': 'success'
    }


api.add_resource(UsersResource, '/users')
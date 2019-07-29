import os

from flask import Flask  # new
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(script_info=None):
  # app instantiation
  app = Flask(__name__)
  
  # set config
  app_settings = os.getenv('APP_SETTINGS')
  app.config.from_object(app_settings)
  
  # instantiate the db
  db.init_app(app)
  
  # import + register blueprints
  from src.api.resources.users import users_blueprint
  app.register_blueprint(users_blueprint)
  
  # shell context for flask cli
  
  @app.shell_context_processor
  def ctx():
      return {'app': app, 'db': db}

  return app
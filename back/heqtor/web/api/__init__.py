from flask import Blueprint
from flask_restful import Api

from heqtor.core import db, Session
from heqtor.web import app

from .me import Me, MeCompany

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(Me, "/me")
api.add_resource(MeCompany, "/me/company")

app.register_blueprint(api_bp, url_prefix="/api")

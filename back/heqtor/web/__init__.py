from flask import Flask
from flask_cors import CORS
from json import JSONEncoder

from heqtor.core import config

flask_config = config["flask_app"]

app = Flask(flask_config["name"])
app.config["ENV"] = flask_config["env"]
app.config["DEBUG"] = flask_config["debug"]
app.config["JWT_SECRET_KEY"] = flask_config["jwt_key"]
app.config["RESTFUL_JSON"] = {"cls": JSONEncoder}
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = flask_config["jwt_expires"]

CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)

from . import auth
from . import api

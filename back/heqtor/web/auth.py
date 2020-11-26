import hashlib

from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from heqtor.core import Session
from heqtor.models.user import User
from heqtor.web import app

jwt = JWTManager(app)
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    # get user infos from request
    user_infos = dict()
    user_infos["email"] = request.json["email"]
    hash = hashlib.sha256()
    hash.update(request.json["password"].encode())
    password = hash.hexdigest()
    user_infos["password"] = password
    user_infos["first_name"] = request.json["first_name"]
    user_infos["last_name"] = request.json["last_name"]
    user_infos["phone"] = request.json["phone"]

    session = Session()
    try:
        # create user
        user = User(**user_infos)
        session.add(user)
        session.query(User).filter(User.email == user_infos["email"]).one()
        # create access token from user infos
        user_data = user.get_small_data()
        access_token = create_access_token(identity=user_data)
        user_data["access_token"] = access_token
        session.commit()
    except IntegrityError:
        session.rollback()
        return jsonify({"error": f"User {user_infos['email']} already exists"}), 400
    except:
        session.rollback()
        return jsonify({"error": "An unexpected error occured"}), 500
    finally:
        session.close()

    return jsonify(**user_data), 200


@auth_bp.route("/login", methods=["POST"])
def login():
    # get user infos from request
    email = request.json["email"]
    hash = hashlib.sha256()
    hash.update(request.json["password"].encode())
    password = hash.hexdigest()

    session = Session()
    try:
        # get user matching login infos
        user = (
            session.query(User).filter(User.email == email, User.password == password).one()
        )
        # create access token from user infos
        user_data = user.get_small_data()
        access_token = create_access_token(identity=user_data)
        user_data["access_token"] = access_token
    except NoResultFound:
        session.rollback()
        return (
            jsonify({"error": "Unknown email / Email and password not matching"}),
            403,
        )
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"error": "An unexpected error occured"}), 500
    finally:
        session.close()

    return jsonify(**user_data), 200


app.register_blueprint(auth_bp, url_prefix="/auth")

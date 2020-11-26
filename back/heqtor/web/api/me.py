from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from heqtor.controllers import get_user


class Me(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()["id"]
        return get_user(user_id)

    @jwt_required
    #route to update user profile
    def post(self):
        try:
            user_id = get_jwt_identity()["id"]
            phone = request.json["phone"]
            return update_user_data(user_id, phone)
        except :
            return False
        # TODO
        # hint : data from post request is located in flask object request.json
        # pass



class MeCompany(Resource):
    @jwt_required
    def get(self):
        company_id = get_jwt_identity()["id"]
        return get_company_byId(company_id)

    @jwt_required
    def post(self):
        try : 
            company_id = get_jwt_identity()["id"]
            phone = request.json["phone"]
            return update_company_data(company_id, phone)
        except :
            return False
  
    # TODO
    # get, post, delete
    # pass



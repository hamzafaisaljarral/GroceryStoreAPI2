from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from database.models import User
import datetime

from resources.errors import unauthorized, user_exist


class SignupApi(Resource):
    def post(self):
        """
        POST response method for creating user.
        :return: JSON object
        """
        data = request.get_json()
        try:
            User.objects.get(email=data.get('email'))
        except:
            post_user = User(**data)
            post_user.save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        return user_exist()


class LoginApi(Resource):
    def post(self):
        data = request.get_json()
        user = User.objects.get(email=data.get('email'))
        auth_success = user.check_pw_hash(data.get('password'))
        if not auth_success:
            return unauthorized()
        else:
            expiry = datetime.timedelta(days=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
            refresh_token = create_refresh_token(identity=str(user.id))
            return jsonify({'result': {'access_token': access_token,
                                       'refresh_token': refresh_token,
                                       'logged_in_as': f"{user.email}"}})


import datetime

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from flask_restful import Api
from flask_cors import CORS
from database.db import initialize_db
from resources.routes import initialize_routes


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'aSuperSecretKey'
app.config['MONGODB_SETTINGS'] = 'mongodb+srv://hamza:I3AsKagslibNCK6C@cluster0.48mgg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'


# app.config['JWT_TOKEN_LOCATION'] = 'cookies'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app)
cors = CORS(app, resources={r'/*': { 'origins': '*' }})
initialize_db(app)
initialize_routes(api)















# import hashlib
# import datetime
# import pymongo
# from flask import Flask, request, jsonify
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
#
#
# app = Flask(__name__)
# jwt = JWTManager(app)
# app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
#
# client = pymongo.MongoClient("mongodb://hamza:<pas7EzPFk9QF8nL>@cluster0.48mgg.mongodb.net/mydatabase?retryWrites=true&w=majority")  # your connection string
# db = client["demo"]
# users_collection = db["users"]
#
#
# @app.route("/api/v1/register", methods=["POST"])
# def register():
#     new_user = request.get_json()  # store the json body request
#     new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest()  # encrpt password
#     doc = users_collection.find_one({"username": new_user["username"]})  # check if user exist
#     if not doc:
#         users_collection.insert_one(new_user)
#         return jsonify({'msg': 'User created successfully'}), 201
#     else:
#         return jsonify({'msg': 'Username already exists'}), 409
#
#
# @app.route("/api/v1/login", methods=["POST"])
# def login():
#     login_details = request.get_json()  # store the json body request
#     user_from_db = users_collection.find_one({'username': login_details['username']})  # search for user in database
#
#     if user_from_db:
#         encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
#         if encrpted_password == user_from_db['password']:
#             access_token = create_access_token(identity=user_from_db['username'])  # create jwt token
#             return jsonify(access_token=access_token), 200
#
#     return jsonify({'msg': 'The username or password is incorrect'}), 401
#
#
# @app.route("/api/v1/user", methods=["GET"])
# @jwt_required
# def profile():
#     current_user = get_jwt_identity()  # Get the identity of the current user
#     user_from_db = users_collection.find_one({'username': current_user})
#     if user_from_db:
#         del user_from_db['_id'], user_from_db['password']  # delete data we don't want to return
#         return jsonify({'profile': user_from_db}), 200
#     else:
#         return jsonify({'msg': 'Profile not found'}), 404
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

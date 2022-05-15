import csv
import json

import os

from flask import request, jsonify, Response
from flask_restful import Resource

from database.models import User, Product,ProductReview
from .errors import forbidden, not_found
from flask_jwt_extended import jwt_required, get_jwt_identity


ALLOWED_EXTENSIONS = 'csv'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class ADDProductAPI(Resource):
    @jwt_required()
    def post(self):
        authorized: bool = User.objects.get(id=get_jwt_identity()).role.admin

        if authorized:
            # check if the post request has the file part
            if 'file' not in request.files:
                resp = jsonify({'message': 'No file part in the request'})
                resp.status_code = 400
                return resp

            file = request.files['file']
            if file.filename == '':
                resp = jsonify({'message': 'No file selected for uploading'})
                resp.status_code = 400
                return resp
            if file and allowed_file(file.filename):
                files = request.files['file']
                files.save(os.path.join('./', files.filename))
                with open(os.path.join('./', files.filename), 'r') as file:
                    check = csv.DictReader(file)
                    for each in check:
                        product = Product(**each, __auto_convert=True).save()
                resp = jsonify({'message': 'File successfully uploaded'})
                resp.status_code = 201
                return resp
            else:
                resp = jsonify({'message': 'Allowed file types are csv'})
                resp.status_code = 400
                return resp
        else:
            return forbidden()


class ADDProductReviewAPI(Resource):
    @jwt_required()
    def post(self):
        authorized: bool = User.objects.get(id=get_jwt_identity())

        if authorized:
            # check userid
            data = request.get_json()
            barcode = data.get('barcode')
            review = ProductReview(userID=authorized.id, barcode=barcode, review=data.get('review'))
            try:
                product = Product.objects.filter(barcode=barcode).first()
                product.review = review
                product.save()
                resp = jsonify({'message': 'review added'
                               })
                resp.status_code = 200
                return resp
            except:
                return not_found()

        return forbidden()


class ProductSearchAPI(Resource):
    @jwt_required()
    def post(self):
        authorized: bool = User.objects.get(id=get_jwt_identity())

        if authorized:
            page = int(request.args.get('page', 0))
            data = request.get_json()
            text = data.get('text')
            products = Product.objects(name__contains=text).filter(available=True)[:10]
            data = [{'totalCount': len(products)}] + [i.serializer for i in products]
            response = data
            return response, 200

        return forbidden()






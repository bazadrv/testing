from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pandas as pd

rest = Flask(__name__)
api = Api(rest)


class Train(Resource):
    def __init__(self):
        pass

    def get(self):
        pass

    def post(self):
        file = request.files['data.txt']
        with open(file, mode='r'):
            text = file.read()
        return text


class Form(Resource):
    def __init__(self):
        pass

    def get(self):
        pass

    def post(self):
        json_data = request.get_json()
        user_name = json_data['username']
        password = json_data['password']
        return jsonify(u=user_name + "id", p=password + "name")


api.add_resource(Form, '/form')
api.add_resource(Train, '/')

if __name__ == '__main__':
    rest.run(debug=True, port=4000)

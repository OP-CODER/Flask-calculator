from flask import request
from flask_restful import Resource

class Add(Resource):
    def post(self):
        data = request.get_json()
        return {
            "Message": data["x"] + data["y"],
            "Status Code": 200
        }

class Subtract(Resource):
    def post(self):
        data = request.get_json()
        return {
            "Message": data["x"] - data["y"],
            "Status Code": 200
        }

class Multiply(Resource):
    def post(self):
        data = request.get_json()
        return {
            "Message": data["x"] * data["y"],
            "Status Code": 200
        }

class Divide(Resource):
    def post(self):
        data = request.get_json()
        try:
            result = data["x"] / data["y"]
        except ZeroDivisionError:
            return {
                "Message": "Division by zero error",
                "Status Code": 400
            }
        return {
            "Message": result,
            "Status Code": 200
        }

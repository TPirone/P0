from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class customer(Resource):
    pass

class account(Resource):
    pass


api.add_resource(customer, '/customer')
api.add_resource(account, '/account')

if __name__ == "__main__":
    app.run()
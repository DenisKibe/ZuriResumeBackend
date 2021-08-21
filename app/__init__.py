from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app=Flask(__name__)

#init CORS
CORS(app)

from app.route import initialize_routes

#init Api
api = Api(app)

initialize_routes(api)
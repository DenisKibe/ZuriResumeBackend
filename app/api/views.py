from flask import json,Response,request
from flask_restful import Resource

class GetDataAndSave(Resource):
    def post(self):
        post_data = request.get_json()

        try: 
            with open('zuridata.json','a') as f:
                json.dump({'firstname':post_data.get('firstname'),'lastname':post_data.get('lastname'),'phone':post_data.get('phone'),'email':post_data.get('email'),'message':post_data.get('message')}, f)

            return Response(json.dumps({'Status':'Success'}),mimetype='application/json',status=200)
        except Exception as e:
            #log the error

            return Response(json.dumps({'Status':'Error'}),mimetype='application/json',status=400)
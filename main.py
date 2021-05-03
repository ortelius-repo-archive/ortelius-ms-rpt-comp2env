import os

import psycopg2
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

PRESIDENTS = {
    'india' : 'modi',
    'usa' : 'trump',
    'russia' : 'putin'
}

# Init db connection
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "postgres")
db_user = os.getenv("DB_USER", "postgres")
db_pass = os.getenv("DB_PASS", "postgres")

#conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)

class PresidentList(Resource): 
    def get(self): 
        return {'presidents':PRESIDENTS},200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('country', required=True)
        parser.add_argument('president', required=True)
        args = parser.parse_args()
        if args['country'] in PRESIDENTS:
            abort(404, message="Country {} already exists".format(args['country']))
        PRESIDENTS[args['country']] = args['president']
        return {'status':'success'},201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('country', required=True)
        parser.add_argument('president', required=True)
        args = parser.parse_args()
        if args['country'] not in PRESIDENTS:
            PRESIDENTS[args['country']] = args['president']
            return {'status':'success'},201
        PRESIDENTS[args['country']] = args['president']
        return {'status':'success'},200


class President(Resource): 
    def get(self, country):
        if country not in PRESIDENTS:
            abort(404, message="Country {} doesn't exist".format(country))
        return {"{}".format(country):PRESIDENTS[country]},200 
    
    def delete(self, country):
        if country not in PRESIDENTS:
            abort(404, message="Country {} doesn't exist".format(country))
        del PRESIDENTS[country]
        return {'status':'success'},200


api.add_resource(PresidentList, '/presidents')
api.add_resource(President, '/presidents/<country>')

if __name__ == '__main__':
    if (os.getenv('FLASK_DEV_ENV', None) is not None):
        app.run(host="127.0.0.1", port=5000)
    else:
        app.run(host="127.0.0.1", port=5000)


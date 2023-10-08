import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Bird

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tonan:x0uckzjcMFsDzKBWyCfGaTGdwPsrdLg4@dpg-ckhfc5eafg7c73dmlbd0-a.ohio-postgres.render.com/bird_app_n70j'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    
    def get(self):
        return {'message': 'Welcome!'}, 200

class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

class BirdByID(Resource):
    def get(self, id):
        bird = Bird.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(bird), 200)


api.add_resource(Home, '/')
api.add_resource(Birds, '/birds')
api.add_resource(BirdByID, '/birds/<int:id>')
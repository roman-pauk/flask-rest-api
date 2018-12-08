from flask import Flask
from flask_restful import Api

# from flask_sqlalchemy import SQLAlchemy

from resources.festival import FestivalList, Festival
from resources.performer import PerformerList, Performer


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\\python-flask-api\\db\\database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

# dbs = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(FestivalList, '/festivals')
api.add_resource(Festival, '/festival/<string:festival_id>')

api.add_resource(PerformerList, '/performers')
api.add_resource(Performer, '/performer/<string:performer_id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
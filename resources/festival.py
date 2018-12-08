from flask_restful import Resource, reqparse
from models.festival import FestivalModel
from models.performer import PerformerModel

class Festival(Resource):
    def get(self, festival_id):
        festival = FestivalModel.find_by_id(festival_id)

        if festival:
            return festival.json()
        return {'message': 'Festival not found'}, 404

    def delete(self, festival_id):
        festival = FestivalModel.find_by_id(festival_id)
        if festival:
            festival.delete_from_db()

        return {'message': 'Festival deleted'}

    def put(self, festival_id):
        festival = FestivalModel.find_by_id(festival_id)

        if not festival:
            return {'message': 'Festival with id {} not found'.format(festival_id)}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        data = parser.parse_args()

        if festival.performers:
            for prf in festival.performers:
                if prf.performer_id == data['user_id']:
                    return {'message': 'Performer with id {} is already added'.format(data['user_id'])}, 404

        performer = PerformerModel.find_by_id(data['user_id'])

        if performer:
            festival.add_performer(performer)
            return festival.json()
        
        return {'message': 'Performer with id {} not found'.format(data['user_id'])}, 404
        


class FestivalList(Resource):
    def get(self):
        return {'festivals': list(map(lambda x: x.json(), FestivalModel.query.all()))}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('logo', type=str, required=True)

        data = parser.parse_args()

        festival = FestivalModel(**data)
        
        try:
            festival.save_to_db()
        except:
            return {"message": "An error occurred creating a festival"}, 500

        return festival.json(), 201


from flask_restful import Resource, reqparse
from models.performer import PerformerModel

class Performer(Resource):
    def get(self, performer_id):
        performer = PerformerModel.find_by_id(performer_id)
        if performer:
            return performer.json()
        return {'message': 'Performer not found'}, 404

    def delete(self, performer_id):
        performer = PerformerModel.find_by_id(performer_id)
        if performer:
            performer.delete_from_db()

        return {'message': 'Performer deleted'}


class PerformerList(Resource):
    def get(self):
        return {'performers': list(map(lambda x: x.json(), PerformerModel.query.all()))}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('logo', type=str, required=True)

        data = parser.parse_args()

        performer = PerformerModel(**data)
        
        try:
            performer.save_to_db()
        except:
            return {"message": "An error occurred creating a performer"}, 500

        return performer.json(), 201

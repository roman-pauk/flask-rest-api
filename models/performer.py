from db import db

from models.subscriber import subs

class PerformerModel(db.Model):
    __tablename__ = 'performers'

    performer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    logo = db.Column(db.String(80))
    festivals = db.relationship('FestivalModel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

    def __init__(self, name, logo):
        self.name = name
        self.logo = logo

    def json_sm(self):
        return {
            'id': self.performer_id,
            'name': self.name,
            'logo': self.logo
        }
    
    def json(self):
        return {
            'id': self.performer_id,
            'name': self.name,
            'logo': self.logo,
            'festivals': [festival.json_sm() for festival in self.festivals]
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(performer_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
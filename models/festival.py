from db import db

from models.subscriber import subs

class FestivalModel(db.Model):
    __tablename__ = 'festivals'

    festival_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    logo = db.Column(db.String(80))
    performers = db.relationship('PerformerModel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

    def __init__(self, name, logo):
        self.name = name
        self.logo = logo

    def json_sm(self):
        return {
            'id': self.festival_id,
            'name': self.name,
            'logo': self.logo
        }

    def json(self):
        print(self.performers)
        return {
            'id': self.festival_id,
            'name': self.name,
            'logo': self.logo,
            'performers': [performer.json_sm() for performer in self.performers]
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(festival_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_performer(self, performer):
        self.performers.append(performer)
        db.session.add(self)
        db.session.commit()
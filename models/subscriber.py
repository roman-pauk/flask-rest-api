from db import db

subs = db.Table('subs',
    db.Column('performer_id', db.Integer, db.ForeignKey('performers.performer_id')),
    db.Column('festival_id', db.Integer, db.ForeignKey('festivals.festival_id'))
)
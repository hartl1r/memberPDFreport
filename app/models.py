# app/models.py

from app import db


class Member(db.Model):
    __tablename__ = 'tblMember_Data'

    #id = db.Column(db.Integer)
    member_id = db.Column(db.String(6), primary_key=True, unique=True, nullable=False)
    last_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return '<Member %r>' % self.member_id


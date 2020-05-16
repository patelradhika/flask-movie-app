"""
----------------------------------- Imports -----------------------------------
"""
from movie import db


"""
----------------------------------- Models ------------------------------------
"""
class Movies(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    pic = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def __init__(self, name, pic, rating, notes):
        self.name = name
        self.pic = pic
        self.rating = rating
        self.notes = notes

    def __repr__(self):
        return f"Movie: {self.name}"
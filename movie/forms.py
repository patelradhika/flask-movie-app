"""
----------------------------------- Imports -----------------------------------
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, ValidationError, NumberRange


"""
------------------------------------ Forms ------------------------------------
"""
class SearchForm(FlaskForm):
    search = StringField()
    submit = SubmitField("Search")


class MovieForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    pic = StringField("Picture")
    rating = FloatField("Rating", validators=[DataRequired(), NumberRange(1,5)])
    notes = TextAreaField("Movie Notes")
    create = SubmitField("Create")

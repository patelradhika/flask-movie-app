"""
----------------------------------- Imports -----------------------------------
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


"""
------------------------------------ Forms ------------------------------------
"""
class SearchForm(FlaskForm):
    search = StringField()
    submit = SubmitField("Search")
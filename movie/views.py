"""
----------------------------------- Imports -----------------------------------
"""
from flask import render_template, Blueprint, request

from movie import db
from movie.forms import SearchForm
from movie.models import Movies


"""
----------------------------------- Blueprint ---------------------------------
"""
core = Blueprint("core", __name__)

"""
------------------------------------ Views ------------------------------------
"""
@core.route('/')
def home():
    form = SearchForm()
    movies = Movies.query.all()
    return render_template('home.html', movies=movies, form=form)
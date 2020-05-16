"""
----------------------------------- Imports -----------------------------------
"""
from flask import render_template, Blueprint, request, redirect, url_for

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


@core.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        form = SearchForm()
        search = form.search.data

        movies = Movies.query.filter(Movies.name.contains(search)).all()
        form.search.data = ""

        return render_template('home.html', form=form, movies=movies)
    else:
        return redirect(url_for('core.home'))
"""
----------------------------------- Imports -----------------------------------
"""
from flask import render_template, Blueprint, request, redirect, url_for, flash

from movie import db
from movie.forms import SearchForm, MovieForm
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
    Search = SearchForm()
    Create = MovieForm()
    Edit = MovieForm()
    movies = Movies.query.all()
    return render_template('home.html', movies=movies, Search=Search, Create=Create, Edit=Edit)


@core.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        Search = SearchForm()
        Create = MovieForm()
        Edit = MovieForm()
        
        search = Search.search.data

        movies = Movies.query.filter(Movies.name.contains(search)).all()
        Search.search.data = ""

        return render_template('home.html', movies=movies, Search=Search, Create=Create, Edit=Edit)
    
    else:
        return redirect(url_for('core.home'))


@core.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        form = MovieForm()

        if form.validate_on_submit():
            name = form.name.data
            rating = form.rating.data
            pic = form.pic.data or "http://gearr.scannain.com/wp-content/uploads/2015/02/noposter.jpg"
            notes = form.notes.data or None

            movie = Movies(name=name, pic=pic, rating=rating, notes=notes)
            db.session.add(movie)
            db.session.commit()
            flash(u"Successfully Created Movie: {}".format(movie.name), "success")

        else:
            flash(u"Movie not created due to incorrect data. Please re-enter valid data.", "danger")

        return redirect(url_for('core.home'))

    else:
        return redirect(url_for('core.home'))


@core.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    messages = []

    if request.method == 'POST':
        form = MovieForm()
        movie = Movies.query.get(id)

        if form.validate_on_submit():
            movie.name = form.name.data
            movie.rating = form.rating.data
            movie.pic = form.pic.data
            movie.notes = request.form.get('notes') or movie.notes
            db.session.commit()
            flash(u"Successfully Updated Movie: {}".format(movie.name), "success")

        else:
            flash(u"Movie details not edited due to incorrect data. Please re-edit with valid data.", "danger")

        return redirect(url_for('core.home'))

    else:
        return redirect(url_for('core.home'))


@core.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    messages = []

    if request.method == 'POST':
        movie = Movies.query.get(id)
        db.session.delete(movie)
        db.session.commit()

        flash(u"Successfully Deleted Movie: {}".format(movie.name), "success")
        return redirect(url_for('core.home'))

    else:
        return redirect(url_for('core.home'))
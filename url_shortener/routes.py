from flask import Blueprint, request, redirect, render_template
from url_shortener import db
from url_shortener.models import Link
import re

url_shortener = Blueprint('url_shortener', __name__)


@url_shortener.route('/')
def index():
    return render_template('index.html')


@url_shortener.route('/<string:short_url>', methods=['GET'])
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    link.visits += 1
    db.session.commit()

    return redirect(link.original_url)


@url_shortener.route('/add_link', methods=['POST'])
def add_link():
    if request.method == 'POST':
        original_url = request.form['original_url']
        link = Link(original_url=original_url)

        db.session.add(link)
        db.session.commit()

        return render_template('link_added.html', new_link= request.host_url + link.short_url, original_url=link.original_url)


@url_shortener.route('/stats')
def stats():
    links = Link.query.all()    
    return render_template('stats.html', links=links)


@url_shortener.errorhandler(404)
def page_not_found(e):
    return '', 404
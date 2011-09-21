"""
Flask Blueprint Docs:  http://flask.pocoo.org/docs/api/#flask.Blueprint

This file is used for both the routing and logic of your
application.
"""

import random
from textwrap import dedent
from flask import Blueprint, render_template, request, jsonify
from paragraphs import PARAGRAPHS

views = Blueprint('views', __name__, static_folder='../static')


@views.route('/')
def index():
    """Render website's index page."""
    return render_template('home.html')


@views.route('/generate')
def generate():
    """Generate JSON Abhi Ipsum paragraphs."""
    if 'paragraphs' in request.args:
        number_of_paragraphs = int(request.args['paragraphs'])
    else:
        number_of_paragraphs = 2
    if 'tags' in request.args and request.args['tags'] == 'yes':
        tags = True
    else:
        tags = False
    paragraph_list = [format_paragraph(random.choice(PARAGRAPHS), tags)
                      for number in xrange(number_of_paragraphs)]
    return jsonify({'paragraphs': paragraph_list})


def format_paragraph(paragraph, tags=False):
    """Properly format a paragraph."""
    formatted_paragraph = dedent(paragraph).strip().replace('\n', ' ')
    if tags:
        formatted_paragraph = '<p>' + formatted_paragraph + '</p>'
    return formatted_paragraph


# The functions below should be applicable to all Flask apps.

@views.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return views.send_static_file(file_dot_text)


@views.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')


@views.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

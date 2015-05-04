from flask import Flask, render_template, send_from_directory, g, request
from cache.cache import Cache

from config import DOCUMENT_DIRECTORY_PATH, INDEX_LIMIT
from os.path import expanduser

app = Flask(__name__, static_folder='public')


def get_cache():
    cache = getattr(g, '_cache', None)
    if cache is None:
        cache = g._cache = Cache()
    return cache


@app.teardown_appcontext
def teardown_cache(exception):
    cache = getattr(g, '_cache', None)
    if cache is not None:
        cache.close()


@app.route('/')
def index():
    """
    Index route page that lists available collections
    """
    page_num = request.args.get("p") or 0
    try:
        page_num = int(page_num)
    except ValueError:
        page_num = 0
    offset = page_num * INDEX_LIMIT
    return render_template("listing.html", collections=get_cache().get_collections_paginated(INDEX_LIMIT, offset),
                           page=page_num)


@app.route('/c/<string:collection>')
def collection_page(collection):
    """
    Route for the collection page that lists documents in a collection
    """
    return render_template("collection.html", collection=get_cache().get_collection_with_address(collection))


@app.route('/public/<path:path>')
def send_static(path):
    """
    Route for sending static files e.g. CSS, images
    """
    return send_from_directory('public', path)


@app.route('/file/<path:path>')
def send_file(path):
    """
    Route for file downloads
    """
    # If the document path has a tilde, expand it
    path_prefix = expanduser(DOCUMENT_DIRECTORY_PATH)
    return send_from_directory(path_prefix, path)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/help')
def help_page():
    return render_template("help.html")

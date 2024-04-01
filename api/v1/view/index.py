#!/usr/bin/python3
'''
module to generate JSON response
'''

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def index():
    '''function'''
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats', strict_slashes=False)
def stats():
    response = {}
    for key, value in classes.items():
        response[key] = storage.count(value)
    return jsonify(response)

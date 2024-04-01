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
#!/usr/bin/python3
'''
module that imports blueprint
'''

from flask import Blueprint

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1/')

from api.v1.views.index import *

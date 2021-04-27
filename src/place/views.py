# -*- coding: utf-8 -*-
import traceback

from flask import Blueprint, request, abort, g
from flask_expects_json import expects_json
from sentry_sdk import capture_exception

from src.utils import make_cross_domain_response, log_any
from ..constants import AppConstants

# from .tasks import add_task
from ..extensions import gmaps

rest_place = Blueprint('rest_place', __name__, url_prefix='/place')


@rest_place.route('/search', methods=['GET'])
def place_search():
    try:
        query = request.args.to_dict()
        text_search = query.get('text_search')
        result = gmaps.places(query=text_search, language='vn')
        result_place = {
            'places': [],
            'text_search': text_search
        }
        if result and result.get('status') == 'OK':
            result_place['places'] = result.get('results')
        return make_cross_domain_response({
            'status': AppConstants.STATUS_OK,
            'msg': 'success',
            'data': result_place,
            'error_code': AppConstants.NOT_E}, 200)
    except Exception as e:
        print(e)
        capture_exception(e)
        traceback.print_exc(e)
        return make_cross_domain_response({
            'status': 0,
            'error_code': 'ERROR_SERVER',
            'data': {},
            'msg': 'Unknown error'
        }, 200)
    # capture_message('Health check route voter service')

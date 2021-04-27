# -*- coding: utf-8 -*-

from flask import Blueprint, request, abort, g
from flask_expects_json import expects_json

from code.utils import make_cross_domain_response, log_any
from ..constants import AppConstants

# from .tasks import add_task

rest_map = Blueprint('rest_map', __name__, url_prefix='/place')


@rest_map.route('/search', methods=['GET'])
def place_search():
    # capture_message('Health check route voter service')
    return make_cross_domain_response({'status': AppConstants.STATUS_OK, 'msg': 'TheCuaTui Health Check base service',
                                       'error_code': AppConstants.NOT_E}, 200)

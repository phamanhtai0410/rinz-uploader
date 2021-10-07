# -*- coding: utf-8 -*-
import traceback

from flask import Blueprint, request, abort, send_file
from sentry_sdk import capture_exception

from src.config import DefaultConfig
from src.constants import AppConstants
from src.utils import make_cross_domain_response, upload_file_to_s3, log_any, save_media_file, allowed_file

rest_filler = Blueprint('rest_filler', __name__, url_prefix='/file')


@rest_filler.route('/upload', methods=['POST'])
def upload_file():
    if "file" not in request.files:
        return make_cross_domain_response({
            "status": 0,
            "msg": "File is required",
            "error_code": AppConstants.E_FILE_NOT_FOUND,
            "data": {}
        })
    try:
        file = request.files["file"]
        output = upload_file_to_s3(file=file, bucket_name=DefaultConfig.S3_BUCKET)
        if output:
            return make_cross_domain_response({
                "status": 1,
                "msg": "success",
                "error_code": '',
                "data": {
                    'url': '{}/{}'.format(DefaultConfig.S3_URL, output)
                }
            })
    except Exception as e:
        capture_exception(e)
        traceback.print_exc()
        return make_cross_domain_response({
            "status": 0,
            "data": {},
            "msg": "Unknown error",
            "error_code": AppConstants.E_SERVER_ERROR
        })


@rest_filler.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    log_any("Download file", file_id)
    try:
        # TODO check white list file id

        # Hard code for test download game rinz
        if file_id in ['rinz.zip', 'rinz_origin.zip']:
            return send_file(file_id)

        return make_cross_domain_response({
            "status": 0,
            "data": {},
            "msg": "File not found",
            "error_code": AppConstants.E_FILE_NOT_FOUND
        })
    except Exception as e:
        #capture_exception(e)
        traceback.print_exc()
        return make_cross_domain_response({
            "status": 0,
            "data": {},
            "msg": "Unknown error",
            "error_code": AppConstants.E_SERVER_ERROR
        })


@rest_filler.route('/media', methods=['POST'])
def upload_media_file():
    if "file" not in request.files:
        return make_cross_domain_response({
            "status": 0,
            "msg": "File is required",
            "error_code": AppConstants.E_FILE_NOT_FOUND,
            "data": {}
        })
    try:
        file = request.files["file"]
        if not allowed_file(file.filename):
            log_any("Invalid file", file.filename)
            return make_cross_domain_response({
                "status": 0,
                "msg": "Invalid file",
                "error_code": AppConstants.E_INVALID_FILE,
                "data": {}
            })

        output = save_media_file(file=file)
        if output:
            return make_cross_domain_response({
                "status": 1,
                "msg": "success",
                "error_code": '',
                "data": {
                    'url': output
                }
            })
    except Exception as e:
        capture_exception(e)
        traceback.print_exc()
        return make_cross_domain_response({
            "status": 0,
            "data": {},
            "msg": "Unknown error",
            "error_code": AppConstants.E_SERVER_ERROR
        })

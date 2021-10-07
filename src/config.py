# -*- coding: utf-8 -*-

import os
import json
from dotenv import load_dotenv

load_dotenv()


class BaseConfig(object):
    PROJECT = "the-cua-tui-upload"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = '\xd2\x0c\xa9\xb7\xd9E\xda-\x1e\xdb;\xb8\x0c\xfc\xbf\xf3\x16[\xa2x\xd5s\x83\xe3'


class DefaultConfig(BaseConfig):
    DEBUG = True

    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    ACCEPT_LANGUAGES = ['vi']
    BABEL_DEFAULT_LOCALE = 'en'

    # Celery
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_TASK_RESULT_EXPIRES = os.getenv('CELERY_TASK_RESULT_EXPIRES')
    CELERY_TASK_RESULT_EXPIRES = int(CELERY_TASK_RESULT_EXPIRES) if CELERY_TASK_RESULT_EXPIRES else 600
    CELERY_DEFAULT_QUEUE = 'voter_celery'
    CELERY_ROUTES = {
        'base.tasks.health_check': {'queue': 'base_health_check'},
    }
    CELERY_TRACK_STARTED = "True"

    CELERY_ENABLE_UTC = False
    CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'
    SENTRY_DSN = os.getenv('SENTRY_DSN')

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    REDIS_URL = os.getenv('REDIS_URL')

    S3_KEY = os.getenv("S3_KEY")
    S3_SECRET = os.getenv("S3_SECRET")
    S3_ENDPOINT = os.getenv("S3_ENDPOINT")
    S3_BUCKET = os.getenv("S3_BUCKET")
    S3_URL = os.getenv("S3_URL")

    UPLOAD_VIDEO_PATH = os.getenv("UPLOAD_VIDEO_PATH", "/mnt/upload/")
    UPLOAD_AUDIO_PATH = os.getenv("UPLOAD_AUDIO_PATH", "/mnt/upload/")

    ALLOWED_EXTENSIONS = ['mp4', 'mp3']

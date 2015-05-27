#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR:   fanzeyi


import os
import tempfile
from plim import preprocessor

def load_upload_dir():
    d = os.getenv('ERU_PERMDIR', '')
    if d:
        return d
    return tempfile.mkdtemp()

DEBUG = bool(os.getenv('DEBUG', ''))

MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'p')

MAX_CONTENT_LENGTH = 32 * 1024 * 1024

MAKO_PREPROCESSOR = preprocessor
MAKO_TRANSLATE_EXCEPTIONS = False

UPLOAD_FOLDER = load_upload_dir()

SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_DATABASE,
)

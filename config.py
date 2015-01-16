#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AUTHOR:   fanzeyi


import os
import yaml
import tempfile
from plim import preprocessor


def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.load(f)


def load_upload_dir():
    d = os.getenv('NBE_PERMDIR', '')
    if not d:
        return tempfile.mkdtemp()
    return d


DEBUG = True
MAX_CONTENT_LENGTH = 32 * 1024 * 1024
MAKO_PREPROCESSOR = preprocessor
MAKO_TRANSLATE_EXCEPTIONS = False
UPLOAD_FOLDER = load_upload_dir()
SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@{host}:{port}/{db}'.format(**load_config()['mysql'])

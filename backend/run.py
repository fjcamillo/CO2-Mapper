from os import path, environ as env
from dotenv import load_dotenv
from app import app
import logging
from logging.handlers import RotatingFileHandler
from collections import namedtuple

load_dotenv(path.join(path.dirname(__file__), '.env'))

create_config = namedtuple('create_config', ['HOST', 'PORT'])
CONFIG = create_config(
    HOST=env['HOST'],
    PORT=env['PORT']
)
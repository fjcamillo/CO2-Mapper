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

if __name__ == '__main__':
    handler = RotatingFileHandler('mapper.log', maxBytes=1000, backupCount=1)
    app.run(debug=True, port=CONFIG.PORT, host=CONFIG.HOST)
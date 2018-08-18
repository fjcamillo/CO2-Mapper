from flask import Flask
from dotenv import load_dotenv
from os import path, environ as env

load_dotenv(path.join(path.dirname(__file__), '../.env'))

app = Flask(__name__)

from app.routes import carbon
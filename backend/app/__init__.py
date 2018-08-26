from flask import Flask
from dotenv import load_dotenv
from os import path, environ as env
from schemas import carbon
from flask_graphql import GraphQLView

load_dotenv(path.join(path.dirname(__file__), '../.env'))

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema = carbon.schema,
        graphiql=True
    )
)
# from app.routes import carbon
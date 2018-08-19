from app import app
from flask_graphql import GraphQLView

from ..models import carbon as carbonModel
from ..schemas import carbon as carbonSchema

@app.add_url_rule('/graphql')
def graph():
    return GraphQLView.as_view(
        'graphql',
        schema=carbonSchema.schema,
        graphiql=True
    )

@app.teardown_appcontext
def shutdown_session(exception=None):
    carbonModel.db_session.remove()


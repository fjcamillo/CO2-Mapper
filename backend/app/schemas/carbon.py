import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from ..models import carbon as CarbonModel

class Carbon(SQLAlchemyObjectType):
    class Meta:
        model = CarbonModel.Carbon
        interfaces = (relay.Node, )

class CarbonConnection(relay.Connection):
    class Meta:
        node = Carbon

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_carbon = SQLAlchemyConnectionField(CarbonConnection)

schema = graphene.Schema(query = Query)
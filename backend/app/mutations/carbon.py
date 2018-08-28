import graphene
from graphene import relay
from ..data import create_carbon

class InputCarbon(relay.ClientIDMutation):

    class Input:
        longitude = graphene.String(required=True)
        latitude = graphene.String(required=True)
        reading = graphene.String(required=True)
        device_identification = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, ):
        pass
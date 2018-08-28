import graphene
from graphene import relay
from ..data import carbon as carbonData


class InputCarbon(relay.ClientIDMutation):

    class Input:
        longitude = graphene.String(required=True)
        latitude = graphene.String(required=True)
        reading = graphene.String(required=True)
        device_identification = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(
            cls, 
            root, 
            info, 
            longitude, 
            latitude, 
            reading, 
            device_identification):
        carbon = carbonData.create_carbon(
            longitude,
            latitude,
            reading,
            device_identification
        )
        return cls(InputCarbon(carbon=carbon))

class Mutation(graphene.ObjectType):
    input_carbon = InputCarbon.Field()
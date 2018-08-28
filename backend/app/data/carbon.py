from ..models import carbon as carbonModels
import datetime

def create_carbon(
    longitude,
    latitude,
    reading,
    device_identification
):
    new_carbon = carbonModels.Carbon(
        created_at=str(datetime.datetime.now()),
        updated_at=str(datetime.datetime.now()),
        longitude = longitude,
        latitude = latitude,
        reading = reading,
        device_identification = device_identification,
    )
    return new_carbon
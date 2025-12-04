import time
import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/temperature")
def get_temperature(location: str = None, sensorID: str = None):
    location, sensorID = generate_temperature_data(location)
    print(location)
    print(sensorID)
    return get_response(location, sensorID)

@app.get("/temperature/{sensorID}")
def get_temperature_id(sensorID: str):
    location, sensorID = generate_temperature_data(None, sensorID)
    return get_response(location, sensorID)

def generate_temperature_data(location=None, sensorID=None):

    if location is None:
        sensor_id_map = {
            "1": "Living Room",
            "2": "Bedroom",
            "3": "Kitchen"
        }
        location = sensor_id_map.get(sensorID, "Unknown")

    if sensorID is None:
        location_map = {
            "Living Room": "1",
            "Bedroom": "2",
            "Kitchen": "3"
        }
        sensorID = location_map.get(location, "0")

    return location, sensorID

def get_response(location, sensorID):
    return {
        "value": 18.0 + float(time.time() * 1e9 % 10) + (float(time.time() * 1e9) % 100) / 100.0,
        "unit": "°C",
        "timestamp": datetime.datetime.now().isoformat(),
        "location": location,
        "status": "OK",
        "sensor_id": sensorID,
        "sensor_type": "temperature",
        "description": "Temperature sensor in " + location
    }
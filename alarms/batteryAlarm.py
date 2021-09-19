import http.client as http
import socket
from json.decoder import JSONDecoder, JSONDecodeError
from RPi import GPIO


def get_level(level_id, pass_code):
    host = "battery-service-staging.herokuapp.com"
    connection = http.HTTPSConnection(host)
    try:
        connection.connect()
        connection.request("GET", f"https://{host}/v1/batterylevel/{level_id}/{pass_code}")
        response = connection.getresponse()
        if response.status == 200:
            data = JSONDecoder().decode(str(response.read().decode("UTF8")))
            return BatteryAlarm(data.get("status"), data.get("level"))
        else:
            raise http.HTTPException("Non 200 http response code received")
    except (http.HTTPException, JSONDecodeError, socket.gaierror):
        print("There is a problem")
        raise
    except Exception:
        raise
    finally:
        connection.close()


def get_pin_state(level_id, pass_code, threshold_level):
    try:
        b = get_level(level_id, pass_code)
        if b.status == 1 and b.level < threshold_level:
            return GPIO.HIGH
        return GPIO.LOW
    except Exception:
        raise

class BatteryAlarm:
    def __init__(self, status, level):
        self.status = status
        self.level = level

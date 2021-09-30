# import http.client as http
# import socket
import socket

from RPi import GPIO
import requests


def get_level(level_id, pass_code):
    host = "battery-service-staging.herokuapp.com"
    # connection = http.HTTPSConnection(host)
    response = None
    try:
        # connection.connect()
        # connection.request("GET", f"https://{host}/v1/batterylevel/{level_id}/{pass_code}")
        # response = connection.getresponse()
        response = requests.get(f"https://{host}/v1/batterylevel/{level_id}/{pass_code}")
        # response.raise_for_status()
        if response.status_code == 200:
            # data = JSONDecoder().decode(str(response.read().decode("UTF8")))
            data = response.json()
            return BatteryAlarm(data.get("status"), data.get("level"))
        else:
            raise requests.exceptions.HTTPError('Non 200 response code received!')
    except (requests.exceptions.HTTPError, socket.gaierror):
        print("There is a problem")
        raise
    except Exception:
        raise
    finally:
        # connection.close()
        if response is not None:
            response.close()


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

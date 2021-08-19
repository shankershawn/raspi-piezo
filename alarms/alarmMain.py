from time import sleep
from RPi import GPIO
import batteryAlarm


def process_main_alarm():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
        while True:
            pin_state = batteryAlarm.get_pin_state("poom", "tzOsQ7es", 40)
            print(f"Pin state: {pin_state}")
            GPIO.output(29, pin_state)
            sleep(2)
            GPIO.output(29, GPIO.LOW)
            sleep(2)
    except KeyboardInterrupt:
        print("Exiting")
    finally:
        GPIO.cleanup()


process_main_alarm()

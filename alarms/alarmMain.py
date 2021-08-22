from time import sleep
from RPi import GPIO

import batteryAlarm


def process_main_alarm():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
        prev_pin_state = -1
        while True:
            pin_state = batteryAlarm.get_pin_state("poom", "tzOsQ7es", 40)
            if prev_pin_state != pin_state:
                print(f"Pin state: {pin_state}")
            GPIO.output(29, pin_state)
            sleep(2)
            GPIO.output(29, GPIO.LOW)
            sleep(2)
            prev_pin_state = pin_state
    except KeyboardInterrupt:
        print("Exiting")
    finally:
        GPIO.cleanup()


process_main_alarm()

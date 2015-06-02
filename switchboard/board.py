import RPi.GPIO as GPIO

class Board():

    def __init__(self, mode=GPIO.BCM):
        self.mode = mode

        GPIO.setwarnings(False)
        self.set_mode(self.mode)

    def set_mode(self, mode):
        GPIO.setmode(mode)

    def get_mode(self):
        return self.mode

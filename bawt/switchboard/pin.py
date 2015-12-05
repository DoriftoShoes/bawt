import RPi.GPIO as GPIO

class Pin():

    def __init__(self, pin, mode=GPIO.OUT):
        self.pin = pin
        self.mode = mode
        self.state = ''

        self.setup()

    def setup(self):
        GPIO.setup(self.pin, self.mode)

    def on(self):
        if self.mode != GPIO.OUT:
            raise Exception("Can only turn on output pins")
            return False
        else:
            GPIO.output(self.pin, True)
            self.state = 'on'
            return True

    def off(self):
        if self.mode != GPIO.OUT:
            raise Exeption("Can only turn off output pins)
            return False
        else:
            GPIO.output(self.pin, False)
            self.state = 'off'
            return True

    def toggle(self):
        if self.state == 'on':
            self.off()
        else:
            self.on()

    def get_state(self):
        return self.state

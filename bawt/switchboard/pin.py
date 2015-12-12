#try:
#    import RPi.GPIO as GPIO
#    bcm = GPIO.BCM
#except:
#    from bawt.mock.RPi import GPIO
from bawt.mock.RPi import GPIO

class Pin:

    def __init__(self, pin, mode=GPIO.OUT):
        """
        :param pin: Pin number
        :param mode: Input or Output
        """
        self.pin = pin
        self.mode = mode
        self.state = None

        self.setup()

    def setup(self):
        """
        Initialize the pin.
        """
        GPIO.setup(self.pin, self.mode)

    def on(self):
        """
        Turn the pin on.
        :return: Boolean
        """
        if self.mode != GPIO.OUT:
            raise Exception("Can only turn on output pins")
        else:
            GPIO.output(self.pin, True)
            self.state = 'on'
            return True

    def off(self):
        """
        Turn the pin off.
        :return: Boolean
        """
        if self.mode != GPIO.OUT:
            raise Exception("Can only turn off output pins")
        else:
            GPIO.output(self.pin, False)
            self.state = 'off'
            return True

    def toggle(self):
        """
        Toggles the pin on or off.
        :return: Boolean
        """
        try:
            if self.state == 'on':
                self.off()
            else:
                self.on()
            return True
        except Exception:
            raise Exception("Unable to toggle pin")

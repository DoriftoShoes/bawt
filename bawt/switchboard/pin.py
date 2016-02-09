import bawt.log as logging
import os

ci = os.environ.get('CI', False)

if not ci:
    try:
        import RPi.GPIO as GPIO
    except:
        from bawt.mock.RPi import GPIO
        print(GPIO.ANNOUNCEMENT)
else:
    from bawt.mock.RPi import GPIO

LOG = logging.get_logger(__name__)


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

        try:
            GPIO.output(self.pin, True)
        except Exception as e:
            LOG.critical("Pin %i could not be enabled" % self.pin)

        self.state = 'on'
        return True

    def off(self):
        """
        Turn the pin off.
        :return: Boolean
        """
        if self.mode != GPIO.OUT:
            raise Exception("Can only turn off output pins")

        try:
            GPIO.output(self.pin, False)
        except Exception as e:
            LOG.critical("Pin %i could not be disabled" % self.pin)

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
            raise Exception("Unable to toggle pin %i" % self.pin)

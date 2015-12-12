#try:
#    import RPi.GPIO as GPIO
#    bcm = GPIO.BCM
#except:
#    from bawt.mock.RPi import GPIO
#    print(GPIO.ANNOUNCEMENT)

from bawt.mock.RPi import GPIO

class Board:

    def __init__(self, mode=GPIO.BCM):
        """
        :param mode: Set the board mode.  Default: GPIO.BCM
        """
        self.mode = mode

        GPIO.setwarnings(False)
        self.set_mode(self.mode)

    def set_mode(self, mode):
        """
        Set board mode.
        :param mode: The mode to set on the board.
        """
        self.mode = mode
        GPIO.setmode(mode)

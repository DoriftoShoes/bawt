
class GPIO:

    BCM = "BCM"
    OUT = "OUT"

    def __init__(self):
        pass

    @staticmethod
    def setwarnings(warnings=False):
        GPIO.warnings = warnings

    @staticmethod
    def setmode(mode):
        GPIO.mode = mode

    @staticmethod
    def setup(pin, mode):
        return True

    @staticmethod
    def output(pin, output=False):
        return True

    @staticmethod
    def input(pin, input=False):
        return True
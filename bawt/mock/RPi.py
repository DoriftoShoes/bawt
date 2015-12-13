class GPIO(object):
    BCM = 11
    BOARD = 10
    BOTH = 33
    FALLING = 32
    HARD_PWM = 43
    HIGH = 1
    I2C = 42
    IN = 1
    LOW = 0
    OUT = 0
    PUD_DOWN = 21
    PUD_OFF = 20
    PUD_UP = 22
    RISING = 31
    RPI_INFO = {'P1_REVISION': 3, 'RAM': '1024M', 'REVISION': 'a21041', 'TYPE': 'Pi2 Model B', 'PROCESSOR': 'BCM2836',
                'MANUFACTURER': 'Embest'}
    RPI_REVISION = 3
    SERIAL = 40
    SPI = 41
    UNKNOWN = -1
    VERSION = '0.5.11'
    ANNOUNCEMENT = '''
    ############################################################
    #                                                          #
    #              WARNING: RPi.GPIO unavailable.              #
    #         bawt.mock.RPi.GPIO will be used instead          #
    #                                                          #
    ############################################################
    '''

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

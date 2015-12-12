import unittest

try:
    import RPi.GPIO as GPIO
except ImportError:
    from bawt.mock.RPi import GPIO
    print(GPIO.ANNOUNCEMENT)

from bawt.switchboard.board import Board
from bawt.switchboard.pin import Pin

class TestBoard(unittest.TestCase):

    BOARD = Board()

    def test_board_set_mode(self):
        TestBoard.BOARD.set_mode(GPIO.BCM)
        self.assertEquals(TestBoard.BOARD.mode,GPIO.BCM, 'Board mode not set correctly')

if __name__ == '__main__':
    unittest.main()

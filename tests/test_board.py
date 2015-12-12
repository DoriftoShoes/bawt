import mock
import unittest

from bawt.mock.RPi import GPIO

from bawt.switchboard.board import Board
from bawt.switchboard.pin import Pin

@mock.patch("RPi.GPIO.setmode", autospec=True)
class TestBoard(unittest.TestCase):

    BOARD = Board()

    def test_board_set_mode(self, mock_mode):
        TestBoard.BOARD.set_mode(GPIO.BCM)
        self.assertEquals(TestBoard.BOARD.mode,GPIO.BCM, 'Board mode not set correctly')

if __name__ == '__main__':
    unittest.main()

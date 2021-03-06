import unittest

from bawt.mock.RPi import GPIO

from bawt.switchboard.board import Board


class TestBoard(unittest.TestCase):

    BOARD = Board()

    def test_board_set_mode(self):
        TestBoard.BOARD.set_mode(GPIO.BCM)
        self.assertEquals(TestBoard.BOARD.mode, GPIO.BCM, 'Board mode not set correctly')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    unittest.TextTestRunner(verbosity=2).run(suite)

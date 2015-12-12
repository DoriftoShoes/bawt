import unittest
from bawt.switchboard.board import Board
from bawt.switchboard.pin import Pin

class TestPin(unittest.TestCase):

    BOARD = Board()
    PIN = Pin(1)

    def test_pin_on(self):
        self.assertTrue(TestPin.PIN.on(), 'Pin failed to turn on')

    def test_pin_off(self):
        self.assertTrue(TestPin.PIN.off(), 'Pin failed to turn off')

    def test_pin_toggle(self):
        self.assertTrue(TestPin.PIN.toggle(), 'Pin failed to toggle')

    def test_pin_get_state_on(self):
        TestPin.PIN.on()
        self.assertEqual(TestPin.PIN.state, 'on', 'Pin was not in state "on"')

    def test_pin_get_state_off(self):
        TestPin.PIN.off()
        self.assertEqual(TestPin.PIN.state, 'off', 'Pin was not in state "off"')

if __name__ == '__main__':
    unittest.main()

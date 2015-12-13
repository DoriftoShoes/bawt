import unittest

from bawt.mock.RPi import GPIO

from bawt.subsystems.camera import Camera


class TestCamera(unittest.TestCase):

    CAM = Camera()

    def test_camera_setup(self):
        TestCamera.CAM.setup()
        self.assertIsInstance(TestCamera.CAM.remote, dict, 'Remote configuration wrong')

    def test_camera_initialize(self):
        TestCamera.CAM.setup()
        TestCamera.CAM._initialize()
        self.assertTrue(TestCamera.CAM._is_initialized, 'Failed to initialize')

    def test_camera_get_filepath_no_ts(self):
        TestCamera.CAM.setup()
        TestCamera.CAM._get_filepath(name='test', use_timestamp=False)
        self.assertEquals(TestCamera.CAM.fname, "%s/test.jpg" % TestCamera.CAM.picture_directory, 'File path incorrect')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCamera)
    unittest.TextTestRunner(verbosity=2).run(suite)
